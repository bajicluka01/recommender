from pandas import *
import random

class ViewsPredictor:
    def fit(self, uim):
        self.df = uim.getRatings()
        self.views = self.df.groupby(['movieID']).size().to_dict()

    def predict(self, user_id):
        return self.views 
        
    def __init__(self):
        pass
