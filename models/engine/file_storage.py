#!/usr/bin/python3
''' This model for storing data '''
import json
import os




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


	def save(self):
		'''serializes the dictionry to json file'''
		with open(FileStorage.__file_path, "w") as file:	
			json.dump(FileStorage.__objects, file)


	def reload(self):
		'''check the if the json file is exist and deserialize it'''
		if os.path.exists(FileStorage.__file_path):
			with open(FileStorage.__file_path, "r") as file:
				json.load(file)

