#File 5: Test_Cases.py

#importing the classes from the file Classes_1.py, Classes_2.py, and Pickle.py
from Classes_1 import Event, Client, Guest, Venue, EventType
from Classes_2 import Caterer, Supplier, Employee, Manager, Designer, Employees
from Pickle import ManageEvents

#Exception handling for creating objects
try:
    #Creating Objects
    #Creating event1 as an object for Event class
    event1 = Event("Graduation Party", "E3692", EventType.Graduation, "Star Theme", "11/05/2024", "16:00", "3 hours", "Park Hyatt Dubai Venue", "A5976", [], "Graduation Catering", "G EVENT Cleaning", "ABC Decorations", "Entertainment Corp.", "Furniture Supply Corp.", 1000.0, None)
    #Creating client1 as an object for Client class
    client1 = Client("A5976", "Maryam", "Jumeira", "Maryam@gmail.com", 2500.0)

    #Creating guest1 and guest2 as objects for Guest class
    guest1 = Guest("C4361", "Aisha", "Umm Suqueim", "aisha@gmail.com")
    guest2 = Guest("D9024", "Shamma", "Nad Al Sheba", "Shamma@gmail.com")

    #Creating venue1 as an object for Venue class
    venue1 = Venue("M6752", "Park Hyatt", "Dubai Creek Club St.", "parkhyatt@gmail.com", 45, 350)
    #Creating caterer1 as an object for Caterer class
    caterer1 = Caterer("X3221", "Graduation Catering", "Sheikh Zayed Road", "grad.catering@gmail.com", "Dessert: Chocolate cake, Drinks: Lemonade", 20, 300)
    #Creating supplier1 as an object for Supplier class
    supplier1 = Supplier("A8875", "ABY Supplying ", "Al Wasl Road", "ABY.supplying@gmail.com", "Cleaning")

    #Creating employee1 and employee2 as objects for Employee class
    employee1 = Employee("Salma J Sam", "98637", Employees.Sales.value, "Salesperson", 20000.0, 30, "01/03/1994", "G9395")
    employee2 = Employee("Mariam Khalid", "98394", Employees.Sales.value, "Salesperson", 20000.0, 25, "02/01/1999", "G9395")

    #Creating manager1 as an object for Manager class
    manager1 = Manager("Susan Meyers", "47899", Employees.Sales.value, "Manager", 37500.00, 42, "03/05/1982", "H1256")
    #Creating designer1 as an object for Designer class
    designer1 = Designer("Fatma", "D8754", Employees.Designers.value, "Designer", 30000.00, 24, "06/02/2000", "W2391", "Graphic Design", "Bachelor's Degree")

    #Creating an instance of ManageEvents class
    event_manager = ManageEvents()

    #Adding instances to ManageEvents class
    event_manager.add_event(event1)
    event_manager.add_client(client1)
    event_manager.add_guest(guest1)
    event_manager.add_venue(venue1)
    event_manager.add_caterer(caterer1)
    event_manager.add_supplier(supplier1)
    event_manager.add_employee(employee1)
    event_manager.add_manager(manager1)
    event_manager.add_designer(designer1)

    print(" ")
    event1.assign_venue(venue1)
    event1.add_guest(guest1)
    event1.add_guest(guest2)
    event1.remove_guest(guest1)
    event1.displayEvent()

    print(" ")
    client1.add_event(event1)
    client1.displayClient()

    print(" ")
    guest2.displayGuest()

    print(" ")
    venue1.modify_capacity(400)
    venue1.displayVenue()

    print(" ")
    caterer1.change_menu("Dessert: Vanilla Cake, Drinks: Orange Juice")
    caterer1.displayCaterer()

    print(" ")
    supplier1.displaySupplier()

    print(" ")
    employee1.update_salary(22000.0)
    employee1.displayEmployee()
    employee2.displayEmployee()

    print(" ")
    designer1.displayDesigner()

    print(" ")
    manager1.add_employee(employee1)
    manager1.add_employee(employee2)
    manager1.displayManagedEmployees()

except ValueError as ve:
    print("ValueError occurred:", ve)
    # Handle ValueError
except ImportError as ie:
    print("ImportError occurred:", ie)
    # Handle ImportError
except Exception as e:
    print("An error occurred during object creation:", str(e))

# Exception handling for saving data
try:
    event_manager.save_data()
except Exception as e:
    print("An error occurred while saving data:", str(e))

# Exception handling for loading data
try:
    event_manager.load_data()
except FileNotFoundError:
    print("No existing data file found.")
except Exception as e:
    print("An error occurred while loading data:", str(e))
