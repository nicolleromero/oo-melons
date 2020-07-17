"""Classes for melon orders."""
import random


class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_base_price(self):
        """Choose a random integer between 5-9 as the base price"""
        base_price = random.choice(range(5, 10))

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == 'Christmas melon':
            base_price = (base_price * 1.5)

        if self.qty < 10 and self.order_type == 'international':
            total = 3 + (1 + self.tax) * self.qty * base_price

        else:
            total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, 'domestic', 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, 'international', 0.17)
        self.country_code = country_code

    def get_country_code(self):

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty, country_code,):
        super().__init__(species, qty, 'government', 0.0)
        self.passed_inspection = False

    def mark_inspection(self, passed):

        self.passed_inspection = passed


test1 = DomesticMelonOrder('watermelon', 3)
order0 = InternationalMelonOrder("watermelon", 6, "AUS")
order2 = GovernmentMelonOrder("watermelon", 6, "AUS")
print(order2.get_total())
