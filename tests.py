from task import conv_num
import random
import string
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        # tests the hexadecimals in conv_num() function with correct hexadecimals uppercase, lowercase, and negative #
        for count in range(100):
            # creates a random correct positive hex string
            random_pos_hex = hex(random.randint(0, 100000))

            # creates a random correct negative hex string
            random_neg_hex = hex(random.randint(-100000, 0))

            # selects either a positive or negative hexadecimal
            choice1 = random.choice([random_pos_hex, random_neg_hex])

            # creates a hexadecimal with a decimal in it.
            string_length = len(choice1)
            dec_position = random.randint(0, string_length + 1)
            dec_hex = choice1[:dec_position] + '.' + choice1[dec_position:]

            # creates hexadecimals that contain letters greater than f, uppercase or lowercase.
            letters = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            # selects a random lowercase or uppercase letter
            letter = random.choice([random.choice(letters), random.choice(letters).upper()])
            # inserts the letter at random location in the hexadecimal.
            letter_hex = choice1[:dec_position] + letter + choice1[dec_position:]

            # random choice chooses one of the options randomly to test
            rand_choice = random.choice([random_pos_hex.upper(), random_pos_hex.lower(), random_neg_hex.upper(),
                                         random_neg_hex.lower(), dec_hex, letter_hex])

            print(rand_choice, type(rand_choice), conv_num(rand_choice), type(conv_num(rand_choice)))

    def test2(self):
        # tests float numbers as strings
        for count in range(100):
            # creates positive and negative float numbers
            random_float = str(random.uniform(-99999999, 99999999))

            random_int = str(random.randint(-99999999, 99999999))

            # inserts a decimal in the float.
            string_length = len(random_float)
            dec_position = random.randint(0, string_length + 1)
            dec_float = random_float[:dec_position] + '.' + random_float[dec_position:]

            # inserted a letter at random position
            choice1 = random.choice([random_float, random_int])
            string_length = len(choice1)
            dec_position = random.randint(0, string_length + 1)
            letter = random.choice(string.ascii_letters)
            letter_number = choice1[:dec_position] + letter + choice1[dec_position:]

            # random choice chooses one of the options randomly to test
            rand_choice = random.choice([random_float, dec_float, random_int, letter_number, '', 1])

            print(rand_choice, type(rand_choice), conv_num(rand_choice), type(conv_num(rand_choice)))


if __name__ == '__main__':
    unittest.main()
