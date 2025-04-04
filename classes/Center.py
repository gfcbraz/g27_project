"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
class Center(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ["_id", "_center_name", "_location"]
    # Class header title
    header = 'Centers'
    # field description for use in, for example, input form
    des = ["Center ID", "Center Name", "Location"]
    # Constructor: Called when an object is instantiated
    def __init__(self, id, center_name, location):
        super().__init__()
        # Object attributes
        id = Center.get_id(id)
        self._id = id
        self._center_name = center_name
        self._location = location
        
        # Add the new object to the dictionary of objects
        Center.obj[id] = self
        # Add the id to the list of object ids
        Center.lst.append(id)
    # id property getter method
    @property
    def id(self):
        return self._id
    # id property setter method
    @id.setter
    def id(self, id):
        self._id = id
    # center_name property getter method
    @property
    def center_name(self):
        return self._center_name
    # center_name property setter method
    @center_name.setter
    def center_name(self, center_name):
        self._center_name = center_name
    # location property getter method
    @property
    def location(self):
        return self._location
    # location property setter method
    @location.setter
    def location(self, location):
        self._location = location