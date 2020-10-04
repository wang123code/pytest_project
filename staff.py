class Staff:
    def __init__(self,name,age):
        self.name = name
        self.age = age


staff = Staff("1101212",16)
print(hasattr(staff,'name'))
print(hasattr(staff,'age'))
print(hasattr(staff,'sex'))



