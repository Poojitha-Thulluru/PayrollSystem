class SalariedEmployee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculatePay(self):
        return self.salary


class HourlyEmployee:
    def __init__(self, name, hourlyRate, hoursWorked):
        self.name = name
        self.hourlyRate = hourlyRate
        self.hoursWorked = hoursWorked

    def calculatePay(self):
        return self.hourlyRate * self.hoursWorked


salaried_employee = SalariedEmployee("Ram", 5000.0)
hourly_employee = HourlyEmployee("Hari", 15.0, 40.0)

print("Salaried Employee")
print("Name:", salaried_employee.name)
print("Monthly Salary:", salaried_employee.calculatePay())

print("\nHourly Employee")
print("Name:", hourly_employee.name)
print("Weekly Pay:", hourly_employee.calculatePay())
