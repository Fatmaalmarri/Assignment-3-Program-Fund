#File 4: Pickle.py
#importing pickle module
import pickle

class ManageEvents:
    """Class to represent event manager"""
    def __init__(self):
        #creating empty lists for events, clients, guests, venues, caterers, suppliers, employees, manager, designers
        self.events = []
        self.clients = []
        self.guests = []
        self.venues = []
        self.caterers = []
        self.suppliers = []
        self.employees = []
        self.managers = []
        self.designers = []

    #define a function to add an event
    def add_event(self, event):
        #append event to events list
        self.events.append(event)

    #define a function to add a client
    def add_client(self, client):
        #append client to clients list
        self.clients.append(client)

    #define a function to add a guest
    def add_guest(self, guest):
        #append guest to guests list
        self.guests.append(guest)

    #define a function to add a venue
    def add_venue(self, venue):
        #append venue to venues list
        self.venues.append(venue)

    #define a function to add a caterer
    def add_caterer(self, caterer):
        #append caterer to caterers list
        self.caterers.append(caterer)

    #define a function to add a supplier
    def add_supplier(self, supplier):
        #append caterer to suppliers list
        self.suppliers.append(supplier)

    #define a function to add an employee
    def add_employee(self, employee):
        #append empployee to employees list
        self.employees.append(employee)

    #define a function to add a manager
    def add_manager(self, manager):
        #append manager to managers list
        self.managers.append(manager)

    #define a function to add a designer
    def add_designer(self, designer):
        #append designer to designers list
        self.designers.append(designer)


    #define a function to save the data
    def save_data(self):
        #save self.events list to a file named 'events.pkl' in binary format using pickle.dump()
        with open('events.pkl', 'wb') as file:
            pickle.dump(self.events, file)

        #save self.clients list to a file named clients.pkl in binary format using pickle.dump()
        with open('clients.pkl', 'wb') as file:
            pickle.dump(self.clients, file)

        #save self.guests list to a file named 'guests.pkl' in binary format using pickle.dump()
        with open('guests.pkl', 'wb') as file:
            pickle.dump(self.guests, file)

        #save self.venues list to a file named 'venues.pkl' in binary format using pickle.dump()
        with open('venues.pkl', 'wb') as file:
            pickle.dump(self.venues, file)

        #save self.caterers list to a file named 'caterers.pkl' in binary format using pickle.dump()
        with open('caterers.pkl', 'wb') as file:
            pickle.dump(self.caterers, file)

        #save self.suppliers list to a file named 'suppliers.pkl' in binary format using pickle.dump()
        with open('suppliers.pkl', 'wb') as file:
            pickle.dump(self.suppliers, file)

        #save self.employees list to a file named 'employees.pkl' in binary format using pickle.dump()
        with open('employees.pkl', 'wb') as file:
            pickle.dump(self.employees, file)

        #save self.managers list to a file named 'managers.pkl' in binary format using pickle.dump()
        with open('managers.pkl', 'wb') as file:
            pickle.dump(self.managers, file)

        #save self.designers list to a file named 'designers.pkl' in binary format using pickle.dump()
        with open('designers.pkl', 'wb') as file:
            pickle.dump(self.designers, file)

    #define a function to load the data
    def load_data(self):
        #loads the 'events.pkl' file using the pickle.load() function
        with open('events.pkl', 'rb') as file:
            #then assigns it to the self.events list
            self.events = pickle.load(file)

        #loads the 'clients.pkl' file using the pickle.load() function
        with open('clients.pkl', 'rb') as file:
            # then assigns it to the self.clients list
            self.clients = pickle.load(file)

        #loads the 'guests.pkl' file using the pickle.load() function
        with open('guests.pkl', 'rb') as file:
            # then assigns it to the self.guests list
            self.guests = pickle.load(file)

        #loads the 'venues.pkl' file using the pickle.load() function
        with open('venues.pkl', 'rb') as file:
            # then assigns it to the self.venues list
            self.venues = pickle.load(file)

        #loads the 'caterers.pkl' file using the pickle.load() function
        with open('caterers.pkl', 'rb') as file:
            # then assigns it to the self.caterers list
            self.caterers = pickle.load(file)

        #loads the 'suppliers.pkl' file using the pickle.load() function
        with open('suppliers.pkl', 'rb') as file:
            # then assigns it to the self.suppliers list
            self.suppliers = pickle.load(file)

        #loads the 'employees.pkl' file using the pickle.load() function
        with open('employees.pkl', 'rb') as file:
            # then assigns it to the self.employees list
            self.employees = pickle.load(file)

        #loads the 'managers.pkl' file using the pickle.load() function
        with open('managers.pkl', 'rb') as file:
            # then assigns it to the self.managers list
            self.managers = pickle.load(file)

        #loads the 'designers.pkl' file using the pickle.load() function
        with open('designers.pkl', 'rb') as file:
            # then assigns it to the self.designers list
            self.designers = pickle.load(file)
