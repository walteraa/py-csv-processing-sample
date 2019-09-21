'''
    Tasks module. Create here any tasks you would like to perform async
'''
import os
from celery_app.celery import app
from db.client import Database
from twitter_searcher.core.searcher import TwitterSearcher

# A max iteration for each entry due to API request in a 15min time-window
MAX_ITERATION = 10
searcher = TwitterSearcher(os.environ['TWITTER_CONSUMER_KEY'],
                           os.environ['TWITTER_CONSUMER_SECRET'],
                           os.environ['TWITTER_TOKEN_KEY'],
                           os.environ['TWITTER_TOKEN_SECRET'])

@app.task
def create_entry(data):
    '''
        Create the object in the database

        Arguments:
        data (dict): Data do be created in the database
    '''
    database = Database()
    data['search_count'] = 0
    data['mentions'] = 0
    entry_id = str(database.insert(data).inserted_id)
    query_twitter.delay(entry_id, data['name'])

@app.task
def query_twitter(entry_id, search_text, since_id=None, iteration=1):
    response = searcher.search(search_text, since_id)
    count = len(response['statuses'])
    max_id = response['search_metadata']['max_id']
    database = Database()
    database.increment(entry_id, count)

    if iteration < MAX_ITERATION and max_id != since_id:
        query_twitter.delay(entry_id,
                            search_text,
                            since_id=max_id,
                            iteration=iteration + 1)
    return 'ran {0} times for id={1}, and was incremented by {2}'.format(iteration, entry_id, count)
