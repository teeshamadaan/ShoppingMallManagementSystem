import datetime

class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print(f"{self.id}. {self.name} - ${self.price} - Stock: {self.stock}")

class ShoppingMall:
    def __init__(self):
        self.products = []
        self.cart = []

    def load_products(self):
        try:
            with open("products.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    id, name, price, stock = line.strip().split(",")
                    self.products.append(Product(int(id), name, float(price), int(stock)))
        except FileNotFoundError:
            print("No products file found.")

    def save_products(self):
        with open("products.txt", "w") as file:
            for p in self.products:
                file.write(f"{p.id},{p.name},{p.price},{p.stock}\n")

    def display_products(self):
        print("\nAvailable Products:")
        for p in self.products:
            p.display()

    def add_to_cart(self, id, qty):
        for p in self.products:
            if p.id == id and p.stock >= qty:
                p.stock -= qty
                self.cart.append((p, qty))
                print(f"Added {qty} x {p.name} to cart.")
                return
        print("Invalid product ID or insufficient stock.")

    def generate_bill(self):
        total = 0
        print("\n----- BILL -----")
        for item, qty in self.cart:
            cost = item.price * qty
            print(f"{item.name} x {qty} = ${cost}")
            total += cost
        print(f"Total Amount: ${total}")

        with open("transactions.txt", "a") as file:
            file.write(f"\nDate: {datetime.datetime.now()}\n")
            for item, qty in self.cart:
                file.write(f"{item.name} x {qty} = ${item.price * qty}\n")
            file.write(f"Total: ${total}\n---------------------\n")

        self.cart.clear()

def main():
    mall = ShoppingMall()
    mall.load_products()

    while True:
        print("\n1. Show Products\n2. Add to Cart\n3. Generate Bill\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            mall.display_products()
        elif choice == '2':
            mall.display_products()
            try:
                id = int(input("Enter Product ID: "))
                qty = int(input("Enter Quantity: "))
                mall.add_to_cart(id, qty)
            except ValueError:
                print("Invalid input.")
        elif choice == '3':
            mall.generate_bill()
            mall.save_products()
        elif choice == '4':
            mall.save_products()
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
