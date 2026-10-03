from flask import Flask, jsonify

app = Flask(__name__)


# Mock inventory database
inventory = [
    {
        "id": 1,
        "name": "Organic Almond Milk",
        "brand": "Silk",
        "price": 350,
        "stock": 20,
        "barcode": "1234567890123"
    },
    {
        "id": 2,
        "name": "Whole Wheat Bread",
        "brand": "Bakers",
        "price": 80,
        "stock": 15,
        "barcode": "2345678901234"
    },
    {
        "id": 3,
        "name": "Corn Flakes",
        "brand": "Kellogg's",
        "price": 450,
        "stock": 10,
        "barcode": "3456789012345"
    }
]


@app.route("/")
def home():
    return "Inventory Management System"


@app.route("/inventory", methods=["GET"])
def get_inventory():
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error":"Inventory item not found"}), 404

@app.route("/inventory", methods=["POST"])
def add_inventory_item():
    data = request.get_json()

    new_id = len(inventory) + 1

    new_item = {
        "id": new_id,
        "name": data["name"],
        "brand": data["brand"],
        "price": data["price"],
        "stock": data["stock"],
        "barcode": data["barcode"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

if __name__ == "__main__":
    app.run(debug=True)