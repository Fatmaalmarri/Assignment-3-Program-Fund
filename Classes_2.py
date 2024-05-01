#File 2: Classes_2.py
#Importing Enum class from the enum python module
from enum import Enum

#Using an enumerator class for employees (sales, manager, salesperson, marketing manager, marketer, accountant, designer, handymen)
class Employees(Enum):
    Sales = "Sales"
    Managers = "Manager"
    Salespersons = "Salesperson"
    MarketingManagers = "Marketing Manager"
    Marketer = "Marketer"
    Accountant = "Accountant"
    Designers = "Designer"
    Handymen = "Handymen"

class Caterer:
    """Class to represent a caterer"""
    #Using initializing constructor to initialize attributes of Caterer class
    def __init__(self, caterer_id, caterer_name, caterer_address, caterer_contact, menu, min_guests, max_guests):
        #Initializing attributes
        self.__caterer_id = caterer_id
        self.__caterer_name = caterer_name
        self.__caterer_address = caterer_address
        self.__caterer_contact = caterer_contact
        self.__menu = menu
        self.__min_guests = min_guests
        self.__max_guests = max_guests

    #defining a function to change the menu
    def change_menu(self, new_menu):
        self.__menu = new_menu

    #Implementing setter and getter functions for Caterer class attributes
    def set_caterer_id(self, caterer_id):
        self.__caterer_id = caterer_id
    def get_caterer_id(self):
        return self.__caterer_id

    def set_caterer_name(self, caterer_name):
        self.__caterer_name = caterer_name
    def get_caterer_name(self):
        return self.__caterer_name

    def set_caterer_address(self, caterer_address):
        self.__caterer_address = caterer_address
    def get_caterer_address(self):
        return self.__caterer_address

    def set_caterer_contact(self, caterer_contact):
        self.__caterer_contact = caterer_contact
    def get_caterer_contact(self):
        return self.__caterer_contact

    def set_menu(self, menu):
        self.__menu = menu
    def get_menu(self):
        return self.__menu

    def set_min_guests(self, min_guests):
        self.__min_guests = min_guests
    def get_min_guests(self):
        return self.__min_guests

    def set_max_guests(self, max_guests):
        self.__max_guests = max_guests
    def get_max_guests(self):
        return self.__max_guests

    #Display Caterer Details
    def displayCaterer(self):
        print("Caterer Details:")
        print("ID: ", self.__caterer_id, " - Name:", self.__caterer_name)
        print("Address: ", self.__caterer_address, " - Contact Information:", self.__caterer_contact)
        print("Menu: ", self.__menu)
        print("Minimum number of guests: ", self.__min_guests)
        print("Maximum number of guests: ", self.__max_guests)


class Supplier:
    """Class to represent a Supplier"""
    #Using initializing constructor to initialize attributes of Supplier class
    def __init__(self, id, name, address, contact_details, service):
        #Initializing attributes
        self.__id = id
        self.__name = name
        self.__address = address
        self.__contact_details = contact_details
        self.__service = service

    # Implementing setter and getter functions for Supplier class attributes
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address
    def get_address(self):
        return self.__address

    def set_contact_details(self, contact_details):
        self.__contact_details = contact_details
    def get_contact_details(self):
        return self.__contact_details

    def set_service(self, service):
        self.__service = service
    def get_service(self):
        return self.__service

    #Display Supplier Details
    def displaySupplier(self):
        print("ID:", self.__id, " - Name:", self.__name)
        print("Address:", self.__address, " - Contact Details: ", self.__contact_details)
        print("Service: ", self.__service)

#Parent Class
class Employee:
    """Class to represent an Employee"""
    #Using initializing constructor to initialize attributes of Employee class
    def __init__(self, employee_name, employee_id, department, job_title, basic_salary, age, dateOfBirth, passport_details):
        #Initializing attributes
        self._employee_name = employee_name
        self._employee_id = employee_id
        self._department = department
        self._job_title = job_title
        self._basic_salary = basic_salary
        self._age = age
        self._dateOfBirth = dateOfBirth
        self._passport_details = passport_details

    #defining a function to update employee's salary
    def update_salary(self, new_salary):
        self._basic_salary = new_salary

    # Implementing setter and getter functions for Employee class attributes
    def set_employee_name(self, employee_name):
        self._employee_name = employee_name
    def get_employee_name(self):
        return self._employee_name

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id
    def get_employee_id(self):
        return self._employee_id

    def set_department(self, department):
        self._department = department
    def get_department(self):
        return self._department

    def set_job_title(self, job_title):
        self._job_title = job_title
    def get_job_title(self):
        return self._job_title

    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary
    def get_basic_salary(self):
        return self._basic_salary

    def set_age(self, age):
        self._age = age
    def get_age(self):
        return self._age

    def set_dateOfBirth(self, dateOfBirth):
        self._dateOfBirth = dateOfBirth
    def get_dateOfBirth(self):
        return self._dateOfBirth

    def set_passport_details(self, passport_details):
        self._passport_details = passport_details
    def get_passport_details(self):
        return self._passport_details

    #Display Employee Details
    def displayEmployee(self):
        print("Employee Information:")
        print("Name:", self._employee_name, " - ID:", self._employee_id)
        print("Department:", self._department, " - Job Title:", self._job_title)
        print("Basic Salary:", self._basic_salary)
        print("Age:", self._age, " - Date Of Birth:", self._dateOfBirth)
        print("Passport Details:", self._passport_details)

#Child class
class Designer(Employee):
    """Class to represent a designer as a child of Employee class"""
    #Using constructor to initialize attributes of Designer class
    def __init__(self, employee_name, employee_id, department, job_title, basic_salary, age, dateOfBirth, passport_details , design_specialization, qualifications):
        # Calling the constructor of the parent class
        Employee.__init__ (self, employee_name, employee_id, department, job_title, basic_salary, age, dateOfBirth, passport_details)
        #Initializing attributes
        self.__design_specialization = design_specialization
        self.__qualifications = qualifications

    # Implementing setter and getter functions for Employee class attributes
    def set_design_specialization(self, design_specialization):
        self.__design_specialization = design_specialization
    def get_design_specialization(self):
        return self.__design_specialization

    def set_qualifications(self, qualifications):
        self.__qualifications = qualifications
    def get_qualifications(self):
        return self.__qualifications

    #Display Designer Class
    def displayDesigner(self):
        print("Designer:")
        Employee.displayEmployee(self)
        print("Design Specialization:", self.__design_specialization)
        print("Qualifications:", self.__qualifications)

class Manager(Employee):
    """Class to represent a Manager as a child of Employee class"""
    #Using constructor to initialize attributes of Manager class
    def __init__(self, employee_name, employee_id, department, job_title, basic_salary, age, dateOfBirth, passport_details):
        # Calling the constructor of the parent class
        Employee.__init__(self, employee_name, employee_id, department, job_title, basic_salary, age, dateOfBirth, passport_details)
        #creating a list to manage employees
        self._employees_managed = []

    #defining a function to add employees into the managed list
    def add_employee(self, employee):
        self._employees_managed.append(employee)

    #Display Manager's Managed Employees
    def displayManagedEmployees(self):
        print(self._employee_name, "Manages:")
        for employee in self._employees_managed:
            print("-", employee.get_employee_name())
