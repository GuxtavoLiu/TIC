    # modulo do django para criar urls
from django.urls import path
    # import todas suas classes do view.py
from .views import *

urlpatterns = [
     # path(
     # 'caminho/da/url',
     #  ClasseLáDoView.as view(),
     #   name = "nomeDessaUrl")
     path('', PaginaInicialView.as_view(), name="index"),
     path('sobre', SobreView.as_view(), name="sobre")
]
