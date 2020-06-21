
import flask
from flask import request, jsonify, Response, json
from flask_pymongo import PyMongo
import image_classification_model as ml_model
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
import os

app = flask.Flask(__name__)
CORS(app)

### swagger specific ###
SWAGGER_URL = '/api/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Image Classification - Sara Yarshenas"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###


@app.route('/api/history', methods=['GET'])
def get_classifier_history():
    predictions = mongo.db.Predictions
    output = []
    for pred_doc in predictions.find():
        pred_obj = get_prediction_object(pred_doc)
        output.append(pred_obj)
    return jsonify({'result': output})


@app.route('/api/predict', methods=['POST'])
def make_prediction():
    try:
        if 'image' not in request.json:
            return Response(json.dumps({'Error': 'No valid image url found'}), status=400, mimetype="application/json")

        predictions = mongo.db.Predictions
        image_path = request.json['image']
        # Test data on ML model
        classifier_result = ml_model.image_classifier_model(image_path)
        if classifier_result is None:
            return Response(json.dumps({'Error': 'Url is not a valid image'}), status=400, mimetype="application/json")

        classes = []
        for res in classifier_result:
            classes.append({"type": res[1], "score": round(res[2].item(), 8)})

        # Insert the object to DB
        output = {'image_path': image_path, 'prediction_result': classes}
        predictions.insert(output)
        return jsonify({'result': {'image_path': image_path, 'prediction_result': classes}})
    except Exception as e:
        print(e)
        return Response(json.dumps({'Error': 'Internal Server Error'}), status=500, mimetype="application/json")


def get_prediction_object(prediction_doc):
    classes = []
    for top_cat in prediction_doc['prediction_result']:
        classes.append({'type': top_cat['type'], 'score': top_cat['score']})
    return {'image_path': prediction_doc['image_path'], 'prediction_result': classes}


app.config.from_pyfile("config.py")

mongo = PyMongo(app)
app.run(host='0.0.0.0', port=os.environ.get('ML_APP_PORT', default=8080))