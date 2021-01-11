from django.dispatch import Signal

pizza_done = Signal(providing_args=["toppings", "size"])

class Pizza:
    def mark_as_done(self, toppings, size):
        pizza_done.send(sender=self.__class__, toppings=toppings, size=size)