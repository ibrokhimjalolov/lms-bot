from services.lms import LMS

URL = "https://lms.tuit.uz/auth/login"


async def parse(message):
    lms = await LMS(message, URL)
    data = {}
    return data



async def get_formated_text(message):
    data = await parse(message)
    return "%s" % data