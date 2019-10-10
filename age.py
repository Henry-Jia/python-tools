import datetime as dt

class formula:
    def __init__(self, first_name, second_name, birthdate_year):
        self.second_name=str(second_name).upper()
        self.first_name=str(first_name).upper()
        self.birthdate=birthdate_year

    def age(self):
        return dt.datetime.today().year-self.birthdate


age=formula("Lim", "Boris", 1987)
print(age.age())