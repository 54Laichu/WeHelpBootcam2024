def find_stat(stat):
    car = []
    for i, value in enumerate(stat):
        if value == 1:
            car.append(i)
    return car

def find(spaces, stat, n):
    car_can_book = find_stat(stat)
    if not car_can_book:
        return -1

    perfect_car = {}
    for car in car_can_book:
        if spaces[car] >= n:
            perfect_car[car] = spaces[car]

    if not perfect_car:
        result = -1
    else:
        result = min(perfect_car, key=perfect_car.get)
    print(result)

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2
