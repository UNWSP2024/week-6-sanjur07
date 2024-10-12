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