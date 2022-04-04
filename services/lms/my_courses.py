from bs4 import BeautifulSoup

from services.lms import LMS

URL = "https://lms.tuit.uz/student/my-courses"


async def parse(message):
    lms = await LMS(message, URL)
    soup = BeautifulSoup(lms.get(URL).text, 'html.parser')
    semester = soup.find('option', {'selected': True})
    if not semester:
        return {}
    url = f"{URL}/data?semester_id={semester.get('value')}"
    data = {
        "semester": {
            "id": semester.get('value'),
            "name": ' '.join(semester.text.split())
        }
    }
    data['courses'] = lms.get(url).json().get('data', [])
    lms.close()
    return data


async def get_formated_text(message) -> str:
    data = await parse(message)
    if not data.get('semester'):
        return "Not Found"
    text = f"<b>Semester: {data.get('semester').get('name')}</b>\nSubjects 👇:\n"
    for course in data.get('courses'):
        text += f"💼 <b>{course.get('subject')}</b>: <i>attendance-❌{course.get('attendance')}</i>\n"
    return text
