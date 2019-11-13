def largest_and_smallest(a, b, c):
    a = float(a)    #converts nums a,b,c into floats
    b = float(b)
    c = float(c)

    if a > b and a > c:  # compares a,b and c to their counterparts and find which one is the largest
        max_val = a
    elif b > a and b > c:
        max_val = b
    else:
        max_val = c

    if a < b and a < c:  # compares a,b and c to their counterparts and find which one is the smallest
        min_val = a
    elif b < a and b < c:
        min_val = b
    else:
        min_val = c

    if int(min_val) == float(min_val):  # this condition converts the min an max values from floats to integeres if possible
        min_val = int(min_val)
    if int(max_val) == float(max_val):
        max_val = int(max_val)

    return max_val, min_val     #return largest and smallest numbers from list

def check_largest_and_smallest(a,b,c):
    if largest_and_smallest(17,1,6) == (17,1):
        return True
    else:
        return False

    if largest_and_smallest(1,17,6) == (1,17):
        print(True)
        return True
    else:
        print(False)
        return False
    if largest_and_smallest(1,1,2) == (2,1):
        print(True)
        return True
    else:
        return False

    if largest_and_smallest(1,1.0000000001,0.99999999999) == (1.0000000001,0.99999999999):
        print(True)
        return True
    else:
        print(False)
        return False

    if largest_and_smallest(1,1,2) == (2,1):
        return True
    else:
        return False


check_largest_and_smallest()