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
