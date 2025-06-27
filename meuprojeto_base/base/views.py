from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from django.contrib import messages
from .models import Item, Armario, Tamanho, Usuario
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):

    context = {}

    return render(request, 'home.html', context)

def additem(request):

    items = Item.objects.all()
    quantidade = []
    for i in range(100):
        quantidade.append(i)
    if request.method == 'POST':
        obj = get_object_or_404(Item, pk=request.POST.get("item"))
        quantidade = request.POST.get("quantidade")
        form = ItemForm(request.POST, instance=obj)
        if form.is_valid():
           item = form.save(commit=False)
           item_obj = Item.objects.get(pk=item.id)
           item.name = item_obj.name
           item.quantidade = item_obj.quantidade + int(quantidade)
           item.armario = item_obj.armario
           item.cautela = item_obj.cautela
           item.patrimonio = item_obj.patrimônio
        
           item.save()
           return redirect('home')
        else:
            print(form.errors)

    context = {'items':items, 'quantidade': quantidade}

    return render(request, 'form_entrada.html', context)

def subitem(request):

    items = Item.objects.all()
    quantidade = []
    for i in range(100):
        quantidade.append(i)
    if request.method == 'POST':
        obj = get_object_or_404(Item, pk=request.POST.get("item"))
        quantidade = request.POST.get("quantidade")
        form = ItemForm(request.POST, instance=obj)
        if form.is_valid():
           item = form.save(commit=False)
           item_obj = Item.objects.get(pk=item.id)
           item.name = item_obj.name
           item.armario = item_obj.armario
           item.cautela = item_obj.cautela
           item.quantidade = item_obj.quantidade - int(quantidade)
           item.patrimonio = item_obj.patrimônio
        
           item.save()
           return redirect('home')
        else:
            print(form.errors)

    context = {'items':items, 'quantidade': quantidade}

    return render(request, 'form_saida.html', context)

def logar(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Usuario.objects.get(email=email)
        except:
            messages.error(request, 'Usuário não existe')
        user = authenticate(request, email=email, password=password)
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email ou senha inválidos ou inexistentes')

    context = {'page':page}
    return render(request, 'login.html', context)

def deslogar(request):
    logout(request)
    return redirect('home')

