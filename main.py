import random


def split(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """

    #################
    # Do not delete return statement
    return numbers


def main():
    numbers = [3, 2, 0, 5, 4]
    # print (id(numbers))
    numbers = split(numbers)
    # print (id(numbers))
    print(numbers)

    numbers = [random.randint(0, 20) for i in range(10)]
    print(numbers)
    numbers = split(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
