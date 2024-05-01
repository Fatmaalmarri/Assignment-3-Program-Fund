#File 3: GUI.py

#importing the classes from the file Classes_1.py, Classes_2.py
from Classes_1 import Event, Client, Guest, Venue
from Classes_2 import Employee, Supplier
#importing tkinter
import tkinter as tk
from tkinter import messagebox

class GUI:
    """Class to represent a GUI"""
    def __init__(self):
        self.root = tk.Tk() #create a main window
        self.root.geometry("650x250") #set the size of the window
        self.root.title("Best Events Company Management") #set the title of the window

        #create an empty list to store employee details
        self.employees_list = []
        #create a label widget for Employee ID
        self.employee_label = tk.Label(self.root, text="Employee ID:")
        #using grid to place the label widget in the window
        self.employee_label.grid(column=0, row=0, padx=5, pady=5)

        #create an entry widget for entering the employee ID
        self.employeeId_entry = tk.Entry(self.root)
        #using grid to place the widget in the window
        self.employeeId_entry.grid(column=1, row=0, padx=5, pady=5)

        #create a button to add an employee
        self.employee_add_button = tk.Button(self.root, text="Add", command=self.add_employee)
        #using grid to place the widget in the window
        self.employee_add_button.grid(column=2, row=0, padx=5, pady=5)

        #create a button to delete an employee
        self.employee_delete_button = tk.Button(self.root, text="Delete", command=self.delete_employee)
        #using grid to place the widget in the window
        self.employee_delete_button.grid(column=3, row=0, padx=5, pady=5)

        #create a button to modify an employee
        self.employee_modify_button = tk.Button(self.root, text="Modify", command=self.modify_employee)
        #using grid to place the widget in the window
        self.employee_modify_button.grid(column=4, row=0, padx=5, pady=5)

        #create a button to display an employee
        self.employee_display_button = tk.Button(self.root, text="Display", command=self.display_employee)
        #using grid to place the widget in the window
        self.employee_display_button.grid(column=5, row=0, padx=5, pady=5)

        #create an empty list to store event details
        self.event_list = []
        #create a label widget for Event ID
        self.event_label = tk.Label(self.root, text="Event ID:")
        #using grid to place the label widget in the window
        self.event_label.grid(column=0, row=1, padx=5, pady=5)

        #create an entry widget for entering the event ID
        self.eventId_entry = tk.Entry(self.root)
        #using grid to place the label widget in the window
        self.eventId_entry.grid(column=1, row=1, padx=5, pady=5)

        #create a button to add an event
        self.event_add_button = tk.Button(self.root, text="Add", command=self.add_event)
        #using grid to place the widget in the window
        self.event_add_button.grid(column=2, row=1, padx=5, pady=5)

        #create a button to delete an event
        self.event_delete_button = tk.Button(self.root, text="Delete", command=self.delete_event)
        #using grid to place the widget in the window
        self.event_delete_button.grid(column=3, row=1, padx=5, pady=5)

        #create a button to modify an event
        self.event_modify_button = tk.Button(self.root, text="Modify", command=self.modify_event)
        #using grid to place the widget in the window
        self.event_modify_button.grid(column=4, row=1, padx=5, pady=5)

        #create a button to display an event
        self.event_display_button = tk.Button(self.root, text="Display", command=self.display_event)
        #using grid to place the widget in the window
        self.event_display_button.grid(column=5, row=1, padx=5, pady=5)

        # create an empty list to store client details
        self.client_list = []
        # create a label widget for Client ID
        self.client_label = tk.Label(self.root, text="Client ID:")
        # using grid to place the label widget in the window
        self.client_label.grid(column=0, row=2, padx=5, pady=5)

        # create an entry widget for entering the Client ID
        self.clientId_entry = tk.Entry(self.root)
        # using grid to place the label widget in the window
        self.clientId_entry.grid(column=1, row=2, padx=5, pady=5)

        # create a button to add a client
        self.client_add_button = tk.Button(self.root, text="Add", command=self.add_client)
        # using grid to place the widget in the window
        self.client_add_button.grid(column=2, row=2, padx=5, pady=5)

        # create a button to delete a client
        self.client_delete_button = tk.Button(self.root, text="Delete", command=self.delete_client)
        # using grid to place the widget in the window
        self.client_delete_button.grid(column=3, row=2, padx=5, pady=5)

        # create a button to modify a client
        self.client_modify_button = tk.Button(self.root, text="Modify", command=self.modify_client)
        # using grid to place the widget in the window
        self.client_modify_button.grid(column=4, row=2, padx=5, pady=5)

        # create a button to display a client
        self.client_display_button = tk.Button(self.root, text="Display", command=self.display_client)
        # using grid to place the widget in the window
        self.client_display_button.grid(column=5, row=2, padx=5, pady=5)

        # create an empty list to store supplier details
        self.supplier_list = []
        # create a label widget for Supplier ID
        self.supplier_label = tk.Label(self.root, text="Supplier ID:")
        # using grid to place the label widget in the window
        self.supplier_label.grid(column=0, row=3, padx=5, pady=5)

        # create an entry widget for entering the supplier ID
        self.supplierId_entry = tk.Entry(self.root)
        # using grid to place the label widget in the window
        self.supplierId_entry.grid(column=1, row=3, padx=5, pady=5)

        # create a button to add a supplier
        self.supplier_add_button = tk.Button(self.root, text="Add", command=self.add_supplier)
        # using grid to place the widget in the window
        self.supplier_add_button.grid(column=2, row=3, padx=5, pady=5)

        # create a button to delete a supplier
        self.supplier_delete_button = tk.Button(self.root, text="Delete", command=self.delete_supplier)
        # using grid to place the widget in the window
        self.supplier_delete_button.grid(column=3, row=3, padx=5, pady=5)

        # create a button to modify a supplier
        self.supplier_modify_button = tk.Button(self.root, text="Modify", command=self.modify_supplier)
        # using grid to place the widget in the window
        self.supplier_modify_button.grid(column=4, row=3, padx=5, pady=5)

        # create a button to display a supplier
        self.supplier_display_button = tk.Button(self.root, text="Display", command=self.display_supplier)
        # using grid to place the widget in the window
        self.supplier_display_button.grid(column=5, row=3, padx=5, pady=5)

        # create an empty list to store guest details
        self.guest_list = []
        # create a label widget for Guest ID
        self.guest_label = tk.Label(self.root, text="Guest ID:")
        # using grid to place the label widget in the window
        self.guest_label.grid(column=0, row=4, padx=5, pady=5)

        # create an entry widget for entering the guest ID
        self.guestId_entry = tk.Entry(self.root)
        # using grid to place the label widget in the window
        self.guestId_entry.grid(column=1, row=4, padx=5, pady=5)

        # create a button to add a guest
        self.guest_add_button = tk.Button(self.root, text="Add", command=self.add_guest)
        # using grid to place the widget in the window
        self.guest_add_button.grid(column=2, row=4, padx=5, pady=5)

        # create a button to delete a guest
        self.guest_delete_button = tk.Button(self.root, text="Delete", command=self.delete_guest)
        # using grid to place the widget in the window
        self.guest_delete_button.grid(column=3, row=4, padx=5, pady=5)

        # create a button to modify a guest
        self.guest_modify_button = tk.Button(self.root, text="Modify", command=self.modify_guest)
        # using grid to place the widget in the window
        self.guest_modify_button.grid(column=4, row=4, padx=5, pady=5)

        # create a button to display a guest
        self.guest_display_button = tk.Button(self.root, text="Display", command=self.display_guest)
        # using grid to place the widget in the window
        self.guest_display_button.grid(column=5, row=4, padx=5, pady=5)

        # create an empty list to store venue details
        self.venue_list = []
        # create a label widget for Venue ID
        self.venue_label = tk.Label(self.root, text="Venue ID:")
        # using grid to place the label widget in the window
        self.venue_label.grid(column=0, row=5, padx=5, pady=5)

        # create an entry widget for entering the venue ID
        self.venueId_entry = tk.Entry(self.root)
        # using grid to place the label widget in the window
        self.venueId_entry.grid(column=1, row=5, padx=5, pady=5)

        # create a button to add a venue
        self.venue_add_button = tk.Button(self.root, text="Add", command=self.add_venue)
        # using grid to place the widget in the window
        self.venue_add_button.grid(column=2, row=5, padx=5, pady=5)

        # create a button to delete a venue
        self.venue_delete_button = tk.Button(self.root, text="Delete", command=self.delete_venue)
        # using grid to place the widget in the window
        self.venue_delete_button.grid(column=3, row=5, padx=5, pady=5)

        # create a button to modify a venue
        self.venue_modify_button = tk.Button(self.root, text="Modify", command=self.modify_venue)
        # using grid to place the widget in the window
        self.venue_modify_button.grid(column=4, row=5, padx=5, pady=5)

        # create a button to display a venue
        self.venue_display_button = tk.Button(self.root, text="Display", command=self.display_venue)
        # using grid to place the widget in the window
        self.venue_display_button.grid(column=5, row=5, padx=5, pady=5)

        #Start/Enter the main loop
        self.root.mainloop()

    def add_employee(self):   #defining a function to add an employee
        employee_id = self.employeeId_entry.get()  #get employee ID from entry widget
        if employee_id: #if employee id is given
            #prompt user to input employee name, department, job title, salary, age, birth date, and passport details
            name = input("Enter employee name: ")
            department = input("Enter department: ")
            job_title = input("Enter employee job title: ")
            basic_salary = input("Enter employee's basic salary: ")
            age = input("Enter employee's age: ")
            dateOfBirth = input("Enter date of birth: ")
            passport_details = input("Enter passport details: ")
            #create a new Employee object with the provided details
            new_employee = Employee(name, employee_id, department, job_title, basic_salary, age, dateOfBirth, passport_details)

            self.employees_list.append(new_employee)  #append the new employee to employees list
            self.employeeId_entry.delete(0, tk.END)  #clear the entry widget
            #show message of success
            messagebox.showinfo("Success", f"Employee with ID {employee_id} added")
        else:  #otherwise, show error message
            messagebox.showerror("Error", "Please enter an employee ID")

    def delete_employee(self):  #defining a function to delete an employee
        employee_id = self.employeeId_entry.get() #get employee ID from entry widget
        if employee_id:  #if employee id is given
            found = False
            #use for loop to iterate through employees list to find the employee with the given ID
            for employee in self.employees_list:
                if employee.get_employee_id() == employee_id:  #if the ID's are equal
                    self.employees_list.remove(employee) #remove the employee from the list
                    found = True #set found to True and break
                    break
            if found: #if found show message of success
                messagebox.showinfo("Success", f"Employee deleted: ID - {employee_id}")
            else:  #if employee with the given ID is not found, show error message
                messagebox.showerror("Error", f"Employee with ID {employee_id} not found")
            self.employeeId_entry.delete(0, tk.END)   #clear the entry widget
        else: #otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter an employee ID")

    def modify_employee(self):  #defining a function to modify employee details
        employee_id = self.employeeId_entry.get()  #get employee ID from entry widget
        new_name = input("Enter new name: ") #let user enter new name
        if employee_id:  #if employee id is given
            found = False
            #use for loop to iterate through employees list to find the employee with the given ID
            for employee in self.employees_list:
                #if the ID's are equal, update the employee name with the new name
                if employee.get_employee_id() == employee_id:
                    employee.set_employee_name(new_name)
                    found = True  #set found to True and break
                    break
            if found:  #if found show message of success
                messagebox.showinfo("Success", f"Employee modified: ID - {employee_id}, New Name - {new_name}")
            else:        #if employee with the given ID is not found, show error message
                messagebox.showerror("Error", f"Employee with ID {employee_id} not found")
            self.employeeId_entry.delete(0, tk.END)  #clear the entry widget
        else:  #otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter an employee ID")

    def display_employee(self):  #defining a function to display employee's details
        employee_id = self.employeeId_entry.get()  #get employee ID from entry widget
        if employee_id: #if employee id is given
            found = False
            #use for loop to iterate through employees list to find the employee with the given ID
            for employee in self.employees_list:
                #if the ID's are equal, print the details
                if employee.get_employee_id() == employee_id:
                    details = (
                        f"ID: {employee.get_employee_id()}\n"
                        f"Name: {employee.get_employee_name()}\n"
                        f"Department: {employee.get_department()}\n"
                        f"Job Title: {employee.get_job_title()}\n"
                        f"Basic Salary: {employee.get_basic_salary()}\n"
                        f"Age: {employee.get_age()}\n"
                        f"Date Of Birth: {employee.get_dateOfBirth()}\n"
                        f"Passport Details: {employee.get_passport_details()}"
                    )
                    messagebox.showinfo("Employee Details:", details)
                    found = True #set found to True and break
                    break
            if not found:      #if employee with the given ID is not found, show error message
                messagebox.showerror("Error", f"Employee with ID {employee_id} not found")
            self.employeeId_entry.delete(0, tk.END) #clear the entry widget
        else:      #otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter an employee ID")

    def add_event(self):  #defining a function to add an event
        event_id = self.eventId_entry.get()  #get event ID from entry widget
        if event_id:  #if event ID is given
            #prompt user to input event details
            event = input("Enter event name: ")
            event_type = input("Enter event type: ")
            theme = input("Enter theme: ")
            date = input("Enter event's date: ")
            time = input("Enter event's time: ")
            duration = input("Enter event's duration: ")
            venue_address = input("Enter venue address: ")
            client_id = input("Enter client ID: ")
            guest_list = input("Enter guest list:")
            catering_comp = input("Enter catering company: ")
            cleaning_comp = input("Enter cleaning company: ")
            decorations_comp = input("Enter decorations company: ")
            entertainment_comp = input("Enter entertainment company: ")
            furniture_comp = input("Enter furniture supply company: ")
            invoice = input("Enter invoice: ")
            venue = input("Enter venue: ")
            #create a new Event object with the provided details
            new_event = Event(event, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_comp, cleaning_comp, decorations_comp, entertainment_comp, furniture_comp, invoice, venue)

            self.event_list.append(new_event)  #append the new event to event list
            self.eventId_entry.delete(0, tk.END)  #clear the entry widget
            #show message of success
            messagebox.showinfo("Success", f"Event with ID {event_id} added")
        else:   #otherwise, show error message
            messagebox.showerror("Error", "Please enter an event ID")

    def delete_event(self):  #defining a function to delete an event
        event_id = self.eventId_entry.get()  #get event ID from entry widget
        if event_id:  # if event ID is given
            found = False
            #use for loop to iterate through events list to find the event with the given ID
            for event in self.event_list:
                if event.get_event_id() == event_id:   # if the ID's are equal
                    self.event_list.remove(event)  #remove event from the list
                    found = True  #set found to True and break
                    break
            if found:         #if found show message of success
                messagebox.showinfo("Success", f"Event deleted: ID - {event_id}")
            else:      #if event with the given ID is not found, show error message
                messagebox.showerror("Error", f"Event with ID {event_id} not found")
            self.eventId_entry.delete(0, tk.END) #clear the entry widget
        else:    #otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter an event ID")

    def modify_event(self):   #defining a function to modify event details
        event_id = self.eventId_entry.get()  #get event ID from entry widget
        new_theme = input("Enter new theme: ") # let user enter new theme
        if event_id:   #if event id is given
            found = False
            #use for loop to iterate through events list to find the event with the given ID
            for event in self.event_list:
                #if the ID's are equal, update the event theme with the new theme
                if event.get_event_id() == event_id:
                    event.set_theme(new_theme)
                    found = True #set found to True and break
                    break
            if found:      #if found show message of success
                messagebox.showinfo("Success", f"Event modified: ID - {event_id}, New Name - {new_theme}")
            else:       #if event with the given ID is not found, show error message
                messagebox.showerror("Error", f"Event with ID {event_id} not found")
            self.eventId_entry.delete(0, tk.END)   #clear the entry widget
        else:   #otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter an event ID")

    def display_event(self):  #defining a function to display event details
        event_id = self.eventId_entry.get() #get event ID from entry widget
        if event_id:  #if event id is given
            found = False
            #use for loop to iterate through events list to find the event with the given ID
            for event in self.event_list:
                #if the ID's are equal, print the details
                if event.get_event_id() == event_id:
                    details = (
                        f"ID: {event.get_event_id()}\n"
                        f"Event: {event.get_event()}\n"
                        f"Event Type: {event.get_event_type()}\n"
                        f"Theme: {event.get_theme()}\n"
                        f"Date: {event.get_date()}\n"
                        f"Time: {event.get_time()}\n"
                        f"Duration: {event.get_duration()}\n"
                        f"Venue Address: {event.get_venue_address()}\n"
                        f"Client ID: {event.get_client_id()}\n"
                        f"Guest List:  {event.get_guest_list()}\n"
                        f"Catering Company: {event.get_catering_comp()}\n"
                        f"Cleaning Company: {event.get_cleaning_comp()}\n"
                        f"Decorations Company: {event.get_decorations_comp()}\n"
                        f"Entertainment Company: {event.get_entertainment_comp()}\n"
                        f"Furniture Supply Company: {event.get_furniture_comp()}\n"
                        f"Invoice: {event.get_invoice()}\n"
                        f"Venue: {event.get_venue()}"
                    )
                    messagebox.showinfo("Event Details:", details)
                    found = True #set found to True and break
                    break
            if not found:    #if event with the given ID is not found, show error message
                messagebox.showerror("Error", f"Event with ID {event_id} not found")
            self.eventId_entry.delete(0, tk.END)  #clear the entry widget
        else:  #otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter an event ID")

    def add_client(self):   #defining a function to add a client
        client_id = self.clientId_entry.get()  #get client ID from entry widget
        if client_id:   #if client ID is given
            #prompt user to input client name, address, contact details, and budget
            name = input("Enter client name: ")
            address = input("Enter address: ")
            contact_details = input("Enter client's contact details: ")
            budget = input("Enter budget: ")
            #create a new Client object with the provided details
            new_client = Client(client_id, name, address, contact_details, budget)

            self.client_list.append(new_client)  #append the new client to client list
            self.clientId_entry.delete(0, tk.END)   #clear the entry widget
            #show message of success
            messagebox.showinfo("Success", f"Client with ID {client_id} added")
        else:   #otherwise, show error message
            messagebox.showerror("Error", "Please enter a client ID")

    def delete_client(self):  #defining a function to delete a client
        client_id = self.clientId_entry.get()    #get client ID from entry widget
        if client_id:   #if client ID is given
            found = False
            #use for loop to iterate through client list to find the client with the given ID
            for client in self.client_list:
                if client.get_id() == client_id:  #if the IDs are equal
                    self.client_list.remove(client)   #remove the client from the list
                    found = True   #set found to True and break
                    break
            if found:  #if found show message of success
                messagebox.showinfo("Success", f"Client deleted: ID - {client_id}")
            else:      #if client with the given ID is not found, show error message
                messagebox.showerror("Error", f"Client with ID {client_id} not found")
            self.clientId_entry.delete(0, tk.END) #clear the entry widget
        else:    #otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter a client ID")

    def modify_client(self):    #defining a function to modify a client
        client_id = self.clientId_entry.get()   #get client ID from entry widget
        new_budget = input("Enter new budget: ")  # let user enter new budget
        if client_id:   # if client ID is given
            found = False
            # use for loop to iterate through client list to find the client with the given ID
            for client in self.client_list:
                # if the IDs are equal, update the client budget with the new budget
                if client.get_id() == client_id:
                    client.set_budget(new_budget)
                    found = True #set found to True and break
                    break
            if found:     #if found show message of success
                messagebox.showinfo("Success", f"Client modified: ID - {client_id}, New Budget - {new_budget}")
            else:     # if client with the given ID is not found, show error message
                messagebox.showerror("Error", f"Client with ID {client_id} not found")
            self.clientId_entry.delete(0, tk.END) #clear the entry widget
        else:   # otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter a client ID")

    def display_client(self): #defining a function to display client
        client_id = self.clientId_entry.get()   # get client ID from entry widget
        if client_id: # if client ID is given
            found = False
            # use for loop to iterate through client list to find the client with the given ID
            for client in self.client_list:
                if client.get_id() == client_id:  # if the IDs are equal, print the details
                    details = (
                        f"ID: {client.get_id()}\n"
                        f"Name: {client.get_name()}\n"
                        f"Address: {client.get_address()}\n"
                        f"Contact Details: {client.get_contact_details()}\n"
                        f"Budget: {client.get_budget()}"
                    )
                    messagebox.showinfo("Client Details:", details)
                    found = True #set found to True and break
                    break
            if not found:    # if client with the given ID is not found, show error message
                messagebox.showerror("Error", f"Client with ID {client_id} not found")
            self.clientId_entry.delete(0, tk.END)  # clear the entry widget
        else:   # otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter a client ID")

    def add_supplier(self):  #defining a function to add supplier
        supplier_id = self.supplierId_entry.get()  # get supplier ID from entry widget
        if supplier_id:    # if supplier ID is given
            # prompt user to input supplier name, address, contact details, and service
            name = input("Enter supplier name: ")
            address = input("Enter address: ")
            contact_details = input("Enter contact details: ")
            service = input("Enter supplier's service: ")
            #create a new Supplier object with the provided details
            new_supplier = Supplier(supplier_id, name, address, contact_details, service)

            self.supplier_list.append(new_supplier)   #append the new supplier to supplier list
            self.supplierId_entry.delete(0, tk.END)   #clear the entry widget
            #show message of success
            messagebox.showinfo("Success", f"Supplier with ID {supplier_id} added")
        else:   # otherwise, show error message
            messagebox.showerror("Error", "Please enter a supplier ID")

    def delete_supplier(self):  #defining a function to delete supplier
        supplier_id = self.supplierId_entry.get()  # get supplier ID from entry widget
        if supplier_id:   # if supplier ID is given
            found = False
            # use for loop to iterate through supplier list to find the supplier with the given ID
            for supplier in self.supplier_list:
                if supplier.get_id() == supplier_id:   # if the IDs are equal
                    self.supplier_list.remove(supplier)  # remove the supplier from the list
                    found = True  #set found to True and break
                    break
            if found:     #if found show message of success
                messagebox.showinfo("Success", f"Supplier deleted: ID - {supplier_id}")
            else:    # if supplier with the given ID is not found, show error message
                messagebox.showerror("Error", f"Supplier with ID {supplier_id} not found")
            self.supplierId_entry.delete(0, tk.END)  # clear the entry widget
        else:    # otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter a supplier ID")

    def modify_supplier(self):  #defining a function to modify supplier
        supplier_id = self.supplierId_entry.get()  # get supplier ID from entry widget
        new_service = input("Enter new service: ")   # let user enter new service
        if supplier_id:  # if supplier ID is given
            found = False
            # use for loop to iterate through supplier list to find the supplier with the given ID
            for supplier in self.supplier_list:
                # if the IDs are equal, update the supplier service with the new service
                if supplier.get_id() == supplier_id:
                    supplier.set_service(new_service)
                    found = True #set found to True and break
                    break
            if found:        #if found show message of success
                messagebox.showinfo("Success", f"Supplier modified: ID - {supplier_id}, New Service - {new_service}")
            else:   # if supplier with the given ID is not found, show error message
                messagebox.showerror("Error", f"Supplier with ID {supplier_id} not found")
            self.supplierId_entry.delete(0, tk.END) #clear the entry widget
        else:  # otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter a supplier ID")

    def display_supplier(self):    #defining a function to display supplier
        supplier_id = self.supplierId_entry.get()    # get supplier ID from entry widget
        if supplier_id:  # if supplier ID is given
            found = False
            # use for loop to iterate through supplier list to find the supplier with the given ID
            for supplier in self.supplier_list:
                # if the IDs are equal, print the details
                if supplier.get_id() == supplier_id:
                    details = (
                        f"ID: {supplier.get_id()}\n"
                        f"Name: {supplier.get_name()}\n"
                        f"Address: {supplier.get_address()}\n"
                        f"Contact Details: {supplier.get_contact_details()}\n"
                        f"Service: {supplier.get_service()}"
                    )
                    messagebox.showinfo("Supplier Details:", details)
                    found = True #set found to True and break
                    break
            if not found:   # if supplier with the given ID is not found, show error message
                messagebox.showerror("Error", f"Supplier with ID {supplier_id} not found")
            self.supplierId_entry.delete(0, tk.END)   # clear the entry widget
        else:    # otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter a supplier ID")

    def add_guest(self):   #defining a function to add a guest
        guest_id = self.guestId_entry.get()  # get guest ID from entry widget
        if guest_id: # if guest ID is given
            # prompt user to input guest name, address, and contact details
            guest_name = input("Enter guest name: ")
            guest_address = input("Enter address: ")
            guest_contact = input("Enter contact details: ")
            #create a new Guest object with the provided details
            new_guest = Guest(guest_id, guest_name, guest_address, guest_contact)

            self.guest_list.append(new_guest)    # append the new guest to guest list
            self.guestId_entry.delete(0, tk.END) # clear the entry widget
            # show message of success
            messagebox.showinfo("Success", f"Guest with ID {guest_id} added")
        else: # otherwise, show error message
            messagebox.showerror("Error", "Please enter a guest ID")

    def delete_guest(self):    #defining a function to delete a guest
        guest_id = self.guestId_entry.get()   # get guest ID from entry widget
        if guest_id:  # if guest ID is given
            found = False
            # use for loop to iterate through guest list to find the guest with the given ID
            for guest in self.guest_list:
                if guest.get_guest_id() == guest_id:  # if the IDs are equal
                    self.guest_list.remove(guest) # remove the guest from the list
                    found = True #set found to True and break
                    break
            if found:       #if found show message of success
                messagebox.showinfo("Success", f"Guest deleted: ID - {guest_id}")
            else:       # if guest with the given ID is not found, show error message
                messagebox.showerror("Error", f"Guest with ID {guest_id} not found")
            self.guestId_entry.delete(0, tk.END) #clear the entry widget
        else:  # otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter a guest ID")

    def modify_guest(self): #defining a function to modify guest
        guest_id = self.guestId_entry.get()   # get guest ID from entry widget
        new_contact = input("Enter new contact details: ")  # let user enter new contact details
        if guest_id:  # if guest ID is given
            found = False
            # use for loop to iterate through guest list to find the guest with the given ID
            for guest in self.guest_list:
                # if the IDs are equal, update the guest contact details with the new details
                if guest.get_guest_id() == guest_id:
                    guest.set_guest_contact(new_contact)
                    found = True #set found to True and break
                    break
            if found:       #if found show message of success
                messagebox.showinfo("Success", f"Guest modified: ID - {guest_id}, New Contact - {new_contact}")
            else:    # if guest with the given ID is not found, show error message
                messagebox.showerror("Error", f"Guest with ID {guest_id} not found")
            self.guestId_entry.delete(0, tk.END)   # clear the entry widget
        else:    # otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter a guest ID")

    def display_guest(self):  #defining a function to display guest
        guest_id = self.guestId_entry.get()   # get guest ID from entry widget
        if guest_id:  # if guest ID is given
            found = False
            # use for loop to iterate through guest list to find the guest with the given ID
            for guest in self.guest_list:
                # if the IDs are equal, print the details
                if guest.get_guest_id() == guest_id:
                    details = (
                        f"ID: {guest.get_guest_id()}\n"
                        f"Name: {guest.get_guest_name()}\n"
                        f"Address: {guest.get_guest_address()}\n"
                        f"Contact Details: {guest.get_guest_contact()}"
                    )
                    messagebox.showinfo("Guest Details:", details)
                    found = True #set found to True and break
                    break
            if not found:    # if guest with the given ID is not found, show error message
                messagebox.showerror("Error", f"Guest with ID {guest_id} not found")
            self.guestId_entry.delete(0, tk.END)  # clear the entry widget
        else:  # otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter a guest ID")

    def add_venue(self):  #defining a function to add a venue
        venue_id = self.venueId_entry.get()  # get venue ID from entry widget
        if venue_id:    # if venue ID is given
            # prompt user to input venue name, address, contact details, minimum guests, and maximum guests
            venue_name = input("Enter venue name: ")
            venue_address = input("Enter venue's address: ")
            venue_contact = input("Enter contact details: ")
            min_guests = input("Enter minimum number of guests:")
            max_guests = input("Enter maximum number of guests:")
            # create a new Venue object with the provided details
            new_venue = Venue(venue_id, venue_name, venue_address, venue_contact, min_guests, max_guests)

            self.venue_list.append(new_venue)  # append the new venue to venue list
            self.venueId_entry.delete(0, tk.END)  # clear the entry widget
            # show message of success
            messagebox.showinfo("Success", f"Venue with ID {venue_id} added")
        else:    # otherwise, show error message
            messagebox.showerror("Error", "Please enter a venue ID")

    def delete_venue(self):  #defining a function to delete venue
        venue_id = self.venueId_entry.get()    # get venue ID from entry widget
        if venue_id:   # if venue ID is given
            found = False
            # use for loop to iterate through venue list to find the venue with the given ID
            for venue in self.venue_list:
                if venue.get_venue_id() == venue_id:  # if the IDs are equal
                    self.venue_list.remove(venue)  # remove the venue from the list
                    found = True #set found to True and break
                    break
            if found:   #if found show message of success
                messagebox.showinfo("Success", f"Venue deleted: ID - {venue_id}")
            else:    # if venue with the given ID is not found, show error message
                messagebox.showerror("Error", f"Venue with ID {venue_id} not found")
            self.venueId_entry.delete(0, tk.END) # clear the entry widget
        else:   # otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter a venue ID")

    def modify_venue(self):  #defining a function to modify venue
        venue_id = self.venueId_entry.get()    # get venue ID from entry widget
        new_max = input("Enter new max: ")   # let user enter new maximum number of guests
        if venue_id:   # if venue ID is given
            found = False
            # use for loop to iterate through venue list to find the venue with the given ID
            for venue in self.venue_list:
                # if the IDs are equal, update the venue maximum guests with the new maximum
                if venue.get_venue_id() == venue_id:
                    venue.set_max_guests(new_max)
                    found = True #set found to True and break
                    break
            if found: #if found show message of success
                messagebox.showinfo("Success", f"Venue modified: ID - {venue_id}, New Max Number of Guests - {new_max}")
            else:   # if venue with the given ID is not found, show error message
                messagebox.showerror("Error", f"Venue with ID {venue_id} not found")
            self.venueId_entry.delete(0, tk.END) # clear the entry widget
        else:     # otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter an venue ID")

    def display_venue(self):  #defining a function to display venue
        venue_id = self.venueId_entry.get()    # get venue ID from entry widget
        if venue_id:   # if venue ID is given
            found = False
            # use for loop to iterate through venue list to find the venue with the given ID
            for venue in self.venue_list:
                # if the IDs are equal, print the details
                if venue.get_venue_id() == venue_id:
                    details = (
                        f"ID: {venue.get_venue_id()}\n"
                        f"Name: {venue.get_venue_name()}\n"
                        f"Address: {venue.get_venue_address()}\n"
                        f"Contact Details: {venue.get_venue_contact()}\n"
                        f"Minimum Number of Guests: {venue.get_min_guests()}\n"
                        f"Maximum Number of Guests: {venue.get_max_guests()}"
                    )
                    messagebox.showinfo("Venue Details:", details)
                    found = True #set found to True and break
                    break
            if not found:    # if venue with the given ID is not found, show error message
                messagebox.showerror("Error", f"Venue with ID {venue_id} not found")
            self.venueId_entry.delete(0, tk.END)  # clear the entry widget
        else:   # otherwise, if ID is not provided show error message
            messagebox.showerror("Error", "Please enter a venue ID")

GUI()
