#Natalie Gardner
#10-28-2024

#The program must display all monetary values to two decimal places and use loops and conditional statements. 
# Grading criteria include creating a flowchart, documentation, correct use of loops and conditionals, accurate output, and program functionality​



def cash_register():
    # Constants
    TAX_RATE = 0.07
    
    # Initialize totals
    total_cost = 0.0
    total_tax = 0.0
    num_items = 0
    
    # Loop to allow multiple items
    while True:
        # Input item cost
        cost = float(input("Enter the cost of the item: $"))
        num_items += 1
        
        # Check if item is taxable
        taxable = input("Is this item taxable? (yes/no): ").strip().lower()
        if taxable == 'yes':
            tax = cost * TAX_RATE
            total_tax += tax
        else:
            tax = 0.0
        
        # Update total cost
        total_cost += (cost + tax)
        
        # Display item cost with tax
        print(f"Item Cost with Tax: ${cost + tax:.2f}")
        
        # Check if user wants to add another item
        another_item = input("Would you like to add another item? (y/n): ").strip().lower()
        if another_item != 'y':
            break
    
    # Display totals
    print("\n--- Checkout Summary ---")
    print(f"Total Items: {num_items}")
    print(f"Subtotal: ${total_cost - total_tax:.2f}")
    print(f"Total Tax: ${total_tax:.2f}")
    print(f"Total Cost (with tax): ${total_cost:.2f}")
    
    # Prompt for amount tendered and calculate change
    while True:
        amount_tendered = float(input("Enter amount tendered: $"))
        if amount_tendered >= total_cost:
            change_due = amount_tendered - total_cost
            print(f"Change Due: ${change_due:.2f}")
            break
        else:
            print("Insufficient funds. Please enter a higher amount.")
    
# Run the cash register program
cash_register()
