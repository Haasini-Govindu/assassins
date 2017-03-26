FROM python:2.7
ADD . /code
WORKDIR /code
RUN apt-get install libpq-dev
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_DB="postgresql+psycopg2://postgres:nwuf89@postgres/postgres"
# RUN python create_db.py
CMD "./go.sh"