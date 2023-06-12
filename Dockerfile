FROM python:3.10.6-buster


# Install dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# Install the Movie sentiment package
COPY movie_sentiment / movie_sentiment
COPY setup.py setup.py
RUN pip install --upgrade pip

#
COPY Makefile Makefile
RUN make clean


CMD uvicorn movie_sentiment.ml_logic.movie_app:app --host 0.0.0.0
