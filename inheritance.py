import logging

logging.basicConfig(filename='oops_log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class Person:

    def __init__(self, details_dict):
        self.name = details_dict.get("name")
        self.dob = details_dict.get("dob")
        self.city = details_dict.get("city")


class Students(Person):

    def __init__(self, details_dict):
        super().__init__(details_dict)
        self.roll_no = details_dict.get("roll_no")
        self.year = details_dict.get("year")


class Professor(Person):

    def __init__(self, details_dict):
        super().__init__(details_dict)
        self.salary = details_dict.get("salary")


class Automobile(Students):

    def __init__(self, details_dict):
        super().__init__(details_dict)
        self.course_fees = details_dict.get("course_fees")


class ComputerScience(Students):

    def __init__(self, details_dict):
        super().__init__(details_dict)
        self.course_fees = details_dict.get("course_fees")


if __name__ == '__main__':
    student_one = Automobile({"name": "Elavarasu", "dob": 1996, "roll_no": "14AU013", "city": "Salem", "year": 2018,
                              "course_fees": 120000})
    student_two = ComputerScience({"name": "Nantha", "dob": 1996, "roll_no": "14CS033", "city": "Salem", "year": 2017,
                                   "course_fees": 100000})
    professor_one = Professor({"name": "Senthil", "dob": 1996, "city": "Salem", "salary": 50000})
    print(student_one.name)
    print(student_two.name)
    print(professor_one.name)
