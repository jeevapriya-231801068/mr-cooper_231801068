# Store all ratings for drivers
driver_ratings = {}


class Rating:
    def __init__(self, ratingId, tripId, raterType, score, comment):
        self.ratingId = ratingId
        self.tripId = tripId
        self.raterType = raterType
        self.score = score
        self.comment = comment

    def submit(self):
        print(f"Rating {self.ratingId} for trip {self.tripId} submitted by {self.raterType} with score {self.score}. Comment: {self.comment}")
        self.updateAverageRating()

    def updateAverageRating(self):
        driver_id = getattr(self, 'driver_id', None)
        if driver_id is None:
            print(f"Rating submitted. Comment: {self.comment}")

    @staticmethod
    def add_rating(driver_id, score):
        if driver_id not in driver_ratings:
            driver_ratings[driver_id] = []
        driver_ratings[driver_id].append(score)
        driver_id = driver_id
        print(f"Added rating {score} for driver {driver_id}. Current ratings: {driver_ratings[driver_id]}")

    @staticmethod
    def get_average_rating(driver_id):
        if driver_id not in driver_ratings or len(driver_ratings[driver_id]) == 0:
            return None
        return sum(driver_ratings[driver_id]) / len(driver_ratings[driver_id])
        