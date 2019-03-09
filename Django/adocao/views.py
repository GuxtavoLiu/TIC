from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.


#Cria uma classe com herança de templateview para exibir
#um arquivo html normal (com conteudo dele)
class PaginaInicialView(TemplateView):
    # Nome do arquivo que vai ser utilizado para renderizar
    # esta pagina/metodo/classe
    template_name = "index.html"

class SobreView(TemplateView):
        # Nome do arquivo que vai ser utilizado para renderizar
        # esta pagina/metodo/classe
        template_name = "sobre.html"
