import matching
import trip as trip_module
import fareengine
import rating as rating_module
from driver import Driver_phase
from Customer import CustomerPhase


def main():
    matching.add_driver(1, "John Smith", "sedan", (40.7, -74.0))
    matching.add_driver(2, "Sarah Jones", "sedan", (40.75, -74.05))
    matching.add_driver(3, "Mike Brown", "sedan", (40.8, -74.1))
    matching.add_driver(4, "Emily Davis", "premium", (40.72, -74.02))
    print(f"Added {len(matching.drivers)} drivers\n")
    

    
    customer = CustomerPhase(
        customerid=101,
        name="Alice",
        phone="555-1234",
        savedPayments=["Credit Card"],
        rating=4.5,
        rideHistory=[]
    )
    print(f"Customer: {customer.name}\n")

    
    lat = float(input("Enter pickup latitude: "))
    lon = float(input("Enter pickup longitude: "))
    customer_location = (lat, lon)
    
    drop_lat = float(input("Enter drop latitude: "))
    drop_lon = float(input("Enter drop longitude: "))
    drop_location = (drop_lat, drop_lon)
    
    ride_type = input("Enter ride type (sedan/premium): ")
    print()
    
    driver = matching.findNearestDriver(customer_location, ride_type)
    
    if driver:
        print(f"Found driver: {driver['name']}")
        
        driver_obj = Driver_phase(
            driverid=driver['driver_id'],
            name=driver['name'],
            phone="555-9999",
            vehicleDetails="Toyota Camry",
            location=driver['location'],
            rating=4.8,
            isOnline=True,
            earningsToday=0
        )
        
    
        driver_obj.goOnline()
        

        trip = trip_module.TripDetails(
            tripid="TRIP001",
            customerid=customer.customerid,
            driverid=driver_obj.driverid,
            pickup=customer_location,
            drop=drop_location,
            status="in_progress",
            fare=0,
            startTime="10:00",
            endTime="",
            distance=5.2,  
            duration=15,  
            vehicle_type=ride_type,
            is_peak_hour=True,
            is_bad_weather=False
        )
        
        trip.start()
        
        cancel = input("Do you want to cancel this ride? (yes/no): ").strip().lower()
        
        if cancel == "yes" or cancel == "y":
            trip.status = "cancelled"
            print(f"\nRide cancelled! Trip {trip.tripid} has been cancelled.")
            return 
        
        print("Ride continues to destination...")
        
        

        fare_calc = fareengine.FareEngine({})
        final_fare = fare_calc.calculate_fare(trip)
        trip.fare = final_fare
        print(f"Final fare: ${final_fare:.2f}")
        
        
        trip.end()
        trip.status = "completed"
        print(f"Trip {trip.tripid} completed. Fare: ${final_fare:.2f}")
        payment_method = customer.savedPayments[0] if customer.savedPayments else "Cash"
        
        print(f"Payment of ${final_fare:.2f} processed using {payment_method}.\n")
            
            
        
        
        while True:
            try:
                rating_score = int(input("Enter rating (1-5): "))
                if 1 <= rating_score <= 5:
                    break
                print("Please enter a number between 1 and 5")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5")
        
        feedback = input("Enter your feedback: ")
        print()
        
        rating_module.Rating.add_rating(driver_obj.driverid, rating_score)
        avg_rating = rating_module.Rating.get_average_rating(driver_obj.driverid)
        
        trip_rating = rating_module.Rating(
            ratingId="R001",
            tripId=trip.tripid,
            raterType="customer",
            score=rating_score,
            comment=feedback
        )
        trip_rating.driver_id = driver_obj.driverid
        trip_rating.submit()
        
        if avg_rating:
            print(f"Driver {driver_obj.name}'s average rating: {avg_rating:.2f}/5.0")
        
        
    else:
        available = matching.expandSearch(customer_location, ride_type)
        if available:
            print(f"Found {len(available)} drivers in expanded area")
        else:
            print("No drivers found even in expanded search.")
            


if __name__ == "__main__":
    main()