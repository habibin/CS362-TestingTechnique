def conv_num(num_str):

    return num_str


def my_datetime(num_sec):
    # convert the given number of seconds into number of days
    num_days = int(((num_sec / 60) / 60) / 24)
    # initalize the starting date and dictionary of how many days are in each month
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
    hex_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    remainder = -1
    if num < 0:
        negative = True
    num = abs(num)

    # convert number to hex
    # source for how to do conversion https://www.permadi.com/tutorial/numDecToHex/
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
