from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index.html'),
    url(r'^sobre$', views.sobre, name='sobre.html'),
    url(r'^cadastro_usuario$', views.cadastro_usuario, name='cadastro_usuario.html'),
    url(r'^eventos$', views.eventos, name='eventos.html'),
    url(r'^rankings$', views.rankings, name='rankings.html'),
    url(r'^administracao$', views.administracao, name='administracao.html'),
    url(r'^login$', views.login, name='login.html'),
    url(r'^cadastro_eventos$', views.cadastro_eventos, name='cadastro_eventos.html'),
    url(r'^fale_conosco$', views.fale_conosco, name='fale_conosco.html'),
]
