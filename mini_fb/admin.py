from django.contrib import admin

# Register your models here.
from .models import Profile

admin.site.register(Profile)

from .models import StatusMessage

admin.site.register(StatusMessage)
