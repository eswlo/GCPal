
def get_unorg_dict(purchase_list, customer_index, item_index, quantity_index):
    report = {}
    for row in purchase_list:
        customer = row[customer_index].lower() 
        item = row[item_index] 
        quantity = int(row[quantity_index])
        if customer in report:
            purchase_dict = report[customer]
            if item in purchase_dict:
                purchase_dict[item] += quantity
            else:
                purchase_dict[item] = quantity
        else:
            val_dict = {}
            val_dict[item] = quantity
            report[customer] = val_dict
    return report



def get_org_dict(unorg_dict):
    keys = ['customer', 'item', 'quantity', 'percentage (%)']
    dict_report = {key: [] for key in keys} #initialize dict for report

    for customer, purchase in unorg_dict.items():
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


def get_row_index(unorg_dict):
    i = 0
    rowId = []
    if len(unorg_dict) != 0:
        while i < len(unorg_dict["customer"]):
            j = i+1
            id = str(j)
            rowId.append(id)
            i+=1
    return rowId
