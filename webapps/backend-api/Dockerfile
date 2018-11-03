FROM python:3
RUN mkdir /code
COPY . /code 
WORKDIR /code 
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "8080"]
