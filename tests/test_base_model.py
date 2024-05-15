#!/usr/bin/python3
'''This is the Test File For Base Model'''
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
	def test__init__(self):
		'''Test Constrctor'''
		my_model = BaseModel()
		self.assertIsNotNone(my_model.id)
		self.assertIsNotNone(my_model.created_at)
		self.assertIsNotNone(my_model.updated_at)


	def test_save(self):
		''' Test save method'''
		my_model = BaseModel()
		last_time = my_model.updated_at
		currnt_time = my_model.save()
		self.assertNotEqual(last_time, currnt_time)


	def test_to_dict(self):
		'''Test to_dict method'''
		my_model = BaseModel()
		my_model_dic = my_model.to_dict()
		self.assertIsInstance(my_model_dic, dict)
		self.assertEqual(my_model_dic["__class__"], "BaseModel")
		self.assertEqual(my_model_dic["id"], my_model.id)
		self.assertEqual(my_model_dic["created_at"], \
                        my_model.created_at.isoformat())
		self.assertEqual(my_model_dic["updated_at"], \
			my_model.updated_at.isoformat())


	def test__str__(self):
		'''Test __str__ mehod'''
		my_model = BaseModel()
		self.assertTrue(str(my_model).startswith('[BaseModel]'))
		self.assertIn(my_model.id, str(my_model))
		self.assertIn(str(my_model.__dict__), str(my_model))




if __name__ == '__main__':
	unittest.main()

