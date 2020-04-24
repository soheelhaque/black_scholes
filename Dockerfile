FROM python:3.7-slim
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org Flask
RUN pip install --trusted-host pypi.python.org connexion[swagger-ui]
RUN pip install --trusted-host pypi.python.org scipy
EXPOSE 5000
CMD ["python", "app.py"]