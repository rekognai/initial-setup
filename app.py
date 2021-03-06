import logging

import boto3
from flask import Flask, request
from werkzeug.utils import secure_filename

from config import ACCESS_KEY, SECRET_KEY

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
s3_client = boto3.client("s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)


# api for uploading files to s3
@app.route("/uploadToS3", methods=['POST'])
def hello():
    file = request.files['file']
    filename = secure_filename(file.filename)
    app.logger.info("incoming file: " + filename)
    s3_client.upload_fileobj(file, 'rekognai-test', filename)
    return filename


app.run()
