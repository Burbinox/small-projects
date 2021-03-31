def change_data_format_to_lists_of_list(triangle):
    for floor in range(len(triangle)):
        new_format = []
        for numbers_in_floor in triangle[floor]:
            new_format.append(int(numbers_in_floor))
        triangle[floor] = new_format
    return triangle


def find_the_shortest_path(triangle):
    triangle.reverse()
    print(triangle)
    print()
    shortest_path = []
    for floor in range(len(triangle)):  # floor indexes
        if floor + 1 == len(triangle):
            break
        for elem in range(len(triangle[floor + 1])):  # elements in before the last one floor
            if floor == 0:
                path = str(min(triangle[floor][elem], triangle[floor][elem + 1])) + str(triangle[floor + 1][elem])
                shortest_path.append(path)
                path = 0
            else:
                first_elem = triangle[floor][elem]
                second_elem = triangle[floor][elem + 1]
                if first_elem < second_elem:
                    shortest_path[elem] = str(shortest_path[elem]) + str(triangle[floor + 1][elem])
                else:
                    shortest_path[elem] = str(shortest_path[elem + 1]) + str(triangle[floor + 1][elem])
            triangle[floor + 1][elem] = triangle[floor + 1][elem] + min(triangle[floor][elem],
                                                                        triangle[floor][elem + 1])
    print("the shortest path is: " + shortest_path[0][::-1])
    triangle.reverse()
    print("the sum of the shortest path is: " + str(triangle[0][0]))


with open('a68617c92920fe68c777d389e25e7d4b/3-medium.txt') as f:
    tri = f.readlines()
    tri = [elem.strip() for elem in tri]
    tri = [elem.replace(" ", "") for elem in tri]

    new_tri = change_data_format_to_lists_of_list(tri)
    find_the_shortest_path(new_tri)
