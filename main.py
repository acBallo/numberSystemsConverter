
def base_check(xnumber, xbase):  # checks if any of the digits in a number are larger then it's base
    for char in xnumber[len(xnumber ) -1]:
        if int(char) >= int(xbase):
            return False
    return True

def convert_from_10(xnumber, xbase, arr, ybase):  # converts a base 10 number to the equivalent in a different base
    if int(xbase) == 2 or int(xbase) == 4 or int(xbase) == 6 or int(xbase) == 8:

        if xnumber == 0:
            return arr
        else:
            quotient = int(xnumber) // int(xbase)
            remainder = int(xnumber) % int(xbase)
            arr.append(remainder)
            dividend = quotient
            convert_from_10(dividend, xbase, arr, base)
    elif int(xbase) == 16:
        if int(xnumber) == 0:
            return arr
        else:
            quotient = int(xnumber) // int(xbase)
            remainder = int(xnumber) % int(xbase)
            if remainder > 9:
                if remainder == 10: remainder = 'A'
                if remainder == 11: remainder = 'B'
                if remainder == 12: remainder = 'C'
                if remainder == 13: remainder = 'D'
                if remainder == 14: remainder = 'E'
                if remainder == 15: remainder = 'F'
            arr.append(remainder)
            dividend = quotient
            convert_from_10(dividend, xbase, arr, ybase)
def convert_to_10(xnumber, xbase, arr, ybase):  # converts a number from a base to base 10
    if int(xbase) == 10:
        for char in xnumber:
            arr.append(char)
        flipped = arr[::-1]
        ans = 0
        j = 0

        for i in flipped:
            ans = ans + (int(i) * (int(ybase) ** j))
            j = j + 1
        return ans









arrayfrom = []
arrayto = []
is_base_possible = False
number = input("Enter the number you would like to convert: ")

while not is_base_possible:  # checks if the base entered is possible for the number
    base = input("What is the base of this number? ")
    is_base_possible = base_check(number, base)
    if not is_base_possible:
        print(f"The number {number} is not a base {base} number")
        base = input
    else:
        break

dBase = input("What is the base you would like to convert to? ")
if int(base) == 10:  # converting from base 10
    convert_from_10(number, dBase, arrayfrom, base)
    answer = arrayfrom[::-1]  # reverses the array
    print(f"In base {dBase} this number is: ")
    print(*answer, sep='')  # prints array without dividers
elif int(dBase) == 10:  # converting to base 10
    answer = convert_to_10(number, dBase, arrayto, base)
    print(f"In base {dBase} this number is: {answer} ")
else:  # number is converted to base 10 before converted to other number systems
    number = convert_to_10(number, 10, arrayto, base)
    convert_from_10(number, dBase, arrayfrom, base)
    answer = arrayfrom[::-1]
    print(f"In base {dBase} this number is: ")
    print(*answer, sep='')

