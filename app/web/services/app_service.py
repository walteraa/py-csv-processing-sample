
from db.client import Database

db = Database()

def app_list():
    data_list = db.all()
    result = []

    # Map result
    for data in data_list:
        result.append(
            {'id': data['id'],
             'track_name': data['name'],
             'n_citacoes': data['mentions'],
             'size_bytes': data['size_bytes'],
             'price': data['price'],
             'prime_genre': data['type']
             }
        )
    return result
