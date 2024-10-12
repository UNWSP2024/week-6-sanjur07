STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

def calculate_sales_tax(total_sales):
    county_sales_tax = total_sales * COUNTY_TAX_RATE
    state_sales_tax = total_sales * STATE_TAX_RATE
    total_sales_tax = county_sales_tax + state_sales_tax
    return county_sales_tax, state_sales_tax, total_sales_tax

def main():
    total_sales = float(input("Enter the total sales for the month: $"))
    county_tax, state_tax, total_tax = calculate_sales_tax(total_sales)

    print(f"County sales tax: ${county_tax:.2f}")
    print(f"State sales tax: ${state_tax:.2f}")
    print(f"Total sales tax: ${total_tax:.2f}")

# Call the main function
if __name__ == "__main__":
    main()

"""START

DECLARE CONSTANTS:
    STATE_TAX_RATE = 0.05  // 5% state tax
    COUNTY_TAX_RATE = 0.025  // 2.5% county tax

FUNCTION calculate_sales_tax(total_sales):
    CALCULATE county_sales_tax = total_sales * COUNTY_TAX_RATE
    CALCULATE state_sales_tax = total_sales * STATE_TAX_RATE
    CALCULATE total_sales_tax = county_sales_tax + state_sales_tax
    RETURN county_sales_tax, state_sales_tax, total_sales_tax
END FUNCTION

MAIN FUNCTION:
    PROMPT user to enter the total sales for the month
    READ total_sales

    CALL calculate_sales_tax(total_sales) and STORE results in county_tax, state_tax, total_tax

    DISPLAY "County sales tax: $", county_tax
    DISPLAY "State sales tax: $", state_tax
    DISPLAY "Total sales tax: $", total_tax
END MAIN FUNCTION

CALL MAIN FUNCTION

END"""