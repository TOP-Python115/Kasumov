class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Расчет зарплаты')
        print('===================')
        for employee in employees:
            print(f'Расчет зарплаты для : {employee.id} - {employee.name}')
            print(f'- Итоговый расчет: {employee.calculate_payroll()} рублей')
            print('')

class Employee:
  def __init__(self, id: int,
                     name: str) -> None:
    self.id = id
    self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
      return self.hours_worked * self.hour_rate
      

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
  

salary_employee = SalaryEmployee(1, 'Максим Сергиенко', 45000)
hourly_employee = HourlyEmployee(2, 'Наталия Штыга', 44, 700)
commission_employee = CommissionEmployee(3, 'Евгений Петров', 55000, 12000)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])
