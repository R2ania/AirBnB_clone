#!/usr/bin/python3
'''This is The Base module its represent the Backbone of the project'''
import uuid
import datetime


class BaseModel():
	''' Is the base class for the other classes'''
	def __init__(self):
		''' Constructor'''
		self.id = str(uid.uuid4())
		self.created_at = datetime.datetime.utcnow()
		self.updated_at = datetime.datetime.utcnow()

	def save(self):
		''' update the instance (updated_at) with the currnt datetime'''
		return datetime.datetime.utcnow(self.updated_at)


	def to_dic(self):
		'''return a dictionary contaning all keys of instances'''
		dic = self.__dict__.copy()
		dic["__class__"] = self.__class__.__name__
		dic["created_at"] = self.created_at.isoformat()
		dic["updated_at"] = self.updated_at.isoformat()
		return dic


	def __str__(self):
		'''Print class name,id and the values'''
		class_name = self.__class__.__name__
		return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

