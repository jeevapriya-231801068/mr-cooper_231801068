class CustomerPhase:
    def __init__(self,customerid,name,phone,savedPayments,rating,rideHistory):
        self.customerid=customerid
        self.name=name
        self.phone=phone
        self.savedPayments=[]
        self.rating=rating
        self.rideHistory=[]
    def requestRide(self,driver):
        print(f"{self.name} has requested a ride from {driver.name}.")
    def cancelRide(self,driver):
        print(f"{self.name} has canceled the ride request from {driver.name}.")
    def rateDriver(self,driver,rating):
        print(f"{self.name} has rated {driver.name} with a rating of {rating}.")
    def viewHistory(self):
        print(f"{self.name}'s ride history: {self.rideHistory}")
    def addPaymentMethod(self,payment):
        self.savedPayments.append(payment)
        print(f"{self.name} has added a new payment method: {payment}.")
    def removePaymentMethod(self,payment):
        if payment in self.savedPayments:
            self.savedPayments.remove(payment)
            print(f"{self.name} has removed the payment method: {payment}.")
        else:
            print(f"{payment} not found in {self.name}'s saved payment methods.")
            
            