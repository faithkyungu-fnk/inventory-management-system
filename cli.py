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
    item = {"name": "Orange Juice",
        "brand": "Minute Maid",
        "price": 200,
        "stock": 10,
        "barcode": "5678901234567"
    }
    response = requests.post(f"{BASE_URL}/inventory", json=item)
    print(f"\nAdded Inventory Item:")
    print(response.json())

        
if __name__ == "__main__":
    get_inventory()
    get_inventory_item(1)
    add_inventory_item()