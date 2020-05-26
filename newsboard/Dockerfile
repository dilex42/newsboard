# Use an official Python runtime as a parent image
FROM python:3.7

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip && pip install -r /code/requirements.txt


COPY . /code/
WORKDIR /code/

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN useradd newsboard && chown -R newsboard /code
USER newsboard

EXPOSE 8000
