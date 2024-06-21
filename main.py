import os
from gc_parcer import get_data
from report_processor import get_unorg_dict, get_org_dict, get_row_index
from tabulate import tabulate

customer_index = 1
item_index = 2
quantity_index = 3
instruction = "Enter the name of the csv file stored in the folder, or press enter to quit: "
output_html_table = "table_of_orders.html"

if __name__ == '__main__':
    filename = input(instruction)
    while len(filename) != 0:
        csv_file = filename + ".csv"
        if os.path.exists(csv_file): #check if the entered csv file exists
            purchase_list = get_data(csv_file)
            purchase_dict_unorg = get_unorg_dict(purchase_list, customer_index, item_index, quantity_index)
            purchase_dict_org = get_org_dict(purchase_dict_unorg)
            rowID = get_row_index(purchase_dict_org)

            # format the organized purchase dict into tabular data  
            table = tabulate(purchase_dict_org, headers="keys", tablefmt="fancy_grid", showindex=rowID)
            
            # extract html code from the tabular data
            table_html = tabulate(purchase_dict_org, headers="keys", tablefmt="html", showindex=rowID)

            # print the table to console
            print(table)
            
            # write the table html to file
            with open(output_html_table, 'w') as f:
                f.write(table_html)
                # f.close
            
            # continue to the next file to be processed
            filename = input(instruction)
        else:
            print("No file was found in the folder.")
            filename = input(instruction)
    else:
        print("Goodbye!")

    
