
def get_raw_report(purchase_list, customer_index, item_index, quantity_index):
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



def make_report_table(raw_report):
    keys = ['customer', 'item', 'quantity', 'percentage (%)']
    dict_report = {key: [] for key in keys} #initialize dict for report

    for customer, purchase in raw_report.items():
        # get total count of purchased items
        sum = 0
        for item, quantity in purchase.items():
            sum += quantity

        # generate dict for report table    
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


