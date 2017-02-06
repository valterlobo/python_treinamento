#Contato 
import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class Contato(Object):

     #Iniciar o contato
    def __init__(self, nome, email):
       
        self.nome = nome        
        self.email = email


    # A property is just like a getter.
    # It turns the method age() into an read-only attribute
    # of the same name.
    @property
    def nome(self):
        return self._nome

    # This allows the property to be set
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # This allows the property to be deleted
    @nome.deleter
    def nome(self):
        del self._nome

    @property
    def email(self):
        return self._email

    # This allows the property to be set
    @email.setter
    def email(self, email):
        self._email = email

    # This allows the property to be deleted
    @email.deleter
    def email(self):
        del self._email



