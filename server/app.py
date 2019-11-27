# import sigrecogtf
import checktwoimg
import uuid
from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
import os
import shutil
import urllib.request
from werkzeug.utils import secure_filename
import json
from tinydb import TinyDB, Query
db = TinyDB('./db.json')
sigtablemulti = db.table('sigtablemulti')
sigtable = db.table('sigtable')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = './uploads/'
UPLOAD_FOLDER_DATA = './data/'

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_DATA'] = UPLOAD_FOLDER_DATA
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def delete_all_files(folder):
    for filename in os.listdir(folder):
        if(filename):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/file-upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        postMeta = json.loads(request.form.get('postMeta'))
        filename = secure_filename(file.filename)
        sigtableContent = {'rowName':postMeta.get('folder_name')}
        SigTableQry = Query()
        if sigtable.contains(SigTableQry.rowName == postMeta.get('folder_name')):
            if postMeta.get('upload_type') == 'training':
                sigtableContent['training_img'] = filename
            elif postMeta.get('upload_type') == 'test':
                sigtableContent['test_img'] = filename
            print('db.search()',db.search(SigTableQry.rowName == postMeta.get('folder_name')))
            sigtable.update(sigtableContent)
        else:
            delete_all_files(app.config['UPLOAD_FOLDER'])
            sigtable.purge()

            if postMeta.get('upload_type') == 'training':
                sigtableContent['training_img'] = filename
            elif postMeta.get('upload_type') == 'test':
                sigtableContent['test_img'] = filename
            sigtable.insert(sigtableContent)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        resp = jsonify({'message': 'File successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(
            {'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp


@app.route("/file-upload-multi", methods=["POST"])
def upload():
    uploaded_files = request.files.getlist("items[]")
    # print('uploaded_files', uploaded_files)
    postMeta = json.loads(request.form.get('postMeta'))
    print('postMeta', postMeta)

    sigtablemulti.purge()
    sigtablemulti.insert({'folder_name': postMeta.get('folder_name')})

    newpath = app.config['UPLOAD_FOLDER_DATA'] + \
        postMeta.get('upload_type')+'/'+postMeta.get('folder_name')

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    # Delete all previous files (if any)
    delete_all_files(newpath)

    validation_status = False
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            validation_status = True
        else:
            validation_status = False
            break
    print('validation_status', validation_status)
    if validation_status:
        for file in uploaded_files:
            filename = secure_filename(file.filename)
            file.save(os.path.join(newpath, filename))
        resp = jsonify('File successfully uploaded')
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(
            {'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp

@app.route('/traintest', methods=['GET'])
def traintest():
    print('sigtablemulti_data', sigtablemulti.all())
    result_data =  1.0 # sigrecogtf.main(sigtablemulti.all()[0].get('folder_name'))
    return jsonify({'result': str(result_data)})

@app.route('/istwoimageequal', methods=['GET'])
def istwoimageequal():
    print('sigtable_data', sigtable.all())
    training_img_path = app.config['UPLOAD_FOLDER']+sigtable.all()[0].get('training_img')
    test_img_path = app.config['UPLOAD_FOLDER']+sigtable.all()[0].get('test_img')
    result_data = checktwoimg.isTwoImageEqual(training_img_path,test_img_path)
    return jsonify({'result': str(result_data)})

if __name__ == '__main__':
    app.run()
