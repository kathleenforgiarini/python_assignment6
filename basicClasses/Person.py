"""
    Topic: Person Class
    Date: 13 Nov 2023
    Author: Kathleen
"""

class Person:
    def __init__(self, firstName="", lastName="", phone=""):
        self._firstName = firstName
        self._lastName = lastName
        self._phone = phone

    def getFirstName(self):
        return self._firstName
    
    def setFirstName(self, firstName):
        if firstName == None:
            print(f"Error, the first name can not be null")
        else:
            self._firstName = firstName

    def getLastName(self):
        return self._lastName

    def setLastName(self, lastName):
        if lastName == None:
            print(f"Error, the last name can not be null")
        else:
            self._lastName = lastName

    def getPhone(self):
        return self._phone

    def setPhone(self, phone):
        if phone == None:
            print(f"Error, the phone can not be null")
        else:
            self._phone = phone

    def __str__(self):
        return f"First Name: {self._firstName} Last Name: {self._lastName} Phone: {self._phone}"
