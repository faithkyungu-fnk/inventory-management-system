# Inventory Management System

## Description

This is a simple Inventory Management System built using Python and Flask.

It allows users to:

* View inventory
* Add inventory items
* Update inventory items
* Delete inventory items
* Search for products using OpenFoodFacts

The inventory is stored in a Python list as a mock database.

## Technologies

* Python
* Flask
* Requests
* Pytest
* OpenFoodFacts API

## How to Run

Activate the virtual environment:

```bash
source venv/bin/activate
```

Start the Flask app:

```bash
python app.py
```

In another terminal, run the CLI:

```bash
python cli.py
```

## Testing

Run the tests using:

```bash
pytest
```

Current tests:

```text
5 passed
```
