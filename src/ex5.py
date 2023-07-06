from pprint import pprint
import csv

def build_car_list():
    mileages = {}
    car_id = {}
    with open("../files/input.txt") as mile_file:
        next(mile_file)
        lines = csv.reader(mile_file, delimiter=',')
        for line in lines:
            mileages[line[0]] = line[1]

    with open("../files/car-ids.txt") as car_id_file:
        lines = csv.reader(car_id_file, delimiter=',')
        for line in lines:
            car_id[line[0]] = line[1]
    result = []
    # print(mileages)
    # print(car_id)
    for mileage_id in mileages:
        # print(mileage_id)
        try:
            result.append({'id': mileage_id, 'miles': int(mileages[mileage_id]), 'model': car_id[mileage_id]})
        except ValueError:
            continue
    return result
def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
