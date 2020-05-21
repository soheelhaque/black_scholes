FROM python:3.7-slim
WORKDIR /tests
ENV DOCKERIZE_VERSION v0.6.1
RUN apt-get update && apt-get install -y wget
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
ADD . /tests
RUN pip install requests
RUN pip install pytest
CMD ["python", "smoke_test.py"]