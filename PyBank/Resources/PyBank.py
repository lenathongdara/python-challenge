# Dependencies
import csv 

# Load the file paths 
input_file = "PyBank\Resources\budget_data.csv"
output_file = "PyBank\Resources\budget_data_output.txt"

# Write out variables 
total_months = 0 
total_revenue = 0 
past_rev = 0 
rev_change = []
months = []
greatest_inc_profits = ["",0]
greatest_dec_profits = ["",9999999999999999999]

# Convert csv into a list of dictionaries (using DictReader to read in revenue_data)
with open(input_file) as revenue_data: 
    reader = csv.DictReader(revenue_data)

    # Create a loop to go through each row into the reader (don't worry about header) 
    for row in reader:

        # Total months will add by one in each row and total revenue needs to be casted as an integer since it would have been read as a string 
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])

        # Calculate for the change in revenue 
        revchange = int(row["Revenue"]) - past_rev
        past_rev = int(row["Revenue"])
        rev_change = rev_change + [revchange]
        months = months = [row["Date"]]

            
        # If statement to calculate the greatest increase in profits
        if (revchange > greatest_inc_profits[1]):
            greatest_inc_profits[0] = row["Date"]
            greatest_inc_profits[1] = revchange
       
        # Calculate the greatest decrease in profits
        if (revchange < greatest_dec_profits[1]):
            greatest_dec_profits[0] = row["Date"]
            greatest_dec_profits[1] = revchange
    
# Make a formula to calculate the average of revenue change 
average_revenue = sum(rev_change) / len(rev_change)

# Print output 
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue: ${average_revenue}\n"
    f"Greatest Increase in Profits: {greatest_inc_profits[0]} (${greatest_inc_profits[1]})\n"
    f"Greatest Decrease in Profits: {greatest_dec_profits[0]} (${greatest_dec_profits[1]})\n"
)

print(output)

# Convert to a text file and save 
with open(output_file, "w") as txt_file:
    txt_file.write(output)

