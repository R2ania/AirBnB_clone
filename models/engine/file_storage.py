#!/usr/bin/python3
''' This model for storing data '''
import json
import os
from models.base_model import BaseModel

class FileStorage:
	'''this class for storing data'''
	__file_path = "file.json" 
	__objects = {}


	def all(self):
		'''returns the all dictionries '''
		return FileStorage.__objects


	def new(self, obj):
		'''sets object in dictionary'''
		ob_class_name = obj.__class__.__name__
		key = "{}.{}".format(ob_class_name, obj.id)
		FileStorage.__objects[key] = obj


	def seve(self):
		'''serializes the dictionry to json file'''
		with open(FileStorage.__file_path, "w", encoding="utf-8") \
				as file:	
		json.dump(FaileStorage.__objects, file)


	def relaoud(self):
		'''check the if the json file is exist and deserialize it'''
		if os.path.exists(FileStorage.__file_path):
		with open(FileStorage.__file_path, "r", encoding="utf-8") \
				as file:
		json.load(FileStorage.__objects, file)

