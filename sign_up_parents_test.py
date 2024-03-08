import unittest
import auth


class TestCheckForm(unittest.TestCase):
    def test_checkemail(self):
        #supposed to success - the format is not valid
        self.assertEqual(auth.check_email("omri.com"),False)
        #supposed to success - the format is valid
        self.assertEqual(auth.check_email("omri@gmail.com"),True)
        #supposed to success - the format is not valid , only numbers
        self.assertEqual(auth.check_email("12345"),False)


    def test_checkname(self):
        #supposed to success - the format is not valid , numbers in name
        self.assertEqual(auth.check_name('1234'), False)
        #supposed to success - the format is valid
        self.assertEqual(auth.check_name('Omri'), True)
        #supposed to success - the format is not valid , too short
        self.assertEqual(auth.check_name('ok'), False)
        #supposed to success - the format is not valid , contains a speical char
        self.assertEqual(auth.check_name('Omri@kadosh'), False)

    def test_checkpassword(self):
        #supposed to success - the format is not valid , too short
        self.assertEqual(auth.check_pass('Ok123'),False)
        #supposed to success - the format is not valid , only numbers
        self.assertEqual(auth.check_pass('12343455466763'),False)
        #supposed to success - the format is not valid , only lowercase
        self.assertEqual(auth.check_pass('okdockcmaskmca'),False)
        #supposed to success - the format is not valid , not contain uppercase
        self.assertEqual(auth.check_pass('sdfs21352'),False)
        #supposed to success - the format is not valid , valid format
        self.assertEqual(auth.check_pass('Ok12345678'),True)
        #supposed to success - the format is not valid , contain space
        self.assertEqual(auth.check_pass('Ok123 45678'),False)

    def test_checkid(self):
        #supposed to success - the format is not valid , contain letters
        self.assertEqual(auth.check_id('Okkdsjc123'),False)
         #supposed to success - the format is not valid , too short
        self.assertEqual(auth.check_id('3432554'),False)
         #supposed to success - the format is not valid , too long
        self.assertEqual(auth.check_id('1234567891'),False)
         #supposed to success - the format is valid
        self.assertEqual(auth.check_id('123456789'),True)
        #supposed to success - the format is not valid , contain space
        self.assertEqual(auth.check_id('Ok123 45678'),False)
        #supposed to success - the format is not valid , contain letters
        self.assertEqual(auth.check_id('dsjcnfsdjbcjdsb'),False)




if __name__ == '__main__':
    unittest.main()