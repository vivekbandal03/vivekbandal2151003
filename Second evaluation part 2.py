import datetime

# Initialize sales and customer data
sales_data = []
customer_data = {}

def record_sale(customer_name, items_purchased, total_amount):
    timestamp = datetime.datetime.now()
    sale = {
        'timestamp': timestamp,
        'customer_name': customer_name,
        'items_purchased': items_purchased,
        'total_amount': total_amount
    }
    sales_data.append(sale)

    # Update customer data
    if customer_name in customer_data:
        customer_data[customer_name]['total_purchases'] += 1
        customer_data[customer_name]['total_amount'] += total_amount
    else:
        customer_data[customer_name] = {
            'total_purchases': 1,
            'total_amount': total_amount
        }

    print("Sale recorded successfully.")

def calculate_total_sales(start_date, end_date):
    total_sales = sum(sale['total_amount'] for sale in sales_data if start_date <= sale['timestamp'] <= end_date)
    return total_sales

def provide_discount(customer_name):
    if customer_name in customer_data and customer_data[customer_name]['total_purchases'] >= 5:
        discount = 0.1  # 10% discount for frequent customers
        print(f"{customer_name} is eligible for a {discount*100}% discount on the next purchase.")
    else:
        print(f"{customer_name} is not eligible for a discount at this time.")

def generate_top_customers_report():
    if not customer_data:
        print("No customer data available.")
    else:
        print("Top Customers:")
        sorted_customers = sorted(customer_data.items(), key=lambda x: x[1]['total_amount'], reverse=True)
        for i, (customer, data) in enumerate(sorted_customers, start=1):
            print(f"{i}. {customer} - Total Purchases: {data['total_purchases']}, Total Amount: ${data['total_amount']}")

while True:
    print("\nOptions:")
    print("1. Record a sale")
    print("2. Calculate total sales for a period")
    print("3. Provide a discount")
    print("4. Generate top customers report")
    print("5. Exit")
    
    choice = input("Select an option (1/2/3/4/5): ")
    
    if choice == '1':
        customer_name = input("Enter customer name: ")
        items_purchased = input("Enter items purchased (comma-separated): ").split(',')
        total_amount = float(input("Enter total amount: $"))
        record_sale(customer_name, items_purchased, total_amount)
    elif choice == '2':
        start_date = datetime.datetime.fromisoformat(input("Enter start date (YYYY-MM-DD): "))
        end_date = datetime.datetime.fromisoformat(input("Enter end date (YYYY-MM-DD): "))
        total_sales = calculate_total_sales(start_date, end_date)
        print(f"Total sales for the period: ${total_sales:.2f}")
    elif choice == '3':
        customer_name = input("Enter customer name: ")
        provide_discount(customer_name)
    elif choice == '4':
        generate_top_customers_report()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
