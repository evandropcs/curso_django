from django.contrib import admin

from .models import Curso
from .models import Autor

admin.site.register(Curso)
admin.site.register(Autor)
