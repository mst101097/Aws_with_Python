import boto3
from boto3.dynamodb.conditions import Key

def query_movies(year, dynamodb=None):
    if not dynamodb:
        dynamodb= boto3.resource('dynamodb',region_name='us-east-1')
    

    table = dynamodb.Table('Movies')


    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )

    return response['Items']

if __name__=="__main__":
    query_year = 2013
    print("Movies from {}".format(query_year))

    movies = query_movies(query_year)

    for movie in movies:
        print(movie['year'],":",movie['title'])


# Movies from 2013
# 2013 : Prisoners
# 2013 : Rush
# 2013 : The Hunger Games: Catching Fire
# 2013 : This Is the End
# 2013 : Thor: The Dark World
# 2013 : World War Z
