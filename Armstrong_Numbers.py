def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    sum_of_digits = sum(int(digit) ** n for digit in num_str)
    return sum_of_digits == num

armstrong_numbers = [num for num in range(100001) if is_armstrong(num)]

print(','.join(map(str, armstrong_numbers)))
