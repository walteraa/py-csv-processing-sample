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
        raise Exception("Not implemented")
