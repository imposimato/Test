BASE_CONV = '0123456789abcdef'

def conv_base(number, base):

    result_str = ""
    while number > 0:

        if 2 > base > len(BASE_CONV):
            print("Please inform a base up to" + str(len(BASE_CONV)))
            break

        result_str = str(BASE_CONV[number % base]) + result_str

        number //= base

    return result_str


def bin_int(bin, base):
    int_res = 0
    temp_num = str(bin)
    power = 0
    while len(temp_num)>0:
        count = 0
        for number in BASE_CONV:
            if number == temp_num[-1]:
                break
            else:
                count += 1

        int_res += count * (base ** power)
        power += 1
        temp_num = temp_num[:-1]

    return int_res


print(bin_int('aaa',16))
#print(conv_base(2730,16))
# base_str = input('Please, inform the base: ')
# base_int = int(base_str)
# number_str = input('Please, inform the number: ')
# number_int = int(number_str)
# print(conv_base(number_int, base_int))