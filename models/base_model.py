#!/usr/bin/python3
'''This is The Base module its represent the Backbone of the project'''
import uuid
import datetime


class Basemodel():
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
		return self.__dict__ and self.__class__
		datetime.isoformat(self.created_at, self.updated_at)

