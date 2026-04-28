from abc import ABC, abstractmethod



class FareStrategy(ABC):
    
    @abstractmethod
    def calculate(self, trip):
        pass
    
    def apply_surge(self, subtotal, trip):
        if trip.is_peak_hour or trip.is_bad_weather:
            if trip.is_peak_hour and trip.is_bad_weather:
                return subtotal * 3.0
            elif trip.is_peak_hour or trip.is_peak_hour:
                return subtotal * 2.0
        return subtotal
    
    def apply_minimum(self, total):
        return max(total, 60)


class EconomyFare(FareStrategy):
    
    def calculate(self, trip):
        base_fare = 30
        rate_per_km = 12
        
        if trip.distance <= 2:
            distance_fare = 0
        else:
            distance_fare = (trip.distance - 2) * rate_per_km
        
        time_charge = trip.duration * 2
        subtotal = base_fare + distance_fare + time_charge
        
        total = self.apply_surge(subtotal, trip)
        return self.apply_minimum(total)


class PremiumFare(FareStrategy):
    
    def calculate(self, trip):
        base_fare = 50 
        rate_per_km = 18  
        
        if trip.distance <= 2:
            distance_fare = 0
        else:
            distance_fare = (trip.distance - 2) * rate_per_km
        
        time_charge = trip.duration * 3 
        subtotal = base_fare + distance_fare + time_charge
        
        total = self.apply_surge(subtotal, trip)
        return self.apply_minimum(total)


class NoSurgeFare(FareStrategy):
    
    def calculate(self, trip):
        base_fare = 30
        rate_per_km = 12 if trip.vehicle_type == 'economy' else 18
        
        if trip.distance <= 2:
            distance_fare = 0
        else:
            distance_fare = (trip.distance - 2) * rate_per_km
        
        time_charge = trip.duration * 2
        subtotal = base_fare + distance_fare + time_charge
        
        return self.apply_minimum(subtotal)

class FareEngine:
    
    def __init__(self, fare_rules):
        self.fare_rules = fare_rules
        self._strategy = None
    
    def set_strategy(self, strategy: FareStrategy):
        self._strategy = strategy
    
    def calculate_fare(self, trip):
        if self._strategy is None:
            if trip.vehicle_type == 'premium':
                self._strategy = PremiumFare()
            else:
                self._strategy = EconomyFare()
        
        return self._strategy.calculate(trip)

    def calculate_cancellation_fee(self, trip, driver_arrived, driver_delay_minutes):
        
        if not driver_arrived:
            return 0  
        if driver_delay_minutes > 5:
            return 0
        
        return 50