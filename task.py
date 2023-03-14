def conv_num(num_str):
    """function takes in a string and converts it into a base 10 number,
    and returns it"""

    # returns None if num_str is not string type of if it is empty string
    if type(num_str) != str or num_str == '':
        return None

    index = 0
    # checks if there is a negative in first index
    if num_str[0] == "-":
        index = 1
    # checks if string is a hexadecimal by seeing if it starts with 0x
    if num_str[index] == "0":
        if num_str[index + 1].lower() == "x":
            # the index tells the function helper where to
            # stop converting the index in the string
            index += 1
            # function helper is called when the string is a hexadecimal
            return hex_check(num_str, index)
    # function helper will check if string is a float then it will convert it
    return float_check(num_str, index)


def hex_check(num_str, index):
    # dictionary key=hex:value=decimal
    base_16 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}

    exp = 0  # exponent that will be raised to the base 16
    total = 0  # will keep track of the total
    # when each index in the string is added

    # loops from the last position in the string to index in reverse
    for pos in range((len(num_str) - 1), index, -1):
        # sets the value of the string position to the dictionary key and use
        # upper() so that it is case-insensitive.
        key = num_str[pos].upper()
        # checks if the key is in dictionary
        if key in base_16:
            # finds the value the key is paired to
            value = base_16[key]
            # multiplies the value with the base 16
            count = value * 16 ** exp
            # updates total count
            total += count
            # increments the exponent by 1
            exp += 1
        # if the key is not found in the dictionary, returns None value
        else:
            return None
    # if the index==2, that means the number is negative.
    if index == 2:
        return -total
    # otherwise, it will return the positive value
    else:
        return total


def float_check(num_str, index):

    # dictionary key=str:value=float
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    total = 0
    before_dec = .0  # will keep track of the total when
    # each index in the string is added
    dec_count = dec_check(num_str, index)  # if a decimal is present,
    # at the end total * 10**dec_count
    decimal_check = 'no'
    # Once decimal is found, variable will be set to "yes" so there isn't
    # 2 decimals in the string

    # loops from the last position in the string to index in reverse
    for pos in range(index, (len(num_str))):
        # sets the value of the string position to the dictionary key
        key = num_str[pos]
        # checks if the key is a decimal
        if key == '.':
            # checks if there's already been a decimal
            if decimal_check == 'no':
                # changes variable to yes, so if another decimal is found,
                # it will return None
                decimal_check = 'yes'
                # finds where the decimal should be placed in the float
                before_dec = total
                total = 0.0
                continue
        # checks if the key is in dictionary
        if key in digits:
            # finds the value the key is paired to
            value = digits[key]
            # multiplies the value with the base 10
            count = value * 10 ** dec_count
            # updates total count
            total += count
            # increments the exponent by 1
            dec_count -= 1
        # if the key is not found in the dictionary, returns None value
        else:
            return None
    if before_dec != 0:
        total = total + before_dec
    total = round(total, len(num_str)-1)
    # if the index==1, that means the number is negative.
    if index == 1:
        return -total
    # otherwise, it will return the positive value
    else:
        return total


def dec_check(num_str, index):
    dec_count = -1
    for pos in range(index, len(num_str)):
        if num_str[pos] != '.':
            dec_count += 1
        if num_str[pos] == '.':
            return dec_count
    return dec_count


def my_datetime(num_sec):
    # convert the given number of seconds into number of days
    num_days = int(((num_sec / 60) / 60) / 24)
    # initialize the starting date and dictionary of
    # how many days are in each month
    curr_month = 1
    curr_day = 1
    curr_year = 1970
    month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days_in_month = month_dict[curr_month]
    # add days until we get to the target date
    while num_days != 0:
        curr_day += 1
        num_days -= 1
        # if in february, check for leap year
        # Source for how to check if a year is a leap year
        # https://learn.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
        if curr_month == 2 and curr_day == 2:
            if curr_year % 4 == 0:
                days_in_month = 29
                if curr_year % 100 == 0:
                    if curr_year % 400 != 0:
                        days_in_month = 28
        # if at end of month, reset day to 1, update month and year accordingly
        if curr_day > days_in_month:
            curr_day = 1
            curr_month += 1
            if curr_month > 12:
                curr_month = 1
                curr_year += 1
            days_in_month = month_dict[curr_month]

    # format the results
    # source for how to properly format f-strings for 2 digit format
    # https://saralgyaan.com/posts/f-string-in-python-usage-guide/#Python_string_formatting_at_a_glance
    # The main section used was "Python f-strings padding"
    return f"{curr_month:02d}-{curr_day:02d}-{curr_year}"


def conv_endian(num, endian='big'):
    if num == 0:
        return "00"
    if endian != 'big' and endian != 'little':
        return None
    byte_list = []
    negative = False
    hex_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if num < 0:
        negative = True
    num = abs(num)

    # convert number to hex
    # source for how to do conversion
    # https://www.permadi.com/tutorial/numDecToHex/
    while num != 0:
        remainder = num % 16
        byte_list.append(hex_table[remainder])
        num = num // 16
    if len(byte_list) % 2 != 0:
        byte_list.append('0')

    # convert the byte list to an endian string
    end_string = make_end_str(byte_list)

    # convert to little endian by creating string with original list
    if endian == 'little':
        end_string = convert_little_end(end_string)

    # add a negative sign to the front if the original number was negative
    if negative:
        end_string = "-" + end_string
    return end_string


def make_end_str(list_of_bytes):
    list_of_bytes.reverse()
    counter = 0
    end_string = ""
    for i in range(len(list_of_bytes)):
        end_string += list_of_bytes[i]
        counter += 1
        if counter == 2:
            counter = 0
            end_string += " "
    return end_string


def convert_little_end(big_str):
    temp_str = ""
    counter = -3
    last_pos = None
    while abs(counter) <= len(big_str):
        temp_str += big_str[counter:last_pos]
        last_pos = counter
        counter -= 3
    big_str = temp_str
    return big_str
