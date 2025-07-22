class person:
    def __init__(self,name=None,age=None,gender=None):
        if isinstance(name,person):
            self.name=name.name
            self.age=name.age
            self.gender=name.gender
        else:
            self.name=name
            self.age=age
            self.gender=gender
    def show_person_info(self):
        print(f"name:{self.name},age:{self.age},gender:{self.gender}")
        
        
            
class acadimicinfo(person):
    def __init__(self,name=None,age=None,gender=None,grades=None):
        super().__init__(name,age,gender)
        if isinstance(name,acadimicinfo):
            self.grades=name.grades
        else:
            self.grades=grades
    def total_marks(self):
        
        try:
            total= sum(self.grades.values())
            avg = total / len(self.grades)
            if avg > 68:
                print("Passed")
                
            else:
                print("Failed")
        
        except Exception as e:
            print(e)
            
                
class contact_info(person):
    def __init__(self,name=None,age=None,gender=None,email=None,phone=None,hobbies=None):
        super().__init__(name,age,gender)
        if isinstance(name,contact_info):
            self.email=name.email
            self.phone=name.phone
            self.hobbies=name.hobbies
        else:
            self.email=email
            self.phone=phone
            self.hobbies=hobbies
    def show_contact_info(self):
        print(f"email:{self.email},phone:{self.phone}")
        print("hobbies:",self.hobbies)
        
        
        
class student_info(acadimicinfo,contact_info):
    def __init__(self,name=None,age=None,gender=None,grades=None,email=None,phone=None,hobbies=None):
        if isinstance(name,student_info):
            acadimicinfo.__init__(self, name.name, name.age, name.gender, name.grades)
            contact_info.__init__(self, name.name, name.age, name.gender, name.email, name.phone, name.hobbies)
        else:
            acadimicinfo.__init__(self, name, age, gender, grades)
            contact_info.__init__(self, name, age, gender, email, phone, hobbies)

    def show_result(self):
        self.total_marks()
        self.show_person_info()
        self.show_contact_info()
            
            
grades={'ss':90,'NT':80,'CS':95,'DLD':85,'EMF':90}
email="vijay651@gmail.com"
 
obj1 = student_info("vijaya", "20", "Female", grades, email, "9642523210", "readingbooks")
obj2=student_info(obj1)
obj2.show_result()














            
        
        
        
        

        
        
            
            
        
        
        
        
        
        
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


    
