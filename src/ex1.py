from ValidationException import ValidationException

def validate_file(input_file):
    with open(input_file) as mile_file:
        next(mile_file)
        for line_num, line in enumerate(mile_file, start=2):
            print(line_num, line)
            car_id, mileage = line.split(',')
            try:
                mileage = int(mileage)
            except ValueError:
                raise ValidationException("Invalid mileage: " + str(mileage))
def ex1():
    try:
        validate_file("../files/input.txt")
    except ValidationException as ve:
        print(ve)

ex1()