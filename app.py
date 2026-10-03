from flask import Flask, jsonify, request
from openfoodfacts import get_product_by_barcode
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
    return jsonify(inventory)

@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):
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

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory_item(item_id):
    data = request.get_json()

    for item in inventory:
        if item["id"] == item_id:

            if "name" in data:
                item["name"] = data["name"]

            if "brand" in data:
                item["brand"] = data["brand"]

            if "price" in data:
                item["price"] = data["price"]

            if "stock" in data:
                item["stock"] = data["stock"]

            if "barcode" in data:
                item["barcode"] = data["barcode"]

            return jsonify(item)

    return jsonify({"error": "Inventory item not found"}), 404

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_inventory_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Inventory item deleted successfully"})

    return jsonify({"error": "Inventory item not found"}), 404

@app.route("/products/<barcode>", methods=["GET"])
def get_product_from_openfoodfacts(barcode):
    product = get_product_by_barcode(barcode)


    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404
if __name__ == "__main__":
    app.run(debug=True)