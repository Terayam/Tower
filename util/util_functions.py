import random


def linear_interp_tuple_list(table, lookup):

    # Find closest index greater than lookup
    closest_index = 0
    last_index = 0

    for index in range(len(table)):

        if(table[index][0] > lookup):
            closest_index = index
            break

        last_index = index

    print("ci: {}, li: {}".format(closest_index, last_index))

    # interpolate x
    inter_x = linear_interp(table[last_index][0],
                            table[closest_index][0],
                            table[last_index][1],
                            table[closest_index][1],
                            lookup)

    # intrpolate y
    inter_y = linear_interp(table[last_index][0],
                            table[closest_index][0],
                            table[last_index][2],
                            table[closest_index][2],
                            lookup)

    return (inter_x, inter_y)


def linear_interp(x1, x2, y1, y2, lookup):

    if((x2 - x1) == 0):
        return y1

    else:
        return ((((y2 - y1) * (lookup - x1)) / (x2 - x1)) + y1)


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
