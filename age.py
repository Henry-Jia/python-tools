import datetime as dt

class formula:
    def __init__(self, first_name, second_name, birthdate_year):
        self.second_name=str(second_name).title() # title text format looks good.
        self.first_name=str(first_name).title()
        self.birthdate=birthdate_year

    def age(self):
        try:
            result_age dt.datetime.today().year-self.birthdate
            return result_age
        execpt:
            print("Some Error occured")
            
    def show_data(self):
        print(f"Name  : {self.first_name} {self.second_name} Age : {self.age()}") # method for get the data.

        
if __name__ == '__main__': # add __name__ variable so you can use this script a module without any bug.
    age=formula("Lim", "Boris", 1987)
    print(age.age())
    age.show_data()
