
def sum(a:int, b:int):
    return a + b

def sum(numbers):
    current_sum = 0
    for number in numbers:
        current_sum = current_sum + number
    return current_sum

def sum(*args):
    current_sum = 0
    for number in args:
        current_sum += number
    return current_sum


def sum_even(numbers):
    length = len(numbers)
    sum = 0
    for index in range(length):
        if index % 2 != 0:
            sum = sum + numbers[index]
    return sum


def main():
    my_sum = sum_even([5, 6, 12])
    print(my_sum)


if __name__ == "__main__":
    main()
