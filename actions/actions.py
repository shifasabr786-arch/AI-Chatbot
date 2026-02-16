from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import json
from datetime import datetime, timedelta 
import random

class ActionEcommerceOrderLookup(Action):
    """Action to look up ecommerce order status"""
    
    def name(self) -> Text:
        return "action_ecommerce_order_lookup"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        order_number = tracker.get_slot("order_number")
        
        if not order_number:
            dispatcher.utter_message(text="I need an order number to check the status. Please provide your order number.")
            return []
        
        # Simulate order lookup (in real implementation, this would query a database)
        order_statuses = ["Processing", "Shipped", "In Transit", "Out for Delivery", "Delivered"]
        estimated_delivery = (datetime.now() + timedelta(days=random.randint(1, 7))).strftime("%Y-%m-%d")
        
        # Mock order data
        order_data = {
            "order_number": order_number,
            "status": random.choice(order_statuses),
            "estimated_delivery": estimated_delivery,
            "tracking_number": f"TRK{random.randint(100000, 999999)}",
            "items": ["Product A", "Product B"],
            "total_amount": f"${random.randint(50, 500)}.00"
        }
        
        response = f"""
Order Details for #{order_data['order_number']}:
• Status: {order_data['status']}
• Estimated Delivery: {order_data['estimated_delivery']}
• Tracking Number: {order_data['tracking_number']}
• Items: {', '.join(order_data['items'])}
• Total Amount: {order_data['total_amount']}
        """
        
        dispatcher.utter_message(text=response)
        return [SlotSet("order_number", order_number)]

class ActionEcommerceProductSearch(Action):
    """Action to search for product information"""
    
    def name(self) -> Text:
        return "action_ecommerce_product_search"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        product_name = tracker.get_slot("product_name")
        
        if not product_name:
            dispatcher.utter_message(text="I need to know which product you're asking about. Please specify the product name.")
            return []
        
        # Simulate product search (in real implementation, this would query a product database)
        mock_products = {
            "laptop": {
                "name": "Gaming Laptop Pro",
                "price": "$1,299.99",
                "description": "High-performance gaming laptop with RTX graphics",
                "availability": "In Stock",
                "rating": "4.5/5"
            },
            "smartphone": {
                "name": "SmartPhone X",
                "price": "$899.99",
                "description": "Latest smartphone with advanced camera system",
                "availability": "In Stock",
                "rating": "4.7/5"
            },
            "headphones": {
                "name": "Wireless Headphones Pro",
                "price": "$199.99",
                "description": "Noise-cancelling wireless headphones",
                "availability": "In Stock",
                "rating": "4.3/5"
            },
            "tablet": {
                "name": "Tablet Pro 12",
                "price": "$599.99",
                "description": "Professional tablet for work and creativity",
                "availability": "Limited Stock",
                "rating": "4.6/5"
            }
        }
        
        product_key = product_name.lower()
        if product_key in mock_products:
            product = mock_products[product_key]
            response = f"""
Product Information:
• Name: {product['name']}
• Price: {product['price']}
• Description: {product['description']}
• Availability: {product['availability']}
• Rating: {product['rating']}
            """
        else:
            response = f"I found some information about '{product_name}':\n• Price: ${random.randint(50, 1000)}.99\n• Availability: In Stock\n• Rating: {random.uniform(3.5, 5.0):.1f}/5"
        
        dispatcher.utter_message(text=response)
        return [SlotSet("product_name", product_name)]

class ActionBankingBalanceCheck(Action):
    """Action to check banking account balance"""
    
    def name(self) -> Text:
        return "action_banking_balance_check"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        account_number = tracker.get_slot("account_number")
        
        if not account_number:
            dispatcher.utter_message(text="For security purposes, I need your account number to check the balance. Please provide your account number.")
            return []
        
        # Simulate balance check (in real implementation, this would query a secure banking system)
        mock_balances = {
            "123456": {"balance": "$2,547.89", "account_type": "Checking"},
            "789012": {"balance": "$15,230.45", "account_type": "Savings"},
            "345678": {"balance": "$8,901.23", "account_type": "Checking"}
        }
        
        if account_number in mock_balances:
            account_info = mock_balances[account_number]
            response = f"""
Account Balance for #{account_number}:
• Account Type: {account_info['account_type']}
• Current Balance: {account_info['balance']}
• Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
            """
        else:
            # Generate a random balance for unknown accounts
            balance = f"${random.randint(100, 50000)}.{random.randint(10, 99)}"
            response = f"""
Account Balance for #{account_number}:
• Current Balance: {balance}
• Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
            """
        
        dispatcher.utter_message(text=response)
        return [SlotSet("account_number", account_number)]

class ActionBankingTransfer(Action):
    """Action to process banking money transfer"""
    
    def name(self) -> Text:
        return "action_banking_transfer"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        amount = tracker.get_slot("amount")
        
        if not amount:
            dispatcher.utter_message(text="I need to know the amount you want to transfer. Please specify the amount.")
            return []
        
        # Simulate transfer processing
        transfer_id = f"TXN{random.randint(100000, 999999)}"
        response = f"""
Transfer Request Processed:
• Transfer ID: {transfer_id}
• Amount: ${amount}
• Status: Pending
• Estimated Processing Time: 1-2 business days
• You will receive a confirmation email shortly.

Note: For security, please verify the recipient details before confirming the transfer.
            """
        
        dispatcher.utter_message(text=response)
        return [SlotSet("amount", amount)]

class ActionDefaultFallback(Action):
    """Action to handle fallback scenarios"""
    
    def name(self) -> Text:
        return "action_default_fallback"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="I'm sorry, I didn't understand that. Could you please rephrase your question? I can help you with ecommerce or banking inquiries.")
        return []
