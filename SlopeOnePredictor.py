from pandas import *
import math

class SlopeOnePredictor:
    def deviations(self, df):
        num_movies = df.shape[1]
        dev = np.zeros((num_movies, num_movies))

        for i in range(num_movies):
            for j in range(num_movies):
                s = 0
                d = df.iloc[:,i] - df.iloc[:,j]
                c = d.count()
                d=d.fillna(0)
                s+= d.sum() / c
                dev[i,j] = s
        return dev
        
    def fit(self, uim):
        self.ratings = uim.getRatings()
        self.U = self.ratings.pivot(index='userID', columns='movieID', values='rating')
        allMovies = unique(self.ratings['movieID'].tolist())
        #print(self.deviations(self.U))

        
    def predict(self, user_id, n=10, rec_seen=True):
        allMovies = unique(self.ratings['movieID'].tolist())
        predictions = {}
        return predictions
        my_rated_movies = self.U.loc[user_id].dropna().index.values
        dev = self.deviations(self.U)
        for movie in allMovies:
            movieidx = self.U.columns.get_loc(movie)
            rating_num = 0
            rating_den = 0
            for i in range(dev.shape[0]):
                ID = self.U.columns[i]
                if ID not in my_rated_movies:
                    continue
                if dev[movieidx][i] == 1.0:
                    continue
                if np.isnan(self.U.loc[user_id, ID]):
                    continue
                if i == movieidx:
                    continue
                d = self.U.iloc[:,movieidx] - self.U.iloc[:,i]
                c = d.count()
                rating_num += (dev[movieidx][i] + self.U.loc[user_id, ID] * c)
                rating_den += c
                if rating_den == 0:
                    predictions[movie] = 0
                else:
                    predictions[movie] = rating_num / rating_den

        return predictions

        
    def __init__(self, min_values=0, threshold=0):
        self.min_values = min_values
        self.threshold = threshold
