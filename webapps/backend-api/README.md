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

## Response Example
GET ```http://0.0.0.0:8000/api/search/?query=crahels&type=username```
```json
[
  {"pk": "281956222", "username": "crahels", "full_name": "Rachel Sidney", "is_private": false, "profile_picture": "https://scontent-sin2-2.cdninstagram.com/vp/253b5d2ea2ee4b3c8b605729dbb3a5a0/5C71630F/t51.2885-19/s150x150/28427463_1636182853156624_1578679027089014784_n.jpg"}, 
  {"pk": "3651846030", "username": "lapakcrahels", "full_name": "Lapak Crahels", "is_private": false, "profile_picture": "https://scontent-sin2-2.cdninstagram.com/vp/0b4429120fa0854693238c945a255e08/5C6B5ECB/t51.2885-19/s150x150/13740989_1763816027173428_2146260344_a.jpg"}, 
  {"pk": "8956070866", "username": "c.rahel_spamz", "full_name": "", "is_private": true, "profile_picture": "https://scontent-sin2-2.cdninstagram.com/vp/b74b9aaf585c684c1a332d17650c56bf/5C7423C4/t51.2885-19/s150x150/42760747_1573765122723481_7043006497193721856_n.jpg"}
]
```

GET ```http://0.0.0.0:8000/api/user/crahels/```
```json
{
  "full_name": "Rachel Sidney", 
  "id": "281956222", 
  "is_private": false, 
  "username": "crahels", 
  "profile_picture": "https://scontent-sin2-2.cdninstagram.com/vp/253b5d2ea2ee4b3c8b605729dbb3a5a0/5C71630F/t51.2885-19/s150x150/28427463_1636182853156624_1578679027089014784_n.jpg"
}
```

GET ```http://0.0.0.0:8000/api/user/604334652/feed```
```json
[
  {
    "timestamp": 1391349939, "shortcode": "j6ppNVSLdh", "image_url": "https://scontent-sin2-2.cdninstagram.com/vp/a9b2a968c0eedf4645dcf1ac3a225db8/5C6B3BA7/t51.2885-15/e15/927850_397727170370929_836143702_n.jpg", "caption": "siap untuk dibedah bsk..", "type": "image", 
    "comments": [
      {"id": "17845325281046653", "text": "waduh", "created_at": 1391351753, "owner": {"id": "422415301", "profile_pic_url": "https://scontent-sin2-2.cdninstagram.com/vp/9886ce0f57fb0771c39b20057d989c50/5C6D80FC/t51.2885-19/s150x150/14134885_1084812971610814_2063615205_a.jpg", "username": "andriyanye"}, "created_time": "1391351753", "from": {"id": "422415301", "profile_picture": "https://scontent-sin2-2.cdninstagram.com/vp/9886ce0f57fb0771c39b20057d989c50/5C6D80FC/t51.2885-19/s150x150/14134885_1084812971610814_2063615205_a.jpg", "username": "andriyanye", "full_name": ""}}, 
      {"id": "17845503532046653", "text": "kasihan yg udah RIP", "created_at": 1391421478, "owner": {"id": "180022196", "profile_pic_url": "https://scontent-sin2-2.cdninstagram.com/vp/80b536beebba8ce187c0ef686b06f99b/5C722A6E/t51.2885-19/s150x150/20686654_1429565167151376_2762488398890401792_a.jpg", "username": "jesslynsulaiman"}, "created_time": "1391421478", "from": {"id": "180022196", "profile_picture": "https://scontent-sin2-2.cdninstagram.com/vp/80b536beebba8ce187c0ef686b06f99b/5C722A6E/t51.2885-19/s150x150/20686654_1429565167151376_2762488398890401792_a.jpg", "username": "jesslynsulaiman", "full_name": ""}}
    ]
  }, 
  {
    "timestamp": 1381562688, "shortcode": "fW98VKSLcY", "image_url": "https://scontent-sin2-2.cdninstagram.com/vp/63631b83a6d840a2c15b4b44fdc1ec35/5BE0DEF7/t51.2885-15/e15/11350728_416621895211665_1733837989_n.jpg", "caption": "My first instavideo #likeforlike #likeforfollow", "type": "video", 
    "comments": [
      {"id": "17845230715046653", "text": "Suaranya knp gitu? @wijayaerick", "created_at": 1381575194, "owner": {"id": "15386801", "profile_pic_url": "https://scontent-sin2-2.cdninstagram.com/vp/df0e87dbd8eb0770a7bed7cff5535bbf/5C74C2B1/t51.2885-19/s150x150/36054632_224960871562029_8131916779883593728_n.jpg", "username": "gebbytrivena"}, "created_time": "1381575194", "from": {"id": "15386801", "profile_picture": "https://scontent-sin2-2.cdninstagram.com/vp/df0e87dbd8eb0770a7bed7cff5535bbf/5C74C2B1/t51.2885-19/s150x150/36054632_224960871562029_8131916779883593728_n.jpg", "username": "gebbytrivena", "full_name": ""}}
    ]
  }
]
```
