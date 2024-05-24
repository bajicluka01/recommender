from pandas import *
import math

class ItemBasedPredictor:
    def similarity(self, p1, p2):
        U = self.U
        #U = U[np.isfinite(U[p1])]
        #U = U[np.isfinite(U[p2])]
        U = U[notnull(U[p1])]
        U = U[notnull(U[p2])]

        norm1 = 0
        norm2 = 0
        sum1 = 0
        users = U.index.tolist()
        if len(users) < self.min_values:
            return 0
        users_mean = self.U.mean(axis=1)
        adjusted_ratings = self.U.sub(users_mean[:, None]).fillna(0).to_numpy()
        users = (self.U.iloc[:,p1] * self.U.iloc[:,p2]).to_numpy().nonzero()[0]
        for u in users:
            #sum1 = sum1 + ((U[p1][u] - self.average[u]) * (U[p2][u] - self.average[u]))
            #norm1 = norm1 + ((U[p1][u] - self.average[u]) ** 2)
            #norm2 = norm2 + ((U[p2][u] - self.average[u]) ** 2)
            sum1 = sum1 + adjusted_ratings[u][p1] * adjusted_ratings[u][p2]
            norm1 = norm1 + adjusted_ratings[u][p1] ** 2
            norm2 = norm2 + adjusted_ratings[u][p2] ** 2

        sim = round((sum1 / (math.sqrt(norm1) * math.sqrt(norm2))), 12)
        if sim < self.threshold:
            return 0
        return sim
        
    def fit(self, uim):
        self.ratings = uim.getRatings()
        sum = self.ratings.groupby(['userID'])['rating'].agg('sum').to_dict()
        n = self.ratings.groupby(['userID']).size().to_dict()
        self.average = {}
        for x,y in sum.items():
            self.average[x] = sum[x] / n[x]
        self.U = self.ratings.pivot(index='userID', columns='movieID', values='rating')
        allMovies = unique(self.ratings['movieID'].tolist())
        self.similarityMatrix = np.zeros((len(allMovies), len(allMovies)))
        for i in range(len(allMovies)):
            for j in range(i+1,len(allMovies)):
                sim = self.similarity(allMovies[i], allMovies[j])
                self.similarityMatrix[i, j] = sim
                self.similarityMatrix[j, i] = sim
        
        print(self.similarityMatrix)


        
    def predict(self, user_id, n=10, rec_seen=True):
        pass

    def similarItems(self, item, n):
        #lookup v similarityMatrix - indeksi top n najvecjih stevil v vrstici item
        pass
        
    def __init__(self, min_values=0, threshold=0):
        self.min_values = min_values
        self.threshold = threshold
