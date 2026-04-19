🚗 Parking Lot System – Low Level Design (LLD)
📌 Overview

This project is a clean and extensible implementation of a Parking Lot System designed using object-oriented principles. It focuses on clarity, scalability, and real-world applicability—exactly the kind of design expected in SDE-1 interviews.

The goal is not just to make it work, but to make it easy to extend, maintain, and reason about.

🧠 Design Approach

The system is built with the following principles in mind:

Separation of Concerns – Each class has a clearly defined responsibility
Extensibility – New features (like pricing models or vehicle types) can be added easily
Thread Safety – Slot allocation is protected against race conditions
Clean Architecture – Models, services, and strategies are logically separated
🏗️ Core Components
1. Vehicle

Represents a vehicle entering the parking lot.
Each vehicle has:

Vehicle number
Vehicle type (Car, Bike, Truck)
2. Parking Slot

Represents an individual parking space.

Responsibilities:

Check if the slot is available
Assign/remove a vehicle
Handle concurrent access safely using locks
3. Parking Floor

Represents a floor in the parking lot.

Responsibilities:

Maintain a list of parking slots
Find an available slot based on vehicle type
4. Ticket

Generated when a vehicle is parked.

Contains:

Vehicle details
Assigned slot
Entry time
Exit time

Used for calculating parking fees.

5. Payment Strategy

Implements flexible pricing logic.

Why this matters:
Instead of hardcoding pricing, we use a strategy pattern, allowing different pricing methods like:

Hourly pricing
Flat rate
Weekend pricing
6. Parking Lot (Service Layer)

Acts as the main controller of the system.

Responsibilities:

Park a vehicle
Unpark a vehicle
Coordinate between floors, slots, and payment
⚙️ How It Works
Parking Flow:
Vehicle arrives
System searches for an available slot
Slot is assigned
Ticket is generated
Unparking Flow:
Ticket is presented
Exit time is recorded
Fee is calculated using pricing strategy
Slot is freed
🔒 Concurrency Handling

To avoid issues like two vehicles taking the same slot:

Each parking slot uses a lock
Assignment happens inside a critical section

This ensures safe operation in multi-threaded environments.

🚀 How to Run
Copy the code into a file (e.g., parking_lot.py)
Run using:
python parking_lot.py
You will see:
Vehicle parked
Parking fee calculated after delay
🔥 Possible Enhancements

This design is intentionally extensible. You can improve it by adding:

Multiple floors with optimized lookup (O(1))
Different pricing per vehicle type
Entry/exit gates with queues
Reservation system
Database integration
REST APIs for real-world usage
