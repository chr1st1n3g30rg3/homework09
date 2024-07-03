import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        test_object = BookLover("Vanessa", "vanessalovesbook@gmail.com", "Horror")
        test_object.add_book("The Shining", 5)
        self.assertTrue("The Shining" in test_object.book_list['book_name'].values)
    
    def test_2_add_book(self):
        '''Try adding the same book twice'''
        test_object = BookLover("Vanessa", "vanessalovesbook@gmail.com", "Horror")
        test_object.add_book("The Shining", 5)
        test_object.add_book("The Shining", 5)
        self.assertEqual(len(test_object.book_list[test_object.book_list['book_name'] == "The Shining"]), 1)
                
    def test_3_has_read(self): 
        test_object = BookLover("Vanessa", "vanessalovesbook@gmail.com", "Horror")
        test_object.add_book("The Shining", 5)
        self.assertTrue(test_object.has_read("The Shining"))
        
    def test_4_has_read(self): 
        test_object = BookLover("Vanessa", "vanessalovesbook@gmail.com", "Horror")
        self.assertFalse(test_object.has_read("The Haunting of Hill House"))
        
    def test_5_num_books_read(self): 
        test_object = BookLover("Vanessa", "vanessalovesbook@gmail.com", "Horror")
        test_object.add_book("The Shining", 5)
        test_object.add_book("Dracula", 2)
        test_object.add_book("House of Leaves", 1)
        self.assertEqual(test_object.num_books_read(), 3)

    def test_6_fav_books(self):
        test_object = BookLover("Vanessa", "vanessalovesbook@gmail.com", "Horror")
        test_object.add_book("The Shining", 5)
        test_object.add_book("Dracula", 2)
        test_object.add_book("House of Leaves", 1)
        fav_books = test_object.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))
                
if __name__ == '__main__':
    unittest.main(verbosity=3)