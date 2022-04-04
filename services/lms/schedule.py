from datetime import datetime
from services.lms import LMS

URL = "https://lms.tuit.uz/student/schedule"



def to_dict(t):
	def make_dict(l: list) -> dict:
		key, val = l
		return {
			key: val if len(val)>0 and val[0] not in "'\"" else 
						datetime.strptime((val[1:-1]), '%Y-%m-%dT%H:%M:%S') if 
						key == 'start' else val[1:-1]
		}
	ans = []
	last = ''
	for i in t:
		if i=='{':
			last = ''
		elif i == '}':
			ans.append(last.split(','))
			for j, a in enumerate(ans[-1]):
				ans[-1][j] = make_dict(list(map(lambda x: x.strip(), a.strip().split(': '))))
		else:
			last += i

	def union(ll):
		data = {}
		for l in ll:
			data.update(l)
		return data
	for i in range(len(ans)):
		ans[i] = union(ans[i])
	return ans


async def parse(message) -> dict:
    lms = await LMS(message, URL)
    text = lms.get(URL).text
    text = text[text.find("events: ")+7:]
    text = text[:text.find("]")]
    data = {
        'schedule': to_dict(text)
    }
    return data


async def get_formated_text(message) -> str:
    data = await parse(message)
    if not data.get('schedule'):
        return "Schedule not found:(:"
    data['schedule'].sort(key=lambda x: x['start'])
    today = []
    for day in  data['schedule']:
        if day['start'].date() == datetime.now().date():
            today.append(day)
    if not today:
        return "There are no lessons today %s." % datetime.now().date()
    text = []
    for lesson in today:
        text.append(
            f"💼Subject: {lesson['title']}\n"
            f"🕐Start: {lesson['start']}\n"
        )
    return text
