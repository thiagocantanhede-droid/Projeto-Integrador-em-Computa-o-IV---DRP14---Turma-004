from django.urls import path
from. import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('entradas/',views.additem, name="Entradas"),
    path('cadastro/',views.register, name="Cadastro"),
    path('saidas/', views.subitem, name="Saídas"),
    path('login/', views.logar, name="login"),
    path('logout/', views.deslogar, name="logout"),
    path('servidor/<str:pk>/', views.servidor, name="Página do Servidor"),
    
    path('retorno_celular/<str:pk>/', views.servidor_celular, name="Retorno Celular"),
    path('retorno_notebook/<str:pk>/', views.servidor_notebook, name="Retorno Notebook"),

    path('listagem_servidores/', views.lista_servidores, name="Listagem de Servidores"),
    path('listagem_item/', views.lista_itens, name="Listagem de Itens"),
    path('listagem_celular/', views.lista_celulares, name="Listagem de Celulares"),
    path('listagem_notebook/', views.lista_notebooks, name="Listagem de Notebooks"),


    path('item/<str:pk>/', views.paginaitem, name="Página do Item"),
    path('material/<str:pk>/', views.paginamaterial, name="Página do Material"),
    path('entradas_saidas/', views.entrada_saida, name="Entradas e Saídas"),
    path('celular/<str:pk>/', views.paginacelular, name="Página do Celular"),
    path('notebook/<str:pk>/', views.paginanotebook, name="Página do Notebook"),


    path('generate-pdf-lista-itens/', views.generate_pdf_view_lista_itens, name="generate-pdf-lista-itens"),
    path('generate-sheet-lista-itens/', views.generate_sheet_view_lista_itens, name="generate-sheet-lista-itens"),

    path('generate-pdf-lista-celulares/', views.generate_pdf_view_lista_celulares, name="generate-pdf-lista-celulares"),
    path('generate-sheet-lista-celulares/', views.generate_sheet_view_lista_celulares, name="generate-sheet-lista-celulares"),

    path('generate-pdf-lista-notebooks/', views.generate_pdf_view_lista_notebooks, name="generate-pdf-lista-notebooks"),
    path('generate-sheet-lista-notebooks/', views.generate_sheet_view_lista_notebooks, name="generate-sheet-lista-notebooks"),
    path('generate-pdf-servidor/<str:pk>/', views.generate_pdf_view_servidor, name="generate-pdf-servidor"),


]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
