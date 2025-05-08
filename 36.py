
number = 585


def check_palindrome(number):
    number_str = str(number)
    length = len(number_str)
    for i in range(length//2):
        if number_str[i] != number_str[length-i-1]:
            return False
    return True


def convert_to_base(number, base):
    if number == 0:
        return "0"
    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    return ''.join(str(x) for x in digits[::-1])
ans = []
for i in range(1, 1000000):
    if check_palindrome(i) and check_palindrome(convert_to_base(i, 2)):
        print(f"Found: {i} in base {2}: {convert_to_base(i, 2)}")
        ans.append(i)

print(f"Sum of all numbers: {sum(ans)}")
