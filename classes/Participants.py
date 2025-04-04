"""
@author: Rui Graça
(2025) objective: class Participants
"""
# Class Participants - generic version with inheritance
from classes.gclass import Gclass
class Participants(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_name','_age']
    # Class header title
    header = 'Participants'
    # field description for use in, for example, input form
    des = ['Id','Name','Age']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, name, age):
        super().__init__()
        # Object attributes
        id = Participants.get_id(id)
        self._id = id
        self._name = name
        self._age = int(age)
        # Add the new object to the dictionary of objects
        Participants.obj[id] = self
        # Add the id to the list of object ids
        Participants.lst.append(id)
    # id property getter method
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    # name property getter method
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    # dob property getter method
    @property
    def age(self):
        return self._age
    # dob property setter method
    @age.setter
    def age(self, age):
        self._age = age



