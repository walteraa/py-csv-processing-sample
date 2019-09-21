'''
    Celery app configuration
'''
import os
from celery import Celery


def make_celery():
    '''
        generates Broker information, configure and return the Celery app
    '''
    broker_url = 'amqp://{0}:{1}@{2}:5672'.format(os.environ['BROKER_USER'],
                                                  os.environ['BROKER_PASS'],
                                                  os.environ['BROKER_HOST'])

    celery = Celery('celery_app',
                    broker=broker_url,
                    backend='rpc://',
                    include=['celery_app.tasks'])

    # Configure queues
    celery.conf.update({
        'task_routes': {
            'create_entry': 'data_queue',
            'update_entry': 'data_queue',
            'query_twitter': 'twitter_queue'
        }
    })

    return celery



app = make_celery()
