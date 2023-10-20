import tkinter as tk
from tkinter import messagebox

# Sample product data (you can replace this with your actual product data)
products = {
    "Product 1": {"price": 10.0},
    "Product 2": {"price": 15.0},
    "Product 3": {"price": 20.0},
}

class StoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Store App")

        self.cart = {}
        self.total_cost = 0.0

        # Create product list frame
        self.product_frame = tk.Frame(root)
        self.product_frame.pack()

        for product, details in products.items():
            product_label = tk.Label(self.product_frame, text=f"{product} - ${details['price']:.2f}")
            product_label.pack()

            add_button = tk.Button(self.product_frame, text="Add to Cart", command=lambda p=product: self.add_to_cart(p))
            add_button.pack()

        # Create cart frame
        self.cart_frame = tk.Frame(root)
        self.cart_frame.pack()

        self.cart_label = tk.Label(self.cart_frame, text="Shopping Cart:")
        self.cart_label.pack()

        self.cart_display = tk.Label(self.cart_frame, text="")
        self.cart_display.pack()

        # Create buttons
        self.calculate_button = tk.Button(root, text="Calculate Total Cost", command=self.calculate_total_cost)
        self.calculate_button.pack()

        self.checkout_button = tk.Button(root, text="Checkout", command=self.checkout)
        self.checkout_button.pack()

    def add_to_cart(self, product):
        if product in self.cart:
            self.cart[product] += 1
        else:
            self.cart[product] = 1
        self.update_cart_display()

    def update_cart_display(self):
        cart_items = [f"{product} x{quantity}" for product, quantity in self.cart.items()]
        self.cart_display.config(text="\n".join(cart_items))

    def calculate_total_cost(self):
        self.total_cost = sum(products[product]["price"] * quantity for product, quantity in self.cart.items())
        messagebox.showinfo("Total Cost", f"Total Cost: ${self.total_cost:.2f}")

    def checkout(self):
        # Here, you can implement the logic for placing orders and delivery options
        # For this example, we will reset the cart and display a message
        self.cart = {}
        self.update_cart_display()
        messagebox.showinfo("Checkout", "Order placed successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = StoreApp(root)
    root.mainloop()
