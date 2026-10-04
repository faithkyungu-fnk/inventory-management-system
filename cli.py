import requests
BASE_URL= "http://127.0.0.1:5000"

def get_inventory():
    response = requests.get(f"{BASE_URL}/inventory")
    print("\nInventory:")
    print(response.json())

def get_inventory_item(item_id):
    response = requests.get(f"{BASE_URL}/inventory/{item_id}")
    print(f"\nInventory Item {item_id}:")
    print(response.json())    

def add_inventory_item():
    name = input("Enter product name: ")
    brand = input("Enter brand: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock: "))
    barcode = input("Enter barcode: ")

    item = {"name": name,
        "brand": brand,
        "price": price,
        "stock": stock,
        "barcode": barcode
    }
    response = requests.post(f"{BASE_URL}/inventory", json=item)
    print(f"\nAdded Inventory Item:")
    print(response.json())

def update_inventory_item(item_id):
    price = float(input("Enter new price: "))
    stock = int(input("Enter new stock: "))

    update_data = {"price": price, "stock": stock}
    response = requests.patch(f"{BASE_URL}/inventory/{item_id}", json=update_data
  )   
    print(f"\nUpdated Inventory Item {item_id}:")
    print(response.json())

def delete_inventory_item(item_id):
    response = requests.delete(f"{BASE_URL}/inventory/{item_id}")
    print(f"\nDeleted Inventory Item {item_id}:")
    print(response.json())

#   lets cli look up a product by barcode
def get_product_from_openfoodfacts(barcode):
    response = requests.get(f"{BASE_URL}/products/{barcode}")
    print(f"\nOpenFoodFacts Product {barcode}:")
    print(response.json())

if __name__ == "__main__":
    while True:
        print("\nInventory Management System")
        print("1. View all inventory")
        print("2. View one inventory item")
        print("3. Add inventory item")
        print("4. Update inventory item")
        print("5. Delete inventory item")
        print("6. Search OpenFoodFacts")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            get_inventory()

        elif choice == "2":
            item_id = int(input("Enter inventory item ID: "))
            get_inventory_item(item_id)

        elif choice == "3":
            add_inventory_item()

        elif choice == "4":
            item_id = int(input("Enter inventory item ID: "))
            update_inventory_item(item_id)

        elif choice == "5":
            item_id = int(input("Enter inventory item ID: "))
            delete_inventory_item(item_id)

        elif choice == "6":
            barcode = input("Enter product barcode: ")
            get_product_from_openfoodfacts(barcode)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
