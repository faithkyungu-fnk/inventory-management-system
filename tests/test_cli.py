import cli

def test_get_inventory(monkeypatch):
    class MockResponse:
        status_code = 200

        def json(self):
            return [
                    {"id": 1,
                    "name": "Organic Almond Milk"}
                    ]

    def mock_get(url):
        return MockResponse()
    
    monkeypatch.setattr(cli.requests, "get", mock_get)

    cli.get_inventory()