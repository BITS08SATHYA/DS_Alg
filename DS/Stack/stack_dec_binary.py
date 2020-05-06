from pythonds.basic.stack import Stack


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"

    rem_stack = Stack()

    while dec_number > 0:
        remainder = dec_number % base
        rem_stack.push(remainder)
        dec_number = dec_number // base

    bin_string = ""
    while not rem_stack.isEmpty():
        a = digits[rem_stack.pop()]
        bin_string = bin_string + a
        # print(a)

    return bin_string


# print("42 is "+ base_converter(42))

# print("binary: ", base_converter(26,2))
# print("octal: ", base_converter(26,8))
print("hex: ", base_converter(26, 16))

# assert base_converter(2) == '10'
# assert base_converter(255) == '11111111'
# assert base_converter(8+1) == '1001'
