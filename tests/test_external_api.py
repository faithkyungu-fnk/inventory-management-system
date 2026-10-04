import openfoodfacts


def test_get_product_by_barcode(monkeypatch):
    class MockResponse:
        status_code = 200

        def json(self):
            return {
                "status": "success",
                "product": {
                    "product_name": "Nutella",
                    "brands": "Ferrero",
                    "product_quantity": "350",
                    "product_quantity_unit": "g",
                    "image_url": "https://example.com/nutella.jpg"
                }
            }

    def mock_get(url, headers):
        return MockResponse()

    monkeypatch.setattr(openfoodfacts.requests, "get", mock_get)

    product = openfoodfacts.get_product_by_barcode("3017620422003")

    assert product["name"] == "Nutella"
    assert product["brand"] == "Ferrero"
    assert product["barcode"] == "3017620422003"