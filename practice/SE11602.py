#Natalie Gardner
#October 13 2024
#Create a Net Pay Calculator program that takes a user’s hourly pay ($14.50), hours worked (32 hours per week), and a tax rate (20%). The program should calculate and display the gross pay, the amount deducted for taxes, and the net pay for a two-week period. Store the results in descriptive variables and ensure the output is labeled and rounded to two decimal places

    # Input: Get user inputs
HRpay= float(14.5)
HRworked = float(32)
Taxrate = float(20) / 100  # Convert to decimal



    # Calculate for two weeks
HRworked = HRworked * 2
Calcgrosspay = HRpay * HRworked
Calctax = Calcgrosspay * Taxrate
Calcnetpay = Calcgrosspay - Calctax

    # Output: Display results formatted as currency
print(f"\nGross Pay: ${Calcgrosspay:.2f}")
print(f"Taxes Deducted: ${Calctax:.2f}")
print(f"Net Pay: ${Calcnetpay:.2f}")
print(f"\nHave a good day")


