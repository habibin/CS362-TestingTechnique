from task import conv_num, conv_endian, my_datetime
from datetime import datetime
import random
import string
import unittest




class TestCase(unittest.TestCase):

    def test1(self):
        # tests the hexadecimals in conv_num() function with correct
        # hexadecimals uppercase, lowercase, and negative #
        for count in range(100):
            # creates a random correct positive hex string
            random_pos_hex = hex(random.randint(0, 100000))

            # creates a random correct negative hex string
            random_neg_hex = hex(random.randint(-100000, 0))

            # selects either a positive or negative hexadecimal
            choice1 = random.choice([random_pos_hex, random_neg_hex])

            # creates a hexadecimal with a decimal in it.
            string_length = len(choice1)
            dec_pos = random.randint(0, string_length + 1)
            dec_hex = choice1[:dec_pos] + '.' + choice1[dec_pos:]

            # creates hexadecimals that contain letters greater than f,
            # uppercase or lowercase.
            letters = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            # selects a random lowercase or uppercase letter
            letter = random.choice([random.choice(letters),
                                    random.choice(letters).upper()])
            # inserts the letter at random location in the hexadecimal.
            letter_hex = choice1[:dec_pos] + letter + choice1[dec_pos:]

            # random choice chooses one of the options randomly to test
            rand_choice = random.choice([random_pos_hex.upper(),
                                         random_pos_hex.lower(),
                                         random_neg_hex.upper(),
                                         random_neg_hex.lower(),
                                         dec_hex, letter_hex])

            print(rand_choice, type(rand_choice),
                  conv_num(rand_choice), type(conv_num(rand_choice)))


    def test2(self):
        # tests float numbers as strings
        for count in range(100):
            # creates positive and negative float numbers
            random_float = str(random.uniform(-99999999, 99999999))

            random_int = str(random.randint(-99999999, 99999999))

            # inserts a decimal in the float.
            string_length = len(random_float)
            dec_pos = random.randint(0, string_length + 1)
            dec_float = random_float[:dec_pos] + '.' + random_float[dec_pos:]

            # inserted a letter at random position
            choice1 = random.choice([random_float, random_int])
            string_length = len(choice1)
            dec_pos = random.randint(0, string_length + 1)
            letter = random.choice(string.ascii_letters)
            letter_number = choice1[:dec_pos] + letter + choice1[dec_pos:]

            # random choice chooses one of the options randomly to test
            rand_choice = random.choice([random_float, dec_float, random_int,
                                         letter_number, '', 1])

            print(rand_choice, type(rand_choice),
                  conv_num(rand_choice), type(conv_num(rand_choice)))


    # Test Con_endian funtionality
    def test_zero(self):
        # Test if input number is zero if it will return correct result
        # Arrange
        num = 0
        expected = "00"
        # Act
        actual = conv_endian(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_invalid_endianness(self):
        # Test if the incorrect endian input will return correct result
        # Arrange
        num = 1234
        endian = 'random'
        expected = None
        # Act
        actual = conv_endian(num, endian)
        # Assert
        self.assertEqual(actual, expected)

    def test_positive_big_endian(self):
        # Test if the positive big endian input will return correct result
        # Arrange
        num = 1234
        expected = "04 D2 "
        # Act
        actual = conv_endian(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_positive_little_endian(self):
        # Test if the positive little endian input will return correct result
        # Arrange
        num = 1234
        endian = 'little'
        expected = "D2 04 "
        # Act
        actual = conv_endian(num, endian)
        # Assert
        self.assertEqual(actual, expected)

    def test_negative_big_endian(self):
        # Test if the negative big endian input will return correct result
        # Arrange
        num = -1234
        expected = "-04 D2 "
        # Act
        actual = conv_endian(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_negative_little_endian(self):
        # Test if the negative little endian input will return correct result
        # Arrange
        num = -1234
        endian = 'little'
        expected = "-D2 04 "
        # Act
        actual = conv_endian(num, endian)
        # Assert
        self.assertEqual(actual, expected)

    def test_large_positive_big_endian(self):
        # Arrange
        num = 4294967295
        expected = "FF FF FF FF "
        # Act
        actual = conv_endian(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_large_positive_little_endian(self):
        # Arrange
        num = 4294967295
        endian = 'little'
        expected = "FF FF FF FF "
        # Act
        actual = conv_endian(num, endian)
        # Assert
        self.assertEqual(actual, expected)

    def test_large_negative_big_endian(self):
        # Arrange
        num = -4294967295
        expected = "-FF FF FF FF "
        # Act
        actual = conv_endian(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_large_negative_little_endian(self):
        # Arrange
        num = -4294967295
        endian = 'little'
        expected = "-FF FF FF FF "
        # Act
        actual = conv_endian(num, endian)
        # Assert
        self.assertEqual(actual, expected)

    def test_empty_string(self):
    # Test that an empty string returns None

        num = ""
        expected = None
        # Act
        actual = conv_num(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_invalid_type(self):
        # Test that a non-string type returns None

        num = 123
        expected = None
        # Act
        actual = conv_num(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_negative_decimal(self):
        # Test that a negative decimal string returns the correct number

        num = "-12.34"
        expected = -12.34
        # Act
        actual = conv_num(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_positive_decimal(self):
        # Test that a positive decimal string returns the correct number

        num = "56.78"
        expected = 56.78
        # Act
        actual = conv_num(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_negative_hexadecimal(self):
        # Test that a negative hexadecimal string returns the correct number

        num = "-0x1a"
        expected = -26
        # Act
        actual = conv_num(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_positive_hexadecimal(self):
        # Test that a positive hexadecimal string returns the correct number

        num = "0x2b"
        expected = 43
        # Act
        actual = conv_num(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_end_decimal(self):
        # Test that a decimal will add a zero at the end

        num = "123."
        expected = 123.0
        # Act
        actual = conv_num(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_begining_decimal(self):
        # Test that a decimal will add a zero at the begining

        num = ".123"
        expected = 0.123
        # Act
        actual = conv_num(num)
        # Assert

        self.assertEqual(actual, expected)

    def test_combining_number_alph(self):
        # Test that a combination of num and alph
        num = ".123A"
        expected = None
        # Act
        actual = conv_num(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_incorrect_dec(self):
        # Test that a incorrect dec
        num = "1.2.3"
        expected = None
        # Act
        actual = conv_num(num)
        # Assert
        self.assertEqual(actual, expected)

    def test_incorrect_hex(self):
        # Test that a incorrect hex
        num = "0xAZ4"
        expected = None
        # Act
        actual = conv_num(num)
        # Assert
        self.assertEqual(actual, expected)

    #def testTime(self):
        #for i in range(0, 100):
            #random_seconds = random.randint(0, 253400000000)  # 0 to year 9999
            #our_result = my_datetime(random_seconds)
            #epoch = datetime(1970, 1, 1)
            #  https://www.mytecbits.com/internet/python/convert-date-to-mm-dd-yyyy
            #  source for formatting datetime to match format of our function
            #self.assertEqual(our_result, epoch.utcfromtimestamp(random_seconds).strftime("%m-%d-%Y"))

if __name__ == '__main__':
    unittest.main()
