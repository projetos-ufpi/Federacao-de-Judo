from django.conf.urls import url

from . import views

from django.contrib.auth.views import login


urlpatterns = [
    url(r'^$', views.index, name='index.html'),
    url(r'^index$', views.index, name='index.html'),
    url(r'^sobre$', views.sobre, name='sobre.html'),
    url(r'^cadastro_usuario$', views.cadastro_usuario, name='cadastro_usuario.html'),
    url(r'^eventos$', views.eventos, name='eventos.html'),
    url(r'^rankings$', views.rankings, name='rankings.html'),
    url(r'^administracao$', views.administracao, name='administracao.html'),
    url(r'^login$', views.login, name='login.html'),
    url(r'^cadastro_eventos$', views.cadastro_eventos, name='cadastro_eventos.html'),
    url(r'^fale_conosco$', views.fale_conosco, name='fale_conosco.html'),
    url(r'^cadastro_academias$', views.cadastro_academias, name='cadastro_academias.html'),
    url(r'^interface_usuario$', views.interface_usuario, name='interface_usuario.html'),
    url(r'^academias$', views.academias, name="academias.html"),
<<<<<<< HEAD
=======
    url(r'^informacoes_eventos$', views.informacoes_eventos, name='informacoes_eventos.html'),
<<<<<<< HEAD
    url(r'^cadastro_noticias$', views.cadastro_noticias, name='cadastro_noticias.html'),
=======
>>>>>>> 266fb7ca451a03d65eda446e8e797fe3a8be4cc7
>>>>>>> aa00b2c69e1198a3b59fa1a572efd96ca48a70d6
]
