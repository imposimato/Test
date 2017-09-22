def hex(number):
    return {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }.get(number, number)


def conv_base(number, base, result_str = ""):

    while number > 0:

        if base == 16:
            result_str += str(hex(number % base))
        else:
            result_str += str(number % base)

        number //= base

    return result_str[::-1]


# base_str = input("Please, inform the base: ")
# base_int = int(base_str)
# number_str = input("Please, inform the number: ")
# number_int = int(number_str)
print(conv_base(25, 16))