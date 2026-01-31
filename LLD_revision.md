# LLD

Here’s a focused OOP + design‑pattern revision tailored for Amazon SDE‑1 India, with crisp examples you can code in 10–15 minutes each.

---

## Core OOP pillars (must revise)

Know definitions, 1–2 lines of use‑case, and 1‑2 examples for each.

* **Encapsulation**: Bundle data + methods, hide internals using access modifiers.
Example: `class BankAccount: def __init__(self): self.__balance = 0` – caller cannot directly set `__balance`.
* **Abstraction**: Expose only what client needs via interfaces/abstract classes.
Example: `PaymentMethod` abstract base class with `pay()`; implementations: `UPIPayment`, `CardPayment`. Client only knows `PaymentMethod`.
* **Inheritance**: Reuse and specialize behavior via `extends` (subclassing).
Example: `class Vehicle` → `class Car(Vehicle)`. Common fields `max_speed`, method `start()`, specialized `open_trunk()` in `Car`.
* **Polymorphism**: Same interface, different behavior at runtime.
Example: `for s in shapes: s.draw()` where `Circle.draw()` and `Rectangle.draw()` behave differently.

Also revise SOLID at a one‑liner level:

* SRP, OCP, LSP, ISP, DIP – and try to map them to patterns below.

---

## High‑yield patterns (with quick examples)

These are the ones that show up most in LLD / OO‑design rounds.

### 1. Singleton

Intent: Ensure only one instance, global access point.

Example: Logger used across services.

```python
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Simple thread-safe check (or use a lock for high concurrency)
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, msg: str):
        print(f"[LOG]: {msg}")

# Usage:
# l1 = Logger()
# l2 = Logger()
# l1 is l2 -> True

```

Where to mention in interview:

* Config manager
* Database connection pool wrapper
* Central metrics/telemetry

---

### 2. Factory Method / Simple Factory

Intent: Centralize object creation logic; caller asks for an interface, factory decides concrete class.

Example: Notification system (email, SMS, push).

```python
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, to: str, message: str):
        pass

class EmailNotification(Notification):
    def send(self, to, message):
        print(f"Sending Email to {to}: {message}")

class SMSNotification(Notification):
    def send(self, to, message):
        print(f"Sending SMS to {to}: {message}")

class NotificationFactory:
    @staticmethod
    def create(notification_type: str) -> Notification:
        if notification_type == "EMAIL":
            return EmailNotification()
        elif notification_type == "SMS":
            return SMSNotification()
        raise ValueError("Unknown notification type")

# Usage:
# n = NotificationFactory.create("EMAIL")
# n.send("user@example.com", "Hello")

```

Where to use:

* Payment gateways (`PaymentFactory` → `Razorpay`, `Stripe`, etc.)
* Storage backends (`Storage` → `S3Storage`, `LocalStorage`)

---

### 3. Strategy

Intent: Swap algorithms/behaviors at runtime without `if‑else` ladders.

Example: Different sorting strategies, or Amazon‑style shipping cost strategies.

```python
from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, order) -> int:
        pass

class StandardShipping(ShippingStrategy):
    def calculate_cost(self, order) -> int:
        return 50

class ExpressShipping(ShippingStrategy):
    def calculate_cost(self, order) -> int:
        return 100

class Order:
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy
        
    def shipping_cost(self) -> int:
        return self.strategy.calculate_cost(self)

# Usage:
# o1 = Order(StandardShipping())
# o2 = Order(ExpressShipping())

```

Where to say in interviews:

* Pricing rules for different customer types
* Different cache eviction policies (LRU, LFU, FIFO)
* Recommendation ranking algorithms

---

### 4. Observer

Intent: One‑to‑many dependency; when subject changes, observers are notified.

Example: Order status update notifications (email + SMS + push).

```python
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, order_id: str, status: str):
        pass

class EmailObserver(Observer):
    def update(self, order_id, status):
        print(f"Email: Order {order_id} is now {status}")

class SMSObserver(Observer):
    def update(self, order_id, status):
        print(f"SMS: Order {order_id} is now {status}")

class OrderSubject:
    def __init__(self):
        self._observers = []

    def add_observer(self, o: Observer):
        self._observers.append(o)

    def remove_observer(self, o: Observer):
        self._observers.remove(o)

    def set_status(self, order_id: str, status: str):
        # update DB logic here...
        self._notify_all(order_id, status)

    def _notify_all(self, order_id, status):
        for o in self._observers:
            o.update(order_id, status)

```

Where to mention:

* Notification systems
* Event bus, pub‑sub
* Stock price updates to multiple dashboards

---

### 5. Decorator

Intent: Add behavior to an object dynamically, without modifying its class or explosion of subclasses.

Example: Coffee ordering system (base coffee + milk + caramel + whip).

```python
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self) -> int:
        pass
    
    @abstractmethod
    def description(self) -> str:
        pass

class SimpleCoffee(Coffee):
    def cost(self): return 50
    def description(self): return "Coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, inner: Coffee):
        self._inner = inner

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._inner.cost() + 10
    
    def description(self):
        return self._inner.description() + ", Milk"

# Usage:
# c = SimpleCoffee()
# c = MilkDecorator(c)
# c.cost() -> 60

```

Where to say:

* Adding features to a base subscription
* Adding filters/logging/metrics around service calls

---

### 6. Builder

Intent: Construct complex objects step‑by‑step with many optional params, without telescoping constructors.

```python
class User:
    def __init__(self, builder):
        self.username = builder._username
        self.email = builder._email
        self.phone = builder._phone
        self.address = builder._address

    class Builder:
        def __init__(self):
            self._username = None
            self._email = None
            self._phone = None
            self._address = None

        def set_username(self, u):
            self._username = u
            return self

        def set_email(self, e):
            self._email = e
            return self

        def set_phone(self, p):
            self._phone = p
            return self

        def set_address(self, a):
            self._address = a
            return self

        def build(self):
            return User(self)

# Usage:
# u = User.Builder().set_username("rahul").set_email("r@example.com").build()

```

Where to mention:

* Creating HTTP requests
* Building complex configuration objects

---

### 7. Adapter

Intent: Make incompatible interfaces work together.

Example: Your code expects `PaymentGateway` interface, but third‑party SDK exposes different methods.

```python
class PaymentGateway:
    def pay(self, amount: int):
        pass

class ThirdPartySDK:
    def make_payment(self, amt_in_rupees: float):
        print(f"Processing {amt_in_rupees} via SDK")

class PaymentAdapter(PaymentGateway):
    def __init__(self):
        self.sdk = ThirdPartySDK()

    def pay(self, amount: int):
        # Convert or adapt logic here
        self.sdk.make_payment(float(amount))

```

Where to say:

* Integrating legacy modules
* Wrapping external APIs

---

### 8. Facade

Intent: Provide a simple interface over a complex subsystem.

```python
class InventoryService:
    def reserve(self, product_id): return True

class PaymentService:
    def charge(self, user_id, amount): return True

class ShippingService:
    def ship(self, product_id, address): print("Shipped")

class OrderFacade:
    def __init__(self):
        self.inventory = InventoryService()
        self.payment = PaymentService()
        self.shipping = ShippingService()

    def place_order(self, user_id, product_id, amount, address):
        if not self.inventory.reserve(product_id): return False
        if not self.payment.charge(user_id, amount): return False
        self.shipping.ship(product_id, address)
        return True

```

Where to mention:

* “PlaceOrderService” hiding many microservices
* Simplifying complex workflows in a clean API

---

## How to answer an Amazon OOD / LLD question

When they say, “Design a parking lot / elevator / Amazon locker system”:

1. Clarify requirements and constraints (users, operations, scale, concurrency at a high level).
2. Identify main entities and relationships
* Example: Parking lot → `ParkingLot`, `ParkingSpot`, `Vehicle`, `Ticket`, `Payment`.


3. Apply OOP pillars
* Use inheritance: `Vehicle` → `Car`, `Bike`.
* Use abstraction: `Payment` interface with `CardPayment`, `CashPayment`.


4. Sprinkle 2–3 patterns naturally
* Strategy: fee calculation based on vehicle type or duration.
* Observer: notify user when spot becomes free.
* Singleton: `ParkingLotManager` (very lightly, acknowledge trade‑offs).
* Factory: creating `Vehicle` or `Ticket` based on input.


5. Talk about SOLID and extensibility
* “If tomorrow we add `Truck`, we just add a new subclass and plug into strategy; no change to existing classes (OCP).”



---

## 15‑minute daily drill (day before interview)

* Pick 1 problem: Parking lot, Hotel booking, Library, Online movie ticket booking, Amazon cart.
* For each:
* List entities and relationships (5 minutes).
* Sketch class diagram in rough (5 minutes).
* Say aloud which patterns you’d use where and why (5 minutes).



If you share 1–2 specific systems you’re likely to get (parking lot, elevator, Amazon cart, etc.), I can outline class diagrams + where to plug each pattern for those use‑cases.

Would you like me to outline the class structure and design patterns for a **Parking Lot** or an **Elevator System** using Python?