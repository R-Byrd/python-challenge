import csv

# File paths used to read and write to
input_file = 'Resources/budget_data.csv'
output_file = 'analysis.txt'

# Initializing variables
total_months = 0
total_net_amt = 0
prev_profit_loss = 0
greatest_profit_increase = {"Date": "", "Amount": 0}
greatest_profit_decrease = {"Date": "", "Amount": 0}
profit_loss_changes_list = []

# Read the input file
with open(input_file, 'r') as file:
    csvreader = csv.DictReader(file)

    # Storing the header row
    header = csvreader.fieldnames
    
    # Loop through each row of the input file
    for row in csvreader:
        # Increase total months by 1 each loop
        total_months += 1

        # Calculate total net amount of "Profit/Losses"
        profit_loss = int(row["Profit/Losses"])
        total_net_amt += profit_loss

        # Calculate the changes in "Profit/Losses"
        profit_loss_changes = profit_loss - prev_profit_loss
        if prev_profit_loss != 0:
            profit_loss_changes_list.append(profit_loss_changes)

            # Update the greatest increase
            if profit_loss_changes > greatest_profit_increase["Amount"]:
                greatest_profit_increase["Date"] = row["Date"]
                greatest_profit_increase["Amount"] = profit_loss_changes

            # Update the greatest decrease
            if profit_loss_changes < greatest_profit_decrease["Amount"]:
                greatest_profit_decrease["Date"] = row["Date"]
                greatest_profit_decrease["Amount"] = profit_loss_changes

        # Update the profit/loss for the next loop
        prev_profit_loss = profit_loss

# Calculate the average change in profit/losses
average_profit_loss_changes = sum(profit_loss_changes_list) / len(profit_loss_changes_list)

# Formatting results to output to terminal
print(f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net_amt}
Average Change: ${average_profit_loss_changes:.2f}
Greatest Increase in Profits: {greatest_profit_increase["Date"]} (${greatest_profit_increase["Amount"]})
Greatest Decrease in Profits: {greatest_profit_decrease["Date"]} (${greatest_profit_decrease["Amount"]})""")

# Exporting the resultes to a text file
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_net_amt}\n")
    file.write(f"Average Change: ${average_profit_loss_changes:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_profit_increase['Date']} (${greatest_profit_increase['Amount']})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_profit_decrease['Date']} (${greatest_profit_decrease['Amount']})\n")