class fullname:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def name1(self):
        dd = f"hello {self.first}"
        return dd

    def name2(self):
        ss = f"your last name is {self.last}"
        return ss


person = fullname(input("enter first name: "),input("enter last name: "))
print(person.name1().title())
print(person.name2().title())
