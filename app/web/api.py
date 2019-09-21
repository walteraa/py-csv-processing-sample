
from io import StringIO
from flask import Flask, jsonify, make_response
import pyexcel as pe
from web.services.app_service import app_list

app = Flask(__name__)

@app.route('/apps.json')
def json_api():
    return jsonify(app_list())

@app.route('/apps.csv')
def download_csv():
    data = [list(app_list()[0].keys())]
    data += list(map(lambda d: list(d.values()), app_list()))
    sheet = pe.Sheet(data)
    io = StringIO()
    sheet.save_to_memory("csv", io)
    output = make_response(io.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output

if __name__ == '__main__':
    app.run()

