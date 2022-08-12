import logging
import random
from abc import ABC, abstractmethod

logging.basicConfig(filename='oops_log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class Computation(ABC):

    @abstractmethod
    def emp_status(self):
        pass

    @abstractmethod
    def wage_computation(self):
        pass


class Employee(Computation):

    def __init__(self, data_dict):
        self.employee_wage_per_hour = data_dict.get("employee_wage_per_hour")
        self.max_working_days = data_dict.get("max_working_days")
        self.max_working_hours = data_dict.get("max_working_hours")
        self.employee_wage_for_month = 0
        self.employee_working_days = 0
        self.employee_working_hours = 0
        self.day_with_wage = {}

    def emp_status(self):
        """
        This function check the employee status
        :return: integer
        """
        try:
            employee_status = random.randint(0, 2)
            return employee_status
        except Exception as ex:
            logger.exception(ex)

    def wage_computation(self):
        """
        This function computes wage of an employee
        :return: None
        """
        try:
            is_absent = 0
            is_full_time = 1
            is_part_time = 2
            full_time_hour = 8
            part_time_hour = 4
            while self.employee_working_days < self.max_working_days and \
                    self.employee_working_hours < self.max_working_hours:
                employee_status = self.emp_status()

                if employee_status == is_full_time:
                    employee_hours = full_time_hour
                elif employee_status == is_part_time:
                    employee_hours = part_time_hour
                else:
                    employee_hours = is_absent

                employee_wage = employee_hours * self.employee_wage_per_hour
                self.employee_wage_for_month += employee_wage
                self.employee_working_hours += employee_hours
                self.employee_working_days += 1
                self.day_with_wage.update({self.employee_working_days: employee_wage})
            return self.employee_wage_for_month
        except Exception as ex:
            logger.exception(ex)


if __name__ == '__main__':
    wage_per_hour = int(input("Enter wage per hour: "))
    max_days = int(input("Enter max working days: "))
    max_hours = int(input("Enter max working hours: : "))
    details_dict = {"employee_wage_per_hour": wage_per_hour, "max_working_days": max_days, "max_working_hours": max_hours}
    emp = Employee(details_dict)
    wage = emp.wage_computation()
    print(wage)
