from gc_parcer import get_data
from report_processor import get_raw_report, make_report_table
from tabulate import tabulate



if __name__ == '__main__':
    customer_index = 1
    item_index = 2
    quantity_index = 3
    csv_file = 'Ordering Inventory.csv'

    purchase_list = get_data(csv_file)
    raw_report = get_raw_report(purchase_list, customer_index, item_index, quantity_index)
    final_report = make_report_table(raw_report)
    print(tabulate(final_report, headers="keys", tablefmt="fancy_grid", showindex=True))
