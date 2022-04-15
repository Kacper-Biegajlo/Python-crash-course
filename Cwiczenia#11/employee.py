class Employee:
    """Few functions regarding emoloyee informations."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_rise(self, raise_amount=5000):
        """Gives a raise to employee - default value 5000 but accepts other"""
        self.annual_salary += raise_amount

