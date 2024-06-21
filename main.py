import os
from gc_parcer import get_data
from report_processor import get_report_dict, get_row_index, get_customer_dict
from tabulate import tabulate

instruction = "Enter the name of the csv file stored in the folder, or press enter to quit: "
header = []

if __name__ == '__main__':
    filename = input(instruction)
    while len(filename) != 0:
        csv_file = filename + ".csv"
        if os.path.exists(csv_file): #check if the entered csv file exists
            purchase_data = get_data(csv_file)
            purchase_list = purchase_data[0]
            purchase_header = purchase_data[1]

            customer_dict = get_customer_dict(purchase_list, purchase_header)
            report_dict = get_report_dict(customer_dict)
            rowID = get_row_index(report_dict)

            # format the organized purchase dict into tabular data  
            table = tabulate(report_dict, headers="keys", tablefmt="fancy_grid", showindex=rowID)
            
            # extract html code from the tabular data
            table_html = tabulate(report_dict, headers="keys", tablefmt="html", showindex=rowID)

            # print the table to console
            print(table)
            
            # write the table html to file
            output_html_table = "table_of_" + filename + ".html"
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

    
