import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("./cloud-django-blog-a8ea599ae3d0.json")
firebase_admin.initialize_app(cred)
