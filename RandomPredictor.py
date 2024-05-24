from pandas import *
import random

class RandomPredictor:
    def fit(self, uim):
        self.uim = uim.getRatings()
        
    def predict(self, user_id):
        return dict([(a, random.randint(self.min_rating, self.max_rating)) for a in self.uim.movieID])   
        
        
    def __init__(self, min_rating, max_rating):
        self.min_rating = min_rating
        self.max_rating = max_rating
