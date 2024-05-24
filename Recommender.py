from pandas import *
import random
from operator import itemgetter

class Recommender:
    def evaluate(self, test_data, n):
        mse = mae = precision = recall = f = 0
        test = test_data.getRatings()
        users = test.userID.unique()
        testPivoted = test.pivot(index='userID', columns='movieID', values='rating')
        
        sum = self.ratings.groupby(['userID'])['rating'].agg('sum').to_dict()
        n = self.ratings.groupby(['userID']).size().to_dict()
        self.average = {}
        for x,y in sum.items():
            self.average[x] = sum[x] / n[x]

        for user in users:
            actualRatings = testPivoted.loc[user].dropna()
            print(actualRatings)
            predictedRatings = self.recommend(user, n=n, rec_seen=False)

            for movie, rating in predictedRatings:
                pass


        return mse, mae, precision, recall, f


    def fit(self, uim):
        self.ratings = uim.getRatings()
        self.predictor.fit(uim)
        
    def recommend(self, user_id, n=10, rec_seen=True):
        d = self.predictor.predict(user_id)
        if rec_seen == True:
            l = [(a,b) for a,b in d.items()]
        else:
            tmp = self.ratings[self.ratings['userID'] == user_id]
            moviesWatchedByUser = tmp['movieID'].values
            l = [(a,b) for a,b in d.items() if a not in moviesWatchedByUser]
        #l.sort(key=itemgetter(1, 0), reverse=True)
        l = sorted(l, key=lambda x: x[0])
        l = sorted(l, key=lambda x: x[1], reverse=True)

        if len(l) < n:
            return l
        return l[0:n]

    def __init__(self, predictor):
        self.predictor = predictor
