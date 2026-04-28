import math

drivers = []


def add_driver(driver_id, name, vehicle_type, location):
    drivers.append({
        'driver_id': driver_id,
        'name': name,
        'vehicle_type': vehicle_type,
        'location': location,
        'is_available': True
    })


def get_distance(loc1, loc2):
    return math.sqrt((loc2[0] - loc1[0])**2 + (loc2[1] - loc1[1])**2)


def findNearestDriver(location, ride_type):
    radius = 3
    
    while radius <= 10:
        found = []
        for d in drivers:
            if d['is_available'] and d['vehicle_type'] == ride_type:
                if get_distance(location, d['location']) <= radius:
                    found.append(d)
        if found:
            return min(found, key=lambda d: get_distance(location, d['location']))
        
        radius = radius + 1
    
    return None


def expandSearch(location, ride_type):
    result = []
    for d in drivers:
        if d['is_available'] and d['vehicle_type'] == ride_type:
            if get_distance(location, d['location']) <= 10:
                result.append(d)
    return result

    