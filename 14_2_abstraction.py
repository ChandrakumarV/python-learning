
# 1. Without abstraction
# Imagine you have two payment methods.
from abc import ABC, abstractmethod


class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Card:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


upi = UPI()
upi.pay(500)

card = Card()
card.pay(1000)


# 2. With abstraction


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}")


class Card(Payment):
    def pay(self, amount):
        print(f"Processing Card payment of ₹{amount}")


def checkout(payment_method, amount):
    payment_method.pay(amount)


checkout(UPI(), 500)
checkout(Card(), 1000)

# Where exactly is abstraction happening?
# Look at this function: checkout()

# The checkout() function doesn't need to know how UPI or card payments work internally.
# - UPI might communicate with a payment API.
# - Card might communicate with a banking gateway.
# - checkout() only needs to know that the object provides a pay() method.

# This does two things:
# 1. Defines a contract: Every concrete child class must implement pay().
# 2. Supports abstraction: Code that uses Payment can rely on a common interface without depending on each payment method's internal details
