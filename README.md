# GCPal
An automation script to facilitate small business owners in tracking customers' purchase history and preferences.

## About
GCPal reads CSV files generated from the Google forms and outputs a table that shows each customer's purchased items, quantities, and percentages related to their overall purchases. 

This is an ongoing project.


## Getting Started
Please install the library tabulate if you haven't already:

```
pip install tabulate
```

## Usage
* Save the CSV file that you'd like to process in the same folder of GCPal.
* Simply execute `python main.py`.

## Roadmap
- [x] Create a simple, functional script.
- [ ] Implement frontend/UI that allows users to indicate the header info of their Google forms.
- [ ] Use the above information to dynamically generate tables.
