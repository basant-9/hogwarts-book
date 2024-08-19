name = input("Enter the name : ")
email = input("Enter the email: ")
phone_number = input("Enter the phone number: ")
class MagicalContact:
    def __init__(self, name, email, phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def set_email(self, email):
        self.__email = email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number 
    
    def describe (self):
        print(f"Name: {self.__name}, Email: {self.__email}, Phone: {self.__phone_number}")

wand_core = input("Enter the wand core: ")
wand_wood = input("Enter the wand wood: ")
wand_length = input("Enter the wand length: ")
house = input("Enter the house (Gryffindor, Hufflepuff, Ravenclaw, Slytherin): ")
class WizardOrWitch(MagicalContact):
    def __init__(self, name, email, phone_number, wand_core, wand_wood, wand_length , houses):
        houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        if houses not in houses :
            print("value error ")
        self.__houses = houses
        self.__wand = {
            "core": wand_core,
            "wood": wand_wood,
            "length": wand_length
        } 

    def get_wand(self):
        return f"{self.__wand['length']}, {self.__wand['wood']}, {self.__wand['core']}"

    def get_house(self):
        return self.__house

    def describe(self):
        print (f"house :{self.__houses} , {self.__wand['length']}, {self.__wand['wood']}, {self.__wand['core']}")
 
species = input("Enter the species: ")
is_tame_input = input("Is tame? : ")
class MagicalCreature (MagicalContact) : 
    def __init__ (self, name , email , phone_number , species , is_tame ) :
        super().__init__(name,email,phone_number)
        self.__species = species
        self.__is_tame = is_tame

    def get_species(self):
        return self.__species
    
    def is_tame (self):
        return self.__is_tame
    
    def describe(self):
        print (f"species :{self.__species} , is_tame : {"yes" if self.__is_tame else "no"}" )

class  MagicalContactBook () :
    def __init__(self):
        self.__contacts = []

    def add_contact(self, contact):
        self.__contacts.append(contact)
        
    def list_contacts(self):
        for contact in self.__contacts:
            contact.describe()
    def find_contact(self, name):
        for contact in self.__contacts:
            if contact.get_name == name:
                contact.describe()
                return contact 

w = (name, email, phone_number, wand_core, wand_wood, wand_length, house)
print(w) 