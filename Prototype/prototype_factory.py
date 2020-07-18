import copy


# the idea for prototype factory is that instead of deep copying the prototype by hand we wrap it in a class so the user
# can connect to it through an API (via some method)
class Address:
    def __init__(self, street_address, suite, city):
        self.suite = suite
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.suite}'


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('123 East Dr', 0, 'London'))
    aux_office_employee = Employee('', Address('123B West Dr', 0, 'London'))

    @staticmethod
    def __new_emp(proto, name, suite) -> Employee:
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_emp(name, suite):
        return EmployeeFactory.__new_emp(EmployeeFactory.main_office_employee, name, suite)

    @staticmethod
    def new_aux_emp(name, suite):
        return EmployeeFactory.__new_emp(EmployeeFactory.aux_office_employee, name, suite)


john = EmployeeFactory.new_main_emp('John', 101)
jane = EmployeeFactory.new_aux_emp('Jane', 102)
print(john, '\n', jane)
