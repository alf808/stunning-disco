from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import requests
import base64

app = Flask(__name__)
api = Api(app)

app_id = None
app_key = None
base_url = 'https://api.kairos.com/'

auth_headers = {
    'app_id': app_id,
    'app_key': app_key
}

def validate_settings():
    if app_id is None:
        raise Exception('Kairos app_id was not set')
    if app_key is None:
        raise Exception('Kairos app_key was not set')

def validate_file_and_url_presence(file, url):
    if not file and not url:
        raise ValueError('An image file or valid URL must be passed')
    if file and url:
        raise ValueError('Cannot receive both a file and URL as arguments')

def _extract_base64_contents(image_path):
    with open(image_path, 'rb') as fp:
        return base64.b64encode(fp.read()).decode('ascii')


class Recognize(Resource):
    def post(self):
        _base_url = base_url + 'recognize'
        posted_data = request.get_json()
        gallery_name = posted_data.get('gallery_name')
        url = posted_data.get('url')
        file = posted_data.get('file')

        validate_settings()
        validate_file_and_url_presence(file, url)

        ret_dict = _build_response(gallery_name, url, file)

        response = requests.post(_base_url, json=ret_dict, headers=auth_headers)
        json_response = response.json()
        if response.status_code != 200 or 'Errors' in json_response:
            raise Exception(response.status_code, json_response, ret_dict)

        return json_response

def _build_response(gallery_name, url, file):
    if file is not None:
        image = _extract_base64_contents(file)
    else:
        image = url

    required_fields = {
        'image': image,
        'gallery_name': gallery_name
    }

    return dict(required_fields)


class AddFace(Resource):
    def post(self):
        _base_url = base_url + 'enroll'
        posted_data = request.get_json()
        subject_id = posted_data.get('subject_id')
        gallery_name = posted_data.get('gallery_name')
        url = posted_data.get('url')
        file = posted_data.get('file')

        validate_settings()
        validate_file_and_url_presence(file, url)

        ret_dict = _build_enroll_response(subject_id, gallery_name, url, file)

        response = requests.post(_base_url, json=ret_dict, headers=auth_headers)
        json_response = response.json()
        if response.status_code != 200 or 'Errors' in json_response:
            raise Exception(response.status_code, json_response, ret_dict)

        return json_response

def _build_enroll_response(subject_id, gallery_name, url, file, imgframe=None):
    if imgframe is not None:
        image = imgframe
    elif file is not None:
        image = _extract_base64_contents(file)
    else:
        image = url
    required_fields = {'image': image, 'subject_id': subject_id,
                       'gallery_name': gallery_name}

    return dict(required_fields)


class Verify(Resource):
    def post(self):
        _base_url = base_url + 'verify'
        posted_data = request.get_json()
        subject_id = posted_data.get('subject_id')
        gallery_name = posted_data.get('gallery_name')
        url = posted_data.get('url')
        file = posted_data.get('file')

        validate_settings()
        validate_file_and_url_presence(file, url)

        ret_dict = _build_verify_response(subject_id, gallery_name, url, file)

        response = requests.post(_base_url, json=ret_dict, headers=auth_headers)
        json_response = response.json()
        if response.status_code != 200 or 'Errors' in json_response:
            raise Exception(response.status_code, json_response, ret_dict)

        return json_response

def _build_verify_response(subject_id, gallery_name, url, file):
    if file is not None:
        image = _extract_base64_contents(file)
    else:
        image = url
    required_fields = {'image': image, 'subject_id': subject_id,
                       'gallery_name': gallery_name}

    return dict(required_fields)


api.add_resource(Recognize, '/recognize')
api.add_resource(AddFace, '/addface')
api.add_resource(Verify, '/verify')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
