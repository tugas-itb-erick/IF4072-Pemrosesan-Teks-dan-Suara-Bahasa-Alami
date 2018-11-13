# Hate Speech Analyzer - Web Application
IF4072 Natural Language & Text Processing

## Overview
This is the web app Hate Speech Analyzer app. It uses [unofficial Instagram API Python wrapper](https://github.com/ping/instagram_private_api) 
to get media comments and the [trained model](https://github.com/tugas-itb-erick/hate-speech-analyzer/tree/master/webapps/app/trained_models) 
to analyze hate speech from comments. 

## Running The Web
### 1. With Docker
Run ```docker-compose up```. The web will be running on 0.0.0.0:8000.
### 2. Without Docker
Run ```python manage.py runserver <HOST:PORT> --nothreading```. The web will be running on HOST:PORT. Do not forget to install the dependencies. 
#### Dependencies
See [requirements.txt](https://github.com/tugas-itb-erick/hate-speech-analyzer/tree/master/webapps/requirements.txt). 

## Endpoint Reference
1. ```/app``` - Home
2. ```/app/search?query=[string]&type=[username|tag]``` - Perform search by name/tag
3. ```/app/user/<username>``` - Get user info and media shortcodes
4. ```/app/media/<shortcode>``` - Get media info and analyzer results
