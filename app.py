from flask import Flask, render_template, jsonify, request, redirect
import io
import os
from flask_cors import CORS
import json


from werkzeug.datastructures import FileStorage
app = Flask(__name__)
CORS(app)


intial_json = {
    "nodes": [],
    "links": []
}


@app.route("/upload-image", methods=["GET", "POST"])
def upload_file():
    try:
        io_string = None
        data = None
        if request.method == "POST":
            if request.files:
                file = request.files['file']
                data_set = file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                data = json.load(io_string)
        return render_template('force_graph.html', geocode=data)
    except Exception as e:
        return str(e)


@app.route('/')
def hello_world():

    return render_template('force_graph.html', geocode=intial_json )



if __name__ == '__main__':
    app.run(debug=True)
