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
2. GET ```/api/user/<username>``` - Get user info and media shortcodes
3. GET ```/api/media/<shortcode>``` - Get media info and analyzer results

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
  "profile_picture": "https://scontent-sin6-1.cdninstagram.com/vp/253b5d2ea2ee4b3c8b605729dbb3a5a0/5C71630F/t51.2885-19/s150x150/28427463_1636182853156624_1578679027089014784_n.jpg",
  "edge_owner_to_timeline_media": {
    "count": 1,
    "page_info": {
      "has_next_page": false,
      "end_cursor": null
    },
    "media": [
      {
        "created_time": 1504255022,
        "shortcode": "BYfe__ADtT2",
        "display_url": "https://scontent-sin6-1.cdninstagram.com/vp/e34022106efa00f896ad4955e4d4c31e/5C70C084/t51.2885-15/e35/21294305_323883801406638_9060648787004882944_n.jpg"
      }
    ]
  }
}
```

GET ```http://0.0.0.0:8000/api/media/BYfe__ADtT2```
```json
{
  "shortcode": "BYfe__ADtT2",
  "display_url": "https://scontent-sin6-1.cdninstagram.com/vp/e34022106efa00f896ad4955e4d4c31e/5C70C084/t51.2885-15/e35/21294305_323883801406638_9060648787004882944_n.jpg",
  "created_time": "1504255022",
  "caption": "A ship is always safe at shore but that is not what it's built for. #tb #bali #indonesia",
  "carousel_display_urls": [
    "https://scontent-sin6-1.cdninstagram.com/vp/e34022106efa00f896ad4955e4d4c31e/5C70C084/t51.2885-15/e35/21294305_323883801406638_9060648787004882944_n.jpg",
    "https://scontent-sin6-1.cdninstagram.com/vp/b5bfd294e6ebd341f94e33cefe517491/5C7406F5/t51.2885-15/e35/21227457_1892651334084067_5067138523887304704_n.jpg",
    "https://scontent-sin6-1.cdninstagram.com/vp/d745880a5e0674d12e840c22c0660889/5C87A6E5/t51.2885-15/e35/21149082_1817627091881280_9222357063068286976_n.jpg"
  ],
  "edge_media_to_comment": {
    "count": 5,
    "page_info": {
      "has_next_page": false,
      "end_cursor": null
    },
    "comments": [
      {
        "comment": {
          "created_time": 1504255464,
          "text": "Sudah kayak chairil anwar ya ponakanku",
          "username": "iwtan",
          "profile_picture": "https://scontent-sin6-1.cdninstagram.com/vp/ae53120bb4722e4cbef9bf9d99a1a32b/5C7BCC43/t51.2885-19/s150x150/35617322_1882947792005369_1187511328667860992_n.jpg",
          "hate_score": {
            "physic": 0,
            "race": 0,
            "religion": 0
          }
        }
      },
      {
        "comment": {
          "created_time": 1504256518,
          "text": "Ada lumba2 gaa chel?",
          "username": "silvyanggun",
          "profile_picture": "https://scontent-sin6-1.cdninstagram.com/vp/c9c66e30cc41888a1e928c9c3873f7b6/5C676992/t51.2885-19/s150x150/43621874_571021223346553_3669966468289658880_n.jpg",
          "hate_score": {
            "physic": 0,
            "race": 0,
            "religion": 0
          }
        }
      },
      {
        "comment": {
          "created_time": 1504257343,
          "text": "HUEHEHE keren ya brrti @iwtan ; ada tp dikiiiiit lumba\"nya malu\" sil @silvyanggun ; iya ini aku yg gambar(?) wkakw @stevenandianto",
          "username": "crahels",
          "profile_picture": "https://scontent-sin6-1.cdninstagram.com/vp/253b5d2ea2ee4b3c8b605729dbb3a5a0/5C71630F/t51.2885-19/s150x150/28427463_1636182853156624_1578679027089014784_n.jpg",
          "hate_score": {
            "physic": 0,
            "race": 0,
            "religion": 0
          }
        }
      },
      {
        "comment": {
          "created_time": 1504257422,
          "text": "Wkwkwk oh ya?? Jam ber kamu kesana? Pas sunset ya? 😂",
          "username": "silvyanggun",
          "profile_picture": "https://scontent-sin6-1.cdninstagram.com/vp/c9c66e30cc41888a1e928c9c3873f7b6/5C676992/t51.2885-19/s150x150/43621874_571021223346553_3669966468289658880_n.jpg",
          "hate_score": {
            "physic": 0,
            "race": 0,
            "religion": 0
          }
        }
      },
      {
        "comment": {
          "created_time": 1504261048,
          "text": "Pngen kesana:(",
          "username": "elvinahertanu_008",
          "profile_picture": "https://scontent-sin6-1.cdninstagram.com/vp/c3c7d425af23dfbdface51865281cc6c/5C754A56/t51.2885-19/s150x150/1661210_1552663505045390_1999571810_a.jpg",
          "hate_score": {
            "physic": 0,
            "race": 0,
            "religion": 0
          }
        }
      }
    ]
  }
}
```
