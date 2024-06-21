import csv

def get_data(file_name):
    ret_list = []
    ret_header = []
    with open(file_name, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in data:
            if i == 0:
                ret_header = row
                i+=1
            else:
                ret_list.append(row)
    return [ret_list, ret_header]







