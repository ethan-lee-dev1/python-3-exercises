import csv
def find_total_visits():
    result = 0
    filenames = ["../files/week-1.csv", "../files/week-2.csv", "../files/week-3.csv"]
    for filename in filenames:
        with open(filename, "r") as file:
            next(file)
            lines = csv.reader(file, delimiter=',')
            for line in lines:
                print(line)
                for value in line[1:]:
                    if int(value) == 1:
                        result += 1
    return result



def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()