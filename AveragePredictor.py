from pandas import *
import random

class AveragePredictor:
    def fit(self, uim):
        self.df = uim.getRatings()

        vs = self.df.groupby(['movieID'])['rating'].agg('sum').to_dict()
        n = self.df.groupby(['movieID']).size().to_dict()

        g_avg = 0
        if self.b > 0:
            g_avg = self.df['rating'].mean()
               
        self.average = {}
        for x,y in vs.items():
            self.average[x] = (y + self.b * g_avg) / (n[x] + self.b)

    def predict(self, user_id):
        return self.average 
        
    def __init__(self, b=0):
        self.b = b
