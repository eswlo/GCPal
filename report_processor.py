
def get_customer_dict(purchase_list, purchase_header):
    report = {}
    for row in purchase_list:
        row_length = len(row)
        if get_sum(row, row_length) != 0:
            customer = row[1].lower()
            i = 2 
            if customer not in report:
                purchase_dict = {}
                while i < row_length:
                    item = purchase_header[i]
                    quantity = 0 
                    if row[i] != "":
                        quantity = int(row[i])
                    purchase_dict[item] = quantity
                    i+=1
                report[customer] = purchase_dict
            else:
                purchase_dict = report[customer]
                while i < row_length:
                    item = purchase_header[i]
                    quantity = 0 
                    if row[i] != "":
                        quantity = int(row[i])
                    purchase_dict[item] += quantity
                    i+=1
    return report


def get_sum(row, row_length):
    i = 2
    total_sum  = 0
    while i < row_length:
        count = 0
        if row[i] != "":
            count = int(row[i])
        total_sum  += count
        i+=1
    return total_sum 


def get_report_dict(input_dict):
    keys = ['customer', 'item', 'quantity', 'percentage (%)']
    dict_report = {key: [] for key in keys} #initialize dict for report

    for customer, purchase in input_dict.items():
        # get total count of purchased items
        sum = 0
        for item, quantity in purchase.items():
            sum += quantity

        # generate organized dict for report table    
        i = 0
        for item, quantity in purchase.items():
            percentage = (quantity / sum) * 100
            if i == 0:
                dict_report['customer'].append(customer)
            else:
                dict_report['customer'].append("")
            dict_report['item'].append(item)
            dict_report['quantity'].append(quantity)
            dict_report['percentage (%)'].append(percentage)
            i+=1
    return dict_report


def get_row_index(input_dict):
    i = 0
    rowId = []
    if len(input_dict) != 0:
        while i < len(input_dict["customer"]):
            j = i+1
            id = str(j)
            rowId.append(id)
            i+=1
    return rowId
