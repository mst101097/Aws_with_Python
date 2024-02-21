import boto3
import json
from decimal import Decimal

def load_movie(movies,dynamodb=None):
    if not dynamodb:
        dynamodb= boto3.resource('dynamodb',region_name='us-east-1')
    
    table = dynamodb.Table('Movies')

    for movie in movies:
        year = int(movie['year'])
        title =  movie['title']
        print("Adding movie :",year, title)
        table.put_item(Item=movie)



if  __name__=="__main__":
    with open('moviedata.json') as jsonFile:
        movie_list= json.load(jsonFile,parse_float=Decimal)

    load_movie(movie_list)

