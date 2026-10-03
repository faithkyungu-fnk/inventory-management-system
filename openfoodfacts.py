import requests


def get_product_by_barcode(barcode):
    url = f"https://world.openfoodfacts.org/api/v3/product/{barcode}"

    headers = {
        "User-Agent": "InventoryManagementSystem/1.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if data.get("status") == "success":
            product = data.get("product", {})

            return {
                "name": product.get("product_name"),
                "brand": product.get("brands"),
                "barcode": barcode,
                "quantity": product.get("product_quantity"),
                "quantity_unit": product.get("product_quantity_unit"),
                "image": product.get("image_url")
            }

    return None