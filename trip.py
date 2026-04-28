class TripDetails:
    def __init__(self, tripid, customerid, driverid, pickup, drop, status, fare, startTime, endTime,
                 distance=0, duration=0, vehicle_type='economy', is_peak_hour=False, is_bad_weather=False):
        self.tripid = tripid
        self.customerid = customerid
        self.driverid = driverid
        self.pickup = pickup
        self.drop = drop
        self.status = status
        self.fare = fare
        self.startTime = startTime
        self.endTime = endTime
        self.distance = distance  
        self.duration = duration 
        self.vehicle_type = vehicle_type 
        self.is_peak_hour = is_peak_hour
        self.is_bad_weather = is_bad_weather
    def start(self):
        print(f"Trip {self.tripid} has started.")
    def end(self):
        print(f"Trip {self.tripid} has ended.")
    def cancel(self):
        print(f"Trip {self.tripid} has been canceled.")
    def calculateFare(self):
        print(f"Calculating fare for trip {self.tripid}.")
    