# Hate Speech Analyzer - Back-End API
IF4072 Natural Language & Text Processing

## Overview
This is the back-end API of Hate Speech Analyzer app. It uses [unofficial Instagram API Python wrapper](https://github.com/ping/instagram_private_api) 
to get media comments and the [trained model](https://github.com/tugas-itb-erick/hate-speech-analyzer/tree/master/notebook) 
to analyze hate speech from comments. 

## Running The API
### 1. With Docker
Run ```docker-compose up```. The API will be running on 0.0.0.0:8000.  
### 2. Without Docker
Run```python manage.py runserver <HOST:PORT>```. The API will be running on HOST:PORT. Do not forget to install the dependencies. 
#### Dependencies
1. [Python>=3](https://www.python.org/downloads/)
2. [Django>=2](https://www.djangoproject.com/download/)
3. [instagram_private_api==1.5.7](https://github.com/ping/instagram_private_api#install)

## API Reference
1. GET ```/api/search?query=[string]&type=[username|tag]``` - Perform search by name/tag
2. GET ```/api/user/<username>``` - Get user info
3. GET ```/api/user/<user_id>/feed``` - Get user feed (comments with analysis result)
