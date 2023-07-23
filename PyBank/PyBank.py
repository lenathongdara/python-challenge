import csv
import os

input_file = "PyBank/Resources/budget_data.csv"
output_file = "PyBank/Analysis/budget_data_output.txt"

# Assign values to variables
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

with open(input_file) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    # Create a loop and that calculates variables in each row 
    for row in reader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

avg_change = sum(net_change_list) / len(net_change_list)

final_summary = (
    f"Financial Analysis\n"
    f"\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_change :.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

print(final_summary)

with open(output_file, "w") as txt_file:
    txt_file.write(final_summary)
