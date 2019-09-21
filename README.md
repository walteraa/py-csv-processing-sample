## Architectural overeview

This application uses a distributed architecture which provides a power of scalability and resilience. I decides to distribute this in few elements as described below:

- Workers: This element is basically a Celery app which gonna receive request trough a RabbitMQ queue and process the data in an async approach. It uses some library which gonna to be described here.
- Libs: The main point of data processing, and listed as:
    - csv-processing: The lib responsible for do all the filter and map as described in the requirements: Filter by category, order by reviews count and map as described in the requirements;
    - TwitterSearcher: The lib which just wraps some functionalities from twython;
    - Database: A lib which wraps some functionalities from pymongo, applied in our context;
- Webapp: A sample flask API which respond the result as JSON or as a CSV download file;
- Cli: a script which open the CSV input file, pre-process it by using the csv-procesing lib and perform async tasks in Celery to reach the Twitter API and get the search count, saving it in the database;

The approach here is simple as described below:

- The file is processed and we got the first 10 entries which are Books or Music ordered by reviews count;
- For each entry, perform(enqueue) an async task to create these entries in the database;
- For each entry creation task, it gonna perform(eneuque) another async tasks to get count from twitter API and increment it in the `n_citacoes` field;
    - Each entry peform the Twitter search/update up to 10 times, due to API limitations

![Architectural overeview diagram](docs/csv-processing-arch.png)
