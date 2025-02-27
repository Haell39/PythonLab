def float_to_binary(num):
    if num < 0:
        sign = -1
        num = -num
    else:
        sign = 1

    integer_part = int(num)
    fractional_part = num - integer_part

    binary_integer = bin(integer_part).replace('0b', '')

    binary_fractional = []
    while fractional_part:
        fractional_part *= 2
        bit = int(fractional_part)
        if bit == 1:
            fractional_part -= bit
            binary_fractional.append('1')
        else:
            binary_fractional.append('0')
        if len(binary_fractional) > 32:  # Limit the length of the fractional part
            break

    binary_fractional = ''.join(binary_fractional)
    binary_number = f"{binary_integer}.{binary_fractional}" if binary_fractional else binary_integer

    return f"-{binary_number}" if sign == -1 else binary_number


def binary_to_float(binary_str):
    if binary_str[0] == '-':
        sign = -1
        binary_str = binary_str[1:]
    else:
        sign = 1

    if '.' in binary_str:
        integer_part, fractional_part = binary_str.split('.')
    else:
        integer_part, fractional_part = binary_str, ''

    integer_value = int(integer_part, 2)

    fractional_value = 0
    for i, bit in enumerate(fractional_part):
        fractional_value += int(bit) * (2 ** -(i + 1))

    return sign * (integer_value + fractional_value)


# Example usage:
real_number = 5
binary_representation = float_to_binary(real_number)
print(f"{real_number} in binary is {binary_representation}")

binary_number = "1001"
real_representation = binary_to_float(binary_number)
print(f"{binary_number} in decimal is {real_representation}")