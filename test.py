html = """{
                    title: "Введение в web-программирование-WEB205-L2 (B-319)",
                    start: "2022-04-04T13:30:00",
                    allDay: false,
                    className: "bg-teal"
                },{
                    title: "Принципы управления-MAP202-1 (E-106)",
                    start: "2022-04-04T15:00:00",
                    allDay: false,
                    className: "bg-brown"
                },{
                    title: "Введение в web-программирование-WEB205 (A-131)",
                    start: "2022-04-04T16:30:00",
                    allDay: false,
                    className: "bg-teal"
                },{
                    title: "Организация компьютера-CAO204-2 (A-010)",
                    start: "2022-04-05T13:30:00",
                    allDay: false,
                    className: "bg-danger"
                },{
                    title: "Проектирование алгоритмов-CAL204-L2 (E-207)",
                    start: "2022-04-05T15:00:00",
                    allDay: false,
                    className: "bg-success"
                },{
                    title: "Вероятность и статистика-MTH204-2 (A-312)",
                    start: "2022-04-05T16:30:00",
                    allDay: false,
                    className: "bg-warning"
                },{
                    title: "Принципы управления-MAP202 (A-116)",
                    start: "2022-04-06T13:30:00",
                    allDay: false,
                    className: "bg-brown"
                },{
                    title: "Принципы управления-MAP202 (A-116)",
                    start: "2022-04-06T15:00:00",
                    allDay: false,
                    className: "bg-brown"
                },{
                    title: "Введение в web-программирование-WEB205 (A-128A)",
                    start: "2022-04-06T16:30:00",
                    allDay: false,
                    className: "bg-teal"
                },{
                    title: "Организация компьютера-CAO204 (A-408)",
                    start: "2022-04-07T13:30:00",
                    allDay: false,
                    className: "bg-danger"
                },{
                    title: "Проектирование алгоритмов-CAL204-L2 (E-207)",
                    start: "2022-04-07T15:00:00",
                    allDay: false,
                    className: "bg-success"
                },{
                    title: "Вероятность и статистика-MTH204 (A-318)",
                    start: "2022-04-07T16:30:00",
                    allDay: false,
                    className: "bg-warning"
                },{
                    title: "Организация компьютера-CAO204 (D-307)",
                    start: "2022-04-09T13:30:00",
                    allDay: false,
                    className: "bg-danger"
                },{
                    title: "Проектирование алгоритмов-CAL204 (E-219)",
                    start: "2022-04-09T15:00:00",
                    allDay: false,
                    className: "bg-success"
                },{
                    title: "Вероятность и статистика-MTH204-L2 (A-118)",
                    start: "2022-04-09T16:30:00",
                    allDay: false,
                    className: "bg-warning"
                }
"""

from datetime import datetime



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