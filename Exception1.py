class SalaryNotInRangeError(Exception):
    def __init__(self,salary,msg="salary not in range"):
        self.salary=salary
        self.msg=msg

    def __str__(self):
        return f'{self.salary}->{self.msg}'


try:
    salary=int(input('Enter salary:'))
    if not 5000<salary<15000:
        raise SalaryNotInRangeError(salary)

except SalaryNotInRangeError as s:
    print(s)