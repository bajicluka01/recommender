from pandas import *

class UserItemData:
    def read(self, path):
        [startDay, startMonth, startYear] = self.start_date.split('.')
        [endDay, endMonth, endYear] = self.end_date.split('.')
        self.ratings = read_csv(path, sep='\t')
        self.ratings = self.ratings[(self.ratings['date_year'] >= int(startYear)) & (self.ratings['date_year'] <= int(endYear))]
        self.ratings = self.ratings.drop(self.ratings[(self.ratings['date_year'] == int(startYear)) & (self.ratings['date_month'] < int(startMonth))].index)
        self.ratings = self.ratings.drop(self.ratings[(self.ratings['date_year'] == int(endYear)) & (self.ratings['date_month'] > int(endMonth))].index)
        self.ratings = self.ratings.drop(self.ratings[(self.ratings['date_year'] == int(startYear)) & (self.ratings['date_month'] == int(startMonth)) & (self.ratings['date_day'] < int(startDay))].index)
        self.ratings = self.ratings.drop(self.ratings[(self.ratings['date_year'] == int(endYear)) & (self.ratings['date_month'] == int(endMonth)) & (self.ratings['date_day'] >= int(endDay))].index)
        self.ratings = self.ratings[self.ratings.groupby('movieID').movieID.transform('count') > self.min_ratings]

    def nratings(self):
        return len(self.ratings)

    def getRatings(self):
        return self.ratings
        
    def __init__(self, path, start_date = '1.1.1', end_date = '31.12.3000', min_ratings = 0):
        self.path = path
        self.start_date = start_date
        self.end_date = end_date
        self.min_ratings = min_ratings
        self.read(path)
