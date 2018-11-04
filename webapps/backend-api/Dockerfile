FROM python:3
RUN mkdir /code
COPY . /code 
WORKDIR /code 
RUN pip install -r requirements.txt
RUN pip install git+https://git@github.com/ping/instagram_private_api.git@1.5.7
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]