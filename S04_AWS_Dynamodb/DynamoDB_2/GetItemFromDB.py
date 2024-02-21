import boto3
from  pprint import pprint
from botocore.exceptions import ClientError

def get_movie(title,year,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    
    table = dynamodb.Table('Movies')

    try:
        response = table.get_item(Key={'year':year,'title':title})
    
    except ClientError as e:
        print(e.response['Error']['Message'])
    
    else:
        return response['Item']

if __name__=="__main__":

    movie = get_movie('Insidious: Chapter 2',2013)
    if movie:
        pprint(movie)




'''
{'info': {'actors': ['Patrick Wilson', 'Rose Byrne', 'Barbara Hershey'],
          'directors': ['James Wan'],
          'genres': ['Horror', 'Thriller'],
          'image_url': 'http://ia.media-imdb.com/images/M/MV5BMTg0OTA5ODIxNF5BMl5BanBnXkFtZTcwNTUzNDg4OQ@@._V1_SX400_.jpg',
          'plot': 'The haunted Lambert family seeks to uncover the mysterious '
                  'childhood secret that has left them dangerously connected '
                  'to the spirit world.',
          'rank': Decimal('7'),
          'rating': Decimal('7.1'),
          'release_date': '2013-09-13T00:00:00Z',
          'running_time_secs': Decimal('6360')},
 'title': 'Insidious: Chapter 2',
 'year': Decimal('2013')}


'''