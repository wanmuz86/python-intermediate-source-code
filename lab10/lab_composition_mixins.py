# Utility class (Logging class) - as Mixin
# Log before and after checkout
class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")

# Display utility class
# display class information and attributes
class DisplayMixin:
    def display(self):
        attrs = vars(self)
        return f"{self.__class__.__name__}({attrs})"


class Payment:   # This could be an abstract class
    def pay(self, amount):
        raise NotImplementedError


class CardPayment(Payment):
    def pay(self, amount):
        print(f"[CARD] Paid {amount}")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"[CASH] Paid {amount}")


# Order now implement LoggingMixin and DisplayMixin
# Inheritence will always be on the left
# Mixins...
class Order(LoggingMixin, DisplayMixin):
    def __init__(self, order_id, total, payment_method):
        self.order_id = order_id
        self.total = total
        # OOP principle -> loosely coupled -> Payment can be extended to Cash, Card .....
        self.payment_method = payment_method  # composition / one to one

    def checkout(self):
        self.log(f"Checkout started: {self.order_id}")
        self.payment_method.pay(self.total)
        self.log(f"Checkout completed: {self.order_id}")


def test_inheritance_version():
    order1 = Order("O200", 80, CardPayment())
    order2 = Order("O201", 30, CashPayment())

    order1.checkout()
    order2.checkout()
    print(order1.display())
    print(order2.display())
    print(Order.__mro__)

test_inheritance_version()


