from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import requests
import uuid
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def download_file(url):
    accepted_formats = set(['image/png', 'image/jpeg', 'image/jpg'])
    if not os.path.exists('Classifier_Images'):
        os.makedirs('Classifier_Images')
    r = requests.get(url)
    if r.status_code == 200 and r.headers['Content-Type'].lower() in accepted_formats:
        file_path = './Classifier_Images/'+str(uuid.uuid4())
        with open(file_path, 'wb') as f:
            f.write(r.content)
        return file_path
    else:
        return None


def image_classifier_model(img_url):
    model = ResNet50(weights='imagenet')
    img_path = download_file(img_url)
    if img_path is None:
        return None
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    return decode_predictions(preds, top=3)[0]


