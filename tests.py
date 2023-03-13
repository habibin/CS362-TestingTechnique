from task import conv_num
import random

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

            conv_num(rand_choice)

            # print(rand_choice, type(rand_choice), conv_num(rand_choice), type(conv_num(rand_choice)))

    def test2(self):
        # tests float numbers as strings
        for count in range(100):
            # creates positive and negative float numbers
            random_num = str(random.uniform(-100000, 1000000))

            # inserts a decimal in the float.
            string_length = len(random_num)
            dec_position = random.randint(0, string_length + 1)
            dec_float = random_num[:dec_position] + '.' + random_num[dec_position:]

            # random choice chooses one of the options randomly to test
            rand_choice = random.choice([random_num, dec_float])

            print(rand_choice, type(rand_choice), conv_num(rand_choice), type(conv_num(rand_choice)))


if __name__ == '__main__':
    unittest.main()
