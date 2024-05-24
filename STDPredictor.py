from pandas import *
import random

class STDPredictor:
    def fit(self, uim):
        self.df = uim.getRatings()
        self.df = self.df[self.df.groupby('movieID').movieID.transform('count') > self.n]
        self.std = self.df.groupby(['movieID'])['rating'].std().to_dict()

    def predict(self, user_id):
        return self.std 
        
    def __init__(self, n=100):
        self.n = n
