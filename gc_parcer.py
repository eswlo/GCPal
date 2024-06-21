import csv

def get_data(file_name):
    ret = []
    with open(file_name, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data) #skip the first row
        for row in data:
            ret.append(row)
    return ret







