from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import requests

from .consts import HEADERS

LOGIN_URL = "https://lms.tuit.uz/auth/login"
HOME_URL = "https://lms.tuit.uz/dashboard/news"


class _LMS:

    async def init(self, message, target=HOME_URL):
        self.message = message
        self.user = message.user
        self.target = target
        self.session = requests.Session()
        if not self.user.login or not self.user.password:
            await self.message.answer(
                "Set login and password to use."
            )
            return
        self.session.headers.update(HEADERS)
        self.set_cookies(self.user.cookies)
        if not self.is_authenticated():
            await self.message.answer("Session expired. Trying log-in...")
            self.login()
            if not self.is_authenticated():
                await self.message.answer("Failed log-in. Check login and password.")
            else:
                await self.message.answer("Successfully loged-in. New session started.")
    
    def login(self) -> bool:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(LOGIN_URL)
        elem = driver.find_element_by_css_selector("input#login")
        for ch in self.user.login:
            elem.send_keys(ch)
        elem = driver.find_element_by_css_selector("input#password")
        for ch in self.user.password:
            elem.send_keys(ch)
        elem = driver.find_element_by_css_selector("button#login-btn")
        elem.click()
        cookies = driver.get_cookies()
        self.set_cookies(cookies)
        self.user.cookies = cookies
        self.user.save(update_fields=['cookies'])
        driver.close()

    def get(self, url=None):
        url = url or self.target
        return self.session.get(url)
    
    def set_cookies(self, cookies):
        for c in cookies:
            self.session.cookies.set(
                c['name'], c['value']
            )
    
    def is_authenticated(self) -> bool:
        return self.session.get(self.target).url == self.target
    
    def close(self):
        try:
            self.session.close()
        except Exception:
            pass


async def _lms(message, target) -> _LMS:
    lms = _LMS()
    await lms.init(message, target)
    return lms

LMS = _lms
