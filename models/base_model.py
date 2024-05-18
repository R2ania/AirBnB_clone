#!/usr/bin/python3
'''This is The Base module its represent the Backbone of the project'''
import uuid
from datetime import datetime
from models import  storage




class BaseModel():


	''' Is the base class for the other classes'''


	def __init__(self, *args, **kwargs):
		'''
		Initialize instance attributes


		Args:
		-*args: List of arguments
		-**kwargs: dict of key-value arguments
'''
		datetime_format = "%d/%m/%y"
		if kwargs:
			for key, value in kwargs.itms():
				if key == "__class__":
					continue
				elif key == "created_at" or "updated_at":
					setattr(self, key, datetime.strptime\
						(value, datetime_format))
				else:
					setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = (datetime.datetime.utcnow())
			self.updated_at = (datetime.datetime.utcnow())
			storage.new(self)


	def save(self):
		''' update the instance (updated_at) with the currnt datetime'''
		self.updated_at = datetime.datetime.utcnow()
		storage.save()


	def to_dict(self):
		'''return a dictionary contaning all keys of instances'''
		dic = self.__dict__.copy()
		dic["__class__"] = type(self).__name__
		dic["created_at"] = dic["created_a"]t.isoformat()
		dic["updated_at"] = dic["updated_at"].isoformat()
		return dic


	def __str__(self):
		'''Print class name,id and the values'''
		class_name = self.__class__.__name__
		return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

