from pandas import *

class MovieData:
    def read(self, path):
        self.movies = read_csv(path, sep='\t')

    def get_title(self, id):
        return self.movies.iloc[self.movies.index[self.movies['id'] == id].tolist()[0]]['title']

    def __init__(self, path):
        self.path = path
        self.read(path)
    