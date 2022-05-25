from os import stat
from bs4 import BeautifulSoup

from services.lms import LMS

URL = "https://lms.tuit.uz/student/my-courses"


async def parse(message):
    id = message.text
    lms = await LMS(message, URL)
    soup = BeautifulSoup(lms.get(URL).text, 'html.parser')
    semester = soup.find('option', {'selected': True})
    if not semester:
        return {}
    url = "https://lms.tuit.uz/student/my-courses/show/" + id
    soup = BeautifulSoup(lms.get(url).text, 'html.parser')
    lms.close()
    data = {
        'tasks': []
    }
    tasks = soup.find('table', {'id': 'simple-table1'})
    if not tasks:
        return {}
    stats = soup.find('table')
    data['stats'] = {
        "achieved": stats.find_all('h4')[0].text.strip(),
        "max": stats.find_all('h4')[1].text.strip(),
        "rating": stats.find_all('h4')[2].text.strip(),
        "grade": stats.find_all('h4')[3].text.strip()
    }
    tasks = tasks.find_all('tr')[1:]
    for task in tasks:
        data['tasks'].append({
            'teacher': task.find_all('td')[0].text.strip(),
            'task_name': task.find('b').text.strip(),
            'deadline': task.find_all('td')[2].text.strip(),
            'score': task.find_all('button')[0].text+"/"+task.find_all('button')[1].text
        })
    return data


async def get_formated_text(message) -> str:
    data = await parse(message)
    if not data.get('tasks'):
        return "Tasks not found🥳"
    text = []
    for task in data.get('tasks'):
        text.append(
            f"👨‍🏫Teacher: <b>{task['teacher']}</b>\n"
            f"📝Task name: <b>{task['task_name']}</b>\n"
            f"⏳Deadline: <b>{task['deadline']}</b>\n"
            f"🎲Score: <b>{task['score']}</b>\n"
        )
    text = '\n'.join(text)
    text = [
        f"🕵️‍♂️Achieved points: <b>{data['stats']['achieved']}</b>\n"
        f"💯Max points: <b>{data['stats']['max']}</b>\n"
        f'{"✅" if float(data["stats"]["rating"][:-1])>=60 else "❌"}Rayting: <b>{data["stats"]["rating"]}</b>\n'
        f"🇺🇿Grade: <b>{data['stats']['grade']}</b>\n"
    ] + [text]
    return text
