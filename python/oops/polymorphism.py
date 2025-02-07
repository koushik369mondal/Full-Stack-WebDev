class PaymentMethod:
    def make_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class CreditCardPayment(PaymentMethod):
    def make_payment(self, amount):
        return f"Paid {amount} INR using Credit Card."

class DebitCardPayment(PaymentMethod):
    def make_payment(self, amount):
        return f"Paid {amount} INR using Debit Card."

class PayPalPayment(PaymentMethod):
    def make_payment(self, amount):
        return f"Paid {amount} INR using PayPal."

# Polymorphism in action
def process_payment(payment_method, amount):
    print(payment_method.make_payment(amount))

# Using different payment methods with the same method
credit_payment = CreditCardPayment()
debit_payment = DebitCardPayment()
paypal_payment = PayPalPayment()

process_payment(credit_payment, 500)
process_payment(debit_payment, 1000)
process_payment(paypal_payment, 1500)
