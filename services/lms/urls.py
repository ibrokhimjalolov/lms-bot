

class URL:
    path = ""
    
    def parse(self) -> dict:
        raise NotImplementedError()      

    def render(self) -> dict:
        raise NotImplementedError()


HOME = URL()
HOME.path = "https://lms.tuit.uz/dashboard/news"
def parse():
    return dict()
HOME.parse = parse


MY_COURSES = URL()
MY_COURSES.path = "https://lms.tuit.uz/student/my-courses"
def parse(self):
    return dict()
MY_COURSES.parse = parse
