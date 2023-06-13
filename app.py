import sys,os
from signLanguage.pipeline.train_pipeline import TrainPipeline
from signLanguage.exception import SignException
from signLanguage.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin


APP_HOST = "0.0.0.0"
APP_PORT = 8080


app = Flask(__name__)
CORS(app)

# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successfull!!" 







if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT)