# -*- coding: utf-8 -*-
"""
@author: António Furtado
(2025) objective: class Studies 
"""
# Class Studies
from classes.gclass import Gclass
import datetime
class Studies(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_title','_field','_start_date','_center_id']
    # Class header title
    header = 'Studies'
    # field description for use in, for example, input form
    des = ['Study Id','Title','Field','Start Date','Center Id']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, title, field, start_date, center_id):
        super().__init__()
        # Object attributes
        id = Studies.get_id(id)
        self._id = id
        self._title = title
        self._field = field
        self._start_date = datetime.date.fromisoformat(start_date)
        self._center_id = center_id
        # Add the new object to the dictionary of objects
        Studies.obj[id] = self
        # Add the id to the list of object ids
        Studies.lst.append(id)
    # id property getter method
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    # title property getter method
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
    # field property getter method
    @property
    def field(self):
        return self._field
    # field property setter method
    @field.setter
    def field(self, field):
        self._field = field
    # start date property getter method
    @property
    def start_date(self):
        return self._start_date
    # start date property setter method
    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date
    # center id property getter method
    @property
    def center_id(self):
        return self._center_id
    # center id property setter method
    @center_id.setter  
    def center_id(self, center_id):
        self._center_id = center_id