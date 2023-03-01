# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    max_height = 0
    heights = numpy.zeros(n, int)

    for i in range(n):
        if parents[i] == -1:
            heights[i] = 1
        elif heights[parents[i]] != 0:
            heights[i] = heights[parents[i]] + 1
        else:
            parent = parents[i]
            cur_max_height = 1

            while parent != -1:
                cur_max_height += 1
                parent = parents[parent]

            parent = parents[i]
            heights[i] = cur_max_height
            
            for j in range(cur_max_height - 1):
                heights[parent] = cur_max_height - 1 - j
                parent = parents[parent]

    max_height = numpy.amax(heights)

    return max_height


def main():
    input_type = input()

    if input_type.upper()[0] == "I":
        # Input I
        count_input = input()
        parent_input = input()

        try:
            parents = numpy.array(list(map(int, parent_input.split())))
            count = int(count_input)
        except:
            print("Wrong input")
        else:
            if parents.size == count:
                print(compute_height(count, parents))
            else:
                print("Number of nodes isn't matching")

    elif input_type.upper()[0] == "F":
        # Input F
        file_input = input()
        
        try:
            file = open("test/" + file_input[:2], "r")
        except:
            print("File not found")
        else:
            count = int(file.readline())
            parents = numpy.array(list(map(int, file.readline().split())))

            print(compute_height(count, parents))

            file.close()
    else:
        print("Wrong input")



# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
