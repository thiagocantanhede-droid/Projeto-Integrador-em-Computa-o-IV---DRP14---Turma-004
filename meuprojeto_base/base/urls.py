from django.urls import path
from. import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('entradas/',views.additem, name="entradas"),
    path('saidas/', views.subitem, name="saídas"),
    path('login/', views.logar, name="login"),
    path('logout/', views.deslogar, name="logout"),
]