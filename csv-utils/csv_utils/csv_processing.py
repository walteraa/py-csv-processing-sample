import csv, heapq

class CSVParser:
    '''
        Class which represents the CSV parser
    '''
    def __init__(self, file_path):
        '''
            Constructor
            Arguments:
            file_path (str): The path of the file to be processed
        '''
        self.file_path = file_path

    def top_n(self, list_size: int, index: int, *categories: str):
        ''' This method is used to get the top n entries of a csv considering the
            column index and the categories as filter

            Parameters:
            list_size (int): The top list size
            index (int): The csv column index to be considered in the "lambda compare to"
            *categories (str): The categories to be filtered in the CSV

            Returns:
            list<dict>: The top n elements processed as a dictionary
        '''

        if self.file_path is None:
            raise Exception('Invalid file')

        if not categories:
            raise Exception('Invalid categories')

        if list_size < 1:
            raise Exception('Invalid size')

        if index < 0:
            raise Exception('Invalid lambda index')

        try:
            with open(self.file_path, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                data = map(lambda row: {'name': row[2],
                                        'count': row[6],
                                        'id': row[0],
                                        'type': row[12],
                                        'size_bytes': row[3],
                                        'price': row[5]},
                           heapq.nlargest(list_size,
                                          filter(lambda e: e[12] in categories,
                                                 reader
                                                 ),
                                          key=lambda e: int(e[index])
                                          )
                           )
                return list(data)
        except:
            raise Exception('Invalid file')
