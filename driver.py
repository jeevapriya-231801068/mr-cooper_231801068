class Driver_phase:
    def __init__(self,driverid,name,phone,vehicleDetails,location,rating,isOnline,earningsToday):
        self.driverid=driverid
        self.name=name
        self.phone=phone
        self.vehicleDetails=vehicleDetails
        self.location=location
        self.rating=rating
        self.isOnline=isOnline
        self.earningsToday=earningsToday
    def goOnline(self):
        print(f"{self.name} is now online.")
    def goOffline(self):
        print(f"{self.name} is now offline.")
    def acceptRide(self,ride):
        print(f"{self.name} has accepted the ride request from {ride.rider.name}.")
    def completeTrip(self,ride):
        print(f"{self.name} has completed the trip for {ride.rider.name}.")
    

    