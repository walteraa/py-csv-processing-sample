'''
    main application
'''
import os
import sys
from csv_utils.csv_processing import CSVParser
from celery_app.tasks import create_entry

TOP_SIZE = 10
COMPARATOR_INDEX = 6

def main():
    """Main method to run the app"""
    if len(sys.argv) != 2:
        print("You should run main by running the following command:"\
              "\n\npython main.py \"The text you would like to send\"")
        exit(1)
    no_variables = False
    if os.environ.get('TWITTER_CONSUMER_KEY') is None:
        print("You should define TWITTER_CONSUMER_KEY environment variable")
        no_variables = True
    if os.environ.get('TWITTER_CONSUMER_SECRET') is None:
        print("You should define TWITTER_CONSUMER_SECRET environment variable")
        no_variables = True

    if no_variables:
        exit(1)

    csv_processor = CSVParser(sys.argv[1])

    for data in csv_processor.top_n(TOP_SIZE, COMPARATOR_INDEX, 'Music', 'Book'):
        create_entry.delay(data)
        print('Task to process {0} was enqueued'.format(data['name']))
    print('All entries was enqueued')


if __name__ == '__main__':
    main()
