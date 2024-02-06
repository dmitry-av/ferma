FROM python:3.10-slim

WORKDIR /app
ADD ./requirements.txt /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt
ADD . /app