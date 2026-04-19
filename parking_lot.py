from enum import Enum
from threading import Lock
import time

# ENUMS
class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    TRUCK = 3

class SlotType(Enum):
    CAR = 1
    BIKE = 2
    TRUCK = 3


# MODELS
class Vehicle:
    def __init__(self, number, vehicle_type):
        self.number = number
        self.type = vehicle_type


class ParkingSlot:
    def __init__(self, slot_id, slot_type):
        self.slot_id = slot_id
        self.slot_type = slot_type
        self.vehicle = None
        self.lock = Lock()

    def is_free(self):
        return self.vehicle is None

    def assign_vehicle(self, vehicle):
        with self.lock:
            if self.vehicle is None:
                self.vehicle = vehicle
                return True
            return False

    def remove_vehicle(self):
        with self.lock:
            self.vehicle = None


class ParkingFloor:
    def __init__(self, floor_id, slots):
        self.floor_id = floor_id
        self.slots = slots

    def find_available_slot(self, vehicle_type):
        for slot in self.slots:
            if slot.is_free() and slot.slot_type == vehicle_type:
                return slot
        return None


class Ticket:
    def __init__(self, vehicle, slot):
        self.vehicle = vehicle
        self.slot = slot
        self.entry_time = time.time()
        self.exit_time = None

    def close_ticket(self):
        self.exit_time = time.time()


# STRATEGY
class PaymentStrategy:
    def calculate_fee(self, ticket):
        raise NotImplementedError


class HourlyPayment(PaymentStrategy):
    def calculate_fee(self, ticket):
        duration = ticket.exit_time - ticket.entry_time
        hours = duration / 3600
        return round(hours * 10, 2)


# SERVICE
class ParkingLot:
    def __init__(self, floors):
        self.floors = floors

    def park_vehicle(self, vehicle):
        for floor in self.floors:
            slot = floor.find_available_slot(vehicle.type)
            if slot and slot.assign_vehicle(vehicle):
                return Ticket(vehicle, slot)
        return None

    def unpark_vehicle(self, ticket, payment_strategy):
        ticket.close_ticket()
        fee = payment_strategy.calculate_fee(ticket)
        ticket.slot.remove_vehicle()
        return fee


# MAIN
if __name__ == "__main__":
    slots = [ParkingSlot(i, SlotType.CAR) for i in range(5)]
    floor = ParkingFloor(1, slots)
    parking_lot = ParkingLot([floor])

    vehicle = Vehicle("RJ14AB1234", VehicleType.CAR)

    ticket = parking_lot.park_vehicle(vehicle)
    print("Vehicle Parked")

    time.sleep(2)

    payment = HourlyPayment()
    fee = parking_lot.unpark_vehicle(ticket, payment)

    print("Parking Fee:", fee)