from django.test import TestCase
from .models import Item

class TestItemModel(TestCase):

    def test_done_defaults_to_False(self):
        item = Item(name="Item")
        item.save()
        self.assertEqual(item.name, "Item")
        self.assertFalse(item.done)
        
    def test_can_create_an_item_with_a_name_and_status(self):
        item = Item(name="Item", done=True)
        item.save()
        self.assertEqual(item.name, "Item")
        self.assertTrue(item.done)
        
    def test_item_as_a_string(self):
        item = Item(name='Item')
        self.assertEqual('Item', str(item))
    