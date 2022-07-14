import logging as lg

lg.basicConfig(filename="logfile.log", level=lg.DEBUG, format='%(asctime)s : %(levelname)s : %(name)s : %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
lg.info("ENCAPSULATION")

class ineuron:
    try:
        def login(self):
            print("Welcome to Ineuron ")
        def signup(self):
            print("Sign up successful")
    except Exception as e:
        lg.exception(e)

    else:
        lg.info("All the list functions worked perfectly.")



class students(ineuron):
    def __init__(self, name, surname, y):
         self._a = name
         self.__s = surname
         self.y = 5

    try:
       def details(self):
          print("Name of student ",self._a)
          print("Surname of student ",self.__s)
       def no_of_courses(self):
           print("no of courses in which student enrol",self.y)
    except Exception as e:
        lg.exception(e)

    else:
        lg.info("All the list functions worked perfectly.")


class intership():
    def __init__(self):
        self.a = "ineuron"
        self.__b = "students"

class job(intership):
    def __init__(self):
        intership.__init__(self)
        print("calling")
        try:
            print(self.__b)
        except Exception as e:
            print(e)
        else:
            lg.info("All the list functions worked perfectly.")

o = intership()
print(o.a)
c = job()
print(c._intership__b)

i= students("vis", "kumar", 255)
i.details()

lg.info(i._a)
lg.info(i._students__s)
lg.info(i.y)

lg.info("METHOD OVERRIDING")

class ineuron:

    try:
        def student(self):
            print("detail of student")

        def hall0ffame(self):
            print("hall of fame")

        def nclass(self):
            print("class name")
    except Exception as e:
        lg.info(e)
    else:
        lg.info("All the list functions worked perfectly.")

class blog(ineuron):
        try:
            def student(self):
                print("these are students list")
        except Exception as e:
            lg.info(e)
        else:
            lg.info("All the list functions worked perfectly.")


class class_type(ineuron):
    try:
        def nclass(self):
            print("list of classes")

        def enroll(self):
            pass
    except Exception as e:
        lg.info(e)
    else:
        lg.info("All the list functions worked perfectly.")

class affiliats(class_type):
    try:
        def affil(self):
            pass
        def enroll(self):
            print("no of affiliates")

    except Exception as e:
        lg.info(e)
    else:
        lg.info("All the list functions worked perfectly.")

class no_of_courses(blog):
    try:
        def student(self):
            print("function of courses class")

    except Exception as e:
        lg.info(e)
    else:
        lg.info("All the list functions worked perfectly.")


i = no_of_courses()
i.student()
a = affiliats()
a.enroll()
b = class_type()
b.nclass()
c = blog()
c.student()


lg.info("POLYMORPHISM")

class ineuron:
    try:
        def login(self):
            print("Welcome to Ineuron ")
        def signup(self):
            print("Sign up successful")
        def details(self):
            print("all students details")

    except Exception as e:
        lg.exception(e)

    else:
        lg.info("All the list functions worked perfectly.")

class students:
    try:
       def details(self):
          print("Show students details ")
       def no_of_courses(self):
           print("no of courses in which student enrol")
    except Exception as e:
        lg.exception(e)

    else:
        lg.info("All the list functions worked perfectly.")

def iner_external(r):
    r.details()

i1 = ineuron()
i2 = students()
iner_external(i1)
iner_external(i2)

class ineuron:
    try:
        def login(self):
            print("Welcome to Ineuron ")
        def signup(self):
            print("Sign up successful")
        def details(self):
            print("all students details")

    except Exception as e:
        lg.exception(e)

    else:
        lg.info("All the list functions worked perfectly.")

class students:
    try:
       def details(self):
          print("Show students details ")
       def no_of_courses(self):
           print("no of courses in which student enrol")
    except Exception as e:
        lg.exception(e)

    else:
        lg.info("All the list functions worked perfectly.")
class intership(students):
    try:
        def intership(self):
           print("no of intership")
    except Exception as e:
        lg.exception(e)
    else:
        lg.info("All the list functions worked perfectly.")


class job(intership):
    try:
       def jobs(self):
           pass
    except Exception as e:
        lg.exception(e)
    else:
        lg.info("All the list functions worked perfectly.")


class classes(intership):
    try:
        def class_type(self):
            print("class type is full stack data science")

    except Exception as e:
        lg.info(e)
    lg.info("All the list functions worked perfectly.")

class blog(classes):
    try:
        def blogs(self):
            pass
    except Exception as e:
        lg.info(e)
    lg.info("All the list functions worked perfectly.")

class affiliates(students):
    try:
        def affiliates(self):
            pass
    except Exception as e:
        lg.info(e)
    lg.info("All the list functions worked perfectly.")

i = intership()
j = job()
bl = blog()
af = affiliates()
cl = classes()

i.details()
i.intership()

j.intership()
j.details()
j.jobs()

bl.details()
bl.class_type()

cl.no_of_courses()
cl.intership()