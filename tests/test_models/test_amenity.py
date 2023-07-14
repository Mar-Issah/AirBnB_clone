import unittest
from models.amenity import Amenity
import models
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_no_args(self):
        """Test for no arguments"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored(self):
        """Test cases for new instances stored in obj"""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_str(self):
        """Test if id is string"""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_datetime(self):
        """Test if createdAt is datetime"""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_datetime(self):
        """Test if updatedAt is datetime"""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_class_attribute(self):
        """Test if name is class attribute"""
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        """Test if two instances have unique ids"""
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_amenity_attributes(self):
        """Test the attributes present in the Amenity class"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    def test_amenity_initial_attributes(self):
        """Test the initial attribute values in the Amenity class"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_attribute_assignment(self):
        """Test attribute assignment in the Amenity class"""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_amenity_str_representation(self):
        """Test the __str__ method of the Amenity class"""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        str_repr = str(amenity)
        self.assertTrue("[Amenity]" in str_repr)
        self.assertTrue(amenity.id in str_repr)
        self.assertTrue(amenity.name in str_repr)


if __name__ == '__main__':
    unittest.main()
