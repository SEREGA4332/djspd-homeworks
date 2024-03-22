from django.contrib import admin

# зарегистрируйте необходимые модели
from main.models import Car


admin.site.register(Car)
