import logging as lg

lg.basicConfig(filename="logfile.log", level=lg.DEBUG, format='%(asctime)s : %(levelname)s : %(name)s : %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
lg.info("MULTI LEVEL INHERITANCE")
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

class blog(job):
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

i= job()
a = classes()
b = blog()
c = affiliates()
i.login()
i.intership()
i.signup()
i.jobs()
i.details()
i.no_of_courses()
a.login()
a.signup()
a.details()
a.class_type()
b.signup()
b.jobs()
b.no_of_courses()
b.blogs()
c.no_of_courses()
c.affiliates()


lg.info("MULTIPLE INHERITANCE")
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


class intership:
    try:
        def intership(self):
           print("no of intership")
    except Exception as e:
        lg.exception(e)
    else:
        lg.info("All the list functions worked perfectly.")


class job(ineuron,students,intership):
    try:
       def jobs(self):
           pass
    except Exception as e:
        lg.exception(e)
    else:
        lg.info("All the list functions worked perfectly.")

class classes(ineuron,students,intership):
    try:
       def class_type(self):
           print("class type is full stack data science")

    except Exception as e:
        lg.info(e)
    lg.info("All the list functions worked perfectly.")


class blog(ineuron,students):
    try:
        def blogs(self):
            pass
    except Exception as e:
        lg.info(e)
    lg.info("All the list functions worked perfectly.")

class affiliates(ineuron,students):
    try:
        def affiliates(self):
            pass
    except Exception as e:
        lg.info(e)
    lg.info("All the list functions worked perfectly.")

i = job()
i.login()
i.intership()
i.signup()
i.jobs()
i.details()
i.no_of_courses()

a = classes()
a.signup()
a.details()
a.class_type()
a.intership()

b = blog()
b.blogs()
b.no_of_courses()
b.details()

c = affiliates()
c.affiliates()
c.login()
