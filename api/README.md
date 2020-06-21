Requirements:
Python 3


To run the project locally:

### `git clone https://github.com/sarahysh12/image_classification.git`

go to the directory and install dependencies by running:

### `pip install -r requirement.txt`

Now you can run the restful app by:

### `python app.py`

To try the endpoints you can refer to Swagger API documentation at:
'https://localhost:8080/api/swagger'

There is an endpoint to do the prediction for an image:

Method: POST
URL: 'https://localhost:8080/api/predict'


To get all the predictions history:

Method: GET
URL: 'https://localhost:8080/api/history'