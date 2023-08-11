# business_logic.py
from db_connection import get_connection

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        # Database logic to register a user
        pass

    def login(self):
        # Database logic to login a user
        pass

class ProductManager(User):
    def manage_stocks(self, product_id, quantity):
        # Logic to manage stocks
        pass

    def view_stocks(self):
        # Logic to view all stocks
        pass

class Customer(User):
    _balance = 0  # private variable

    def __init__(self, username, password, balance):
        super().__init__(username, password)
        self._balance = balance

    def purchase_stock(self, product_id, quantity):
        # Logic to purchase stock
        pass

    def view_orders(self):
        # Logic to view all orders
        pass
