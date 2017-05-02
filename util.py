import random


def biggest(list):
    big = list[0]

    for number in list:
        if(abs(number) > abs(big)):
            big = number

    return big


def smallest(list):
    small = list[0]

    for number in list:
        if(abs(number) < abs(small)):
            small = number

    return small


def random_color():

    color = [random.randrange(255) for x in range(3)]
    color.append(255)

    return tuple(color)
