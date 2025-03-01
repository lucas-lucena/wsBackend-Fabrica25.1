FROM python:3.11-slim

WORKDIR /app_rotten_potatoes

COPY . /app_rotten_potatoes
COPY ./requirements.txt /app_rotten_potatoes/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]