FROM python:3.9.18

WORKDIR /home/ubuntu/mlopspipeline/docker/flaskapp/app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR ./app

CMD gunicorn main:app --bind 0.0.0.0:5000

EXPOSE 5000
