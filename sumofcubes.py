"""
There is a popular conjecture in Maths which states that numbers that can be expressed as a sum of three cubes of integers,
 allowing both positive and negative cubes in the sum. Refer https://en.wikipedia.org/wiki/Sums_of_three_cubes

 Andrew Booker wrote an algorithm in March 2019 in order to find the result for number 33. Refer https://www.youtube.com/watch?v=ASoz_NuIvP0

 This code takes stab at Andrew's algorithm in a Pythonic way.



"""

import threading
import itertools
import math


value = 3
bound = 10**3
xy_list = []

xy_lock = threading.RLock

def generate_xy_combinations():
    """
    |x|, |y| <= bound
    :return: Generates all the possible integer combination for x and y
    """
    global xy_list
    data = list(range(-(bound),bound+1))
    xy_list = [p for p in itertools.product(data, repeat=2)]

    print("Length of permutation "+str(len(xy_list)))

    iLen = math.floor(len(xy_list) / 4)
    threading.Thread(target=calculate_z,args=(xy_list[0:iLen],1,)).start()
    threading.Thread(target=calculate_z, args=(xy_list[iLen:iLen+iLen], 2,)).start()
    threading.Thread(target=calculate_z, args=(xy_list[iLen + iLen:iLen + iLen + iLen], 3,)).start()
    threading.Thread(target=calculate_z, args=(xy_list[iLen + iLen +iLen:len(xy_list)], 4,)).start()

def calculate_z(xy_list,i):
    """

    :param xy_list: List of x,y tuples
    :param i: Thread index
    :return: Calculates z and prints the result if it matches with value
    """
    print("Running thread "+str(i))
    global value
    for item in xy_list:
        x, y = item
        d = x + y
        if d == 0:
            continue
        interm_val = x**2 - (x*y) + y**2
        for z in range(-(bound),bound+1):
            if (value - z**3)/d == interm_val:
                print("Result found using x= "+str(x)+" y= "+str(y)+" z= "+str(z)+" in thread "+str(i))
    print("Thread "+str(i)+" completed.")




if value % 9 == 4 or value % 9 == 5:
    print("Not possible")
    exit()

generate_xy_combinations()


