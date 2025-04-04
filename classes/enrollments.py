"""
@author: Gonçalo Braz
(2025) objective: class Enrollments
"""
# Class Enrollments
from classes.gclass import Gclass
import datetime
class Enrollments(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_participant_id','_study_id','_enrollment_date','_consent_status','_status']
    # Class header title
    header = 'Enrollments'
    # field description for use in, for example, input form
    des = ['Enrollment Id','Participant Id','Study Id','Enrollment Date','Consent Status','Status']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, participant_id, study_id, enrollment_date, consent_status, status):
        super().__init__()
        # Object attributes
        id = Enrollments.get_id(id)
        self._id = id
        self._participant_id = participant_id
        self._study_id = study_id
        self._enrollment_date = datetime.datetime.strptime(enrollment_date, '%d/%m/%Y').date()
        self._consent_status = consent_status
        self._status = status
        # Add the new object to the dictionary of objects
        Enrollments.obj[id] = self
        # Add the id to the list of object ids
        Enrollments.lst.append(id)

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def participant_id(self):
        return self._participant_id
    @participant_id.setter
    def participant_id(self, participant_id):
        self._participant_id = participant_id

    @property
    def study_id(self):
        return self._study_id
    @study_id.setter
    def study_id(self, study_id):
        self._study_id = study_id

    @property
    def enrollment_date(self):
        return self._enrollment_date
    @enrollment_date.setter
    def enrollment_date(self, enrollment_date):
        self._enrollment_date = enrollment_date

    @property
    def consent_status(self):
        return self._consent_status
    @consent_status.setter
    def consent_status(self, consent_status):
        self._consent_status = consent_status
    
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        self._status = status























