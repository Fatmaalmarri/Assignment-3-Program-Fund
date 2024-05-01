#File 1: Classes_1.py
#Importing Enum class from the enum python module
from enum import Enum
#Using an enumerator class for event types (wedding, birthday, themed parties, and graduation)
class EventType(Enum):
    Wedding = "Wedding"
    Birthday = "Birthday"
    ThemedParties = "Themed Parties"
    Graduation = "Graduation"

class Event:
    """Class to represent an Event"""
    # Using initializing constructor to initialize attributes of Event class
    def __init__(self, event, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_comp, cleaning_comp,decorations_comp, entertainment_comp, furniture_comp, invoice, venue):
        #Initializing attributes
        self.__event = event
        self.__event_id = event_id
        self.__event_type = event_type
        self.__theme = theme
        self.__date = date
        self.__time = time
        self.__duration = duration
        self.__venue_address = venue_address
        self.__client_id = client_id
        self.__guest_list = guest_list
        self.__catering_comp = catering_comp
        self.__cleaning_comp = cleaning_comp
        self.__decorations_comp = decorations_comp
        self.__entertainment_comp = entertainment_comp
        self.__furniture_comp = furniture_comp
        self.__invoice = invoice
        #This represents aggregation between Venue and Event classes
        self.__venue = venue #aggregation

    #defining a function to assign a venue for an event
    def assign_venue(self, venue):
        self.__venue = venue

    #defining a function to add guests to the event, and appending it to the guest list
    def add_guest(self, guest):
        self.__guest_list.append(guest)

    #defining a function to remove guests from the event
    def remove_guest(self, guest):
        #Exception handling for removing guest
        try:
            # if guest is in the list remove guest, otherwise print guest not found
            if guest in self.__guest_list:
                self.__guest_list.remove(guest)
            else:
                raise ValueError("Guest not found")
        except ValueError as e:
            print("Error:", e)


    # Implementing setter and getter functions for Event class attributes
    def set_event(self, event):
        self.__event = event
    def get_event(self):
        return self.__event

    def set_event_id(self, event_id):
        self.__event_id = event_id
    def get_event_id(self):
        return self.__event_id

    def set_event_type(self, event_type):
        self.__event_type = event_type
    def get_event_type(self):
        return self.__event_type

    def set_theme(self, theme):
        self.__theme = theme
    def get_theme(self):
        return self.__theme

    def set_date(self, date):
        self.__date = date
    def get_date(self):
        return self.__date

    def set_time(self, time):
        self.__time = time
    def get_time(self):
        return self.__time

    def set_duration(self, duration):
        self.__duration = duration
    def get_duration(self):
        return self.__duration

    def set_venue_address(self, venue_address):
        self.__venue_address = venue_address
    def get_venue_address(self):
        return self.__venue_address

    def set_client_id(self, client_id):
        self.__client_id = client_id
    def get_client_id(self):
        return self.__client_id

    def set_guest_list(self, guest_list):
        self.__guest_list = guest_list
    def get_guest_list(self):
        return self.__guest_list

    def set_catering_comp(self, catering_comp):
        self.__catering_comp = catering_comp
    def get_catering_comp(self):
        return self.__catering_comp

    def set_cleaning_comp(self, cleaning_comp):
        self.__cleaning_comp = cleaning_comp
    def get_cleaning_comp(self):
        return self.__cleaning_comp

    def set_decorations_comp(self, decorations_comp):
        self.__decorations_comp = decorations_comp
    def get_decorations_comp(self):
        return self.__decorations_comp

    def set_entertainment_comp(self, entertainment_comp):
        self.__entertainment_comp = entertainment_comp
    def get_entertainment_comp(self):
        return self.__entertainment_comp

    def set_furniture_comp(self, furniture_comp):
        self.__furniture_comp = furniture_comp
    def get_furniture_comp(self):
        return self.__furniture_comp

    def set_invoice(self, invoice):
        self.__invoice = invoice
    def get_invoice(self):
        return self.__invoice

    def set_venue(self, venue):
        self.__venue = venue
    def get_venue(self):
        return self.__venue

    #Display Event Details
    def displayEvent(self):
        print("Event:", self.__event, " - Event ID:", self.__event_id)
        print("Type:", self.__event_type.value, " - Theme:", self.__theme)
        print("Date:", self.__date, " - Time:", self.__time)
        print("Event's Duration:", self.__duration)
        print("Venue Address:", self.__venue_address)
        print("Client ID:", self.__client_id)
        print("Guests List:")
        for guest in self.__guest_list:
            print("-", guest.get_guest_name())
        print("Catering Company:", self.__catering_comp)
        print("Cleaning Company:", self.__cleaning_comp)
        print("Decorations Company:", self.__decorations_comp)
        print("Entertainment Company:", self.__entertainment_comp)
        print("Furniture Supply Company:", self.__furniture_comp)
        print("Invoice:", self.__invoice)
        print("Venue:", self.__venue.get_venue_name())

class Client:
    """Class to represent a client"""
    #Using initializing constructor to initialize attributes of Client class
    def __init__(self, id, name, address, contact_details, budget):
        #Initializing attributes
        self.__id = id
        self.__name = name
        self.__address = address
        self.__contact_details = contact_details
        self.__budget = budget
        #This represents composition between Event and Client classes
        self.__events = [] #composition (an event cannot exist without a client)

    #defining a function to add an event for the client
    def add_event(self, event):
        self.__events.append(event)

    # Implementing setter and getter functions for Client class attributes
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

    def set_budget(self, budget):
        self.__budget = budget
    def get_budget(self):
        return self.__budget

    #Display Client Details
    def displayClient(self):
        print("Client Details:")
        print("ID:", self.__id, " - Name:", self.__name)
        print("Address:", self.__address, "- Contact Details:", self.__contact_details)
        print("Budget:", self.__budget)

class Guest:
    """Class to represent a guest"""
    #Using initializing constructor to initialize attributes of Guest class
    def __init__(self, guest_id, guest_name, guest_address, guest_contact):
        #Initializing attributes
        self.__guest_id = guest_id
        self.__guest_name = guest_name
        self.__guest_address = guest_address
        self.__guest_contact = guest_contact

    # Implementing setter and getter functions for Guest class attributes
    def set_guest_id(self, guest_id):
        self.__guest_id = guest_id
    def get_guest_id(self):
        return self.__guest_id

    def set_guest_name(self, guest_name):
        self.__guest_name = guest_name
    def get_guest_name(self):
        return self.__guest_name

    def set_guest_address(self, guest_address):
        self.__guest_address = guest_address
    def get_guest_address(self):
        return self.__guest_address

    def set_guest_contact(self, guest_contact):
        self.__guest_contact = guest_contact
    def get_guest_contact(self):
        return self.__guest_contact

    #Display Guest Details
    def displayGuest(self):
        print("Guest Details:")
        print("ID:", self.__guest_id, " - Name:", self.__guest_name)
        print("Address:", self.__guest_address, " - Contact Details:", self.__guest_contact)

class Venue:
    """Class to represent a venue"""
    #Using initializing constructor to initialize attributes of Venue class
    def __init__(self, venue_id, venue_name, venue_address, venue_contact, min_guests, max_guests):
        #Initializing attributes
        self.__venue_id = venue_id
        self.__venue_name = venue_name
        self.__venue_address = venue_address
        self.__venue_contact = venue_contact
        self.__min_guests = min_guests
        self.__max_guests = max_guests

    #defining a function to modify the capacity of the venue and change the max number of guests
    def modify_capacity(self, new_max_guests):
        self.__max_guests = new_max_guests

    # Implementing setter and getter functions for Venue class attributes
    def set_venue_id(self, venue_id):
        self.__venue_id = venue_id
    def get_venue_id(self):
        return self.__venue_id

    def set_venue_name(self, venue_name):
        self.__venue_name = venue_name
    def get_venue_name(self):
        return self.__venue_name

    def set_venue_address(self, venue_address):
        self.__venue_address = venue_address
    def get_venue_address(self):
        return self.__venue_address

    def set_venue_contact(self, venue_contact):
        self.__venue_contact = venue_contact
    def get_venue_contact(self):
        return self.__venue_contact

    def set_min_guests(self, min_guests):
        self.__min_guests = min_guests
    def get_min_guests(self):
        return self.__min_guests

    def set_max_guests(self, max_guests):
        self.__max_guests = max_guests
    def get_max_guests(self):
        return self.__max_guests

    #Display Venue Details
    def displayVenue(self):
        print("Venue Information:")
        print("ID:", self.__venue_id, " - Name:", self.__venue_name )
        print("Address:", self.__venue_address, " - Contact Information:", self.__venue_contact)
        print("Minimum number of guests:", self.__min_guests)
        print("Maximum number of guests:", self.__max_guests)
