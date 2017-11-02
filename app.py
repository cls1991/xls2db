# coding: utf8

"""
    core logic for export xls sheet to mysql table.
"""

import os

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import tablib

import resource

UPLOAD_FOLDER = 'tmp'
ALLOWED_EXTENSIONS = ('xls', 'xlsx')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.debug = True


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


mappings = {
    'sample(sample.xls)': 'sample',
}


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    result = False
    errmsg = ''
    if request.method == 'POST':
        f = request.files['file']
        m = request.form['model']
        if f and allowed_file(f.filename):
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.mkdir(app.config['UPLOAD_FOLDER'])
            path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
            f.save(path)
            model = resource.sources.get(m)
            if model is None:
                errmsg = 'model %s not found' % m
            else:
                with open(path, 'rb') as fs:
                    data_book = tablib.import_book(fs.read())
                    model.import_data(data_book)
                    result = True
        else:
            errmsg = 'only xls, xlsx file allowed'
    return render_template('index.html', mappings=mappings, status='success' if result else 'failure', request=request,
                           errmsg=errmsg)


@app.route('/')
def index():
    return render_template('index.html', mappings=mappings)


if __name__ == '__main__':
    app.run(port=5001)
