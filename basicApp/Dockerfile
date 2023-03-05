FROM python:3.7.6-buster

WORKDIR /app
COPY ./ /app
COPY requirements.txt /tmp/
RUN pip install --upgrade pip

RUN pip3 install --no-cache -r /tmp/requirements.txt

ENTRYPOINT ["python", "flask_app.py"]