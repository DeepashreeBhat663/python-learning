from abc import ABC,abstractmethod
class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class manager(employee):
    def calculate_salary(self,working_hours,rate_per_hour):
        salary=working_hours*rate_per_hour
        print(salary)
m=manager()
m.calculate_salary(13,5)
    