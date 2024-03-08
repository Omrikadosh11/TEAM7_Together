
import unittest
import re
from auth import check_email , check_id , check_name , check_pass

class TestValidations(unittest.TestCase):

    def test_check_email(self):
        self.assertTrue(check_email("example@example.com"))
        self.assertTrue(check_email("user.name+tag+sorting@example.com"))
        self.assertFalse(check_email("plainaddress"))
        self.assertFalse(check_email("@missing-user.com"))
        self.assertFalse(check_email("email.domain.com"))
        self.assertFalse(check_email("email@111.222.333.44444"))

    def test_check_name(self):
        self.assertTrue(check_name("John"))
        self.assertFalse(check_name("Jo"))
        self.assertFalse(check_name("joh3n"))
        self.assertFalse(check_name("Jo!hn"))
        self.assertTrue(check_name("Jonathan"))
    
    def test_check_pass(self):
        self.assertFalse(check_pass("short"))
        self.assertFalse(check_pass("longenough"))
        self.assertTrue(check_pass("Lowercase123"))
        self.assertFalse(check_pass("UPPERCASE123"))
        self.assertTrue(check_pass("ValidPassword123"))
        self.assertFalse(check_pass("NoNumbers"))
        self.assertFalse(check_pass("Invalid Password123"))

    def test_check_id(self):
        self.assertTrue(check_id("123456789"))
        self.assertFalse(check_id("12345"))
        self.assertFalse(check_id("123456789a"))
        self.assertFalse(check_id("1234 6789A"))
        self.assertFalse(check_id("!@#$%^&*()"))

if __name__ == '__main__':
    unittest.main()
