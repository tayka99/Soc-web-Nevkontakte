from django.contrib.admin import site
from  .models import Post, Event, Profile

site.register(Post)
site.register(Profile)
site.register(Event)
