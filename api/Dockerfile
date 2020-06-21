FROM python:3.8

ADD requirement.txt /ml_app/
RUN pip install -r /ml_app/requirement.txt

ADD app.py /ml_app/
ADD image_classification_model.py /ml_app/
ADD static/swagger.json /ml_app/static/
ADD config.json /ml_app/

WORKDIR /ml_app
CMD python app.py


