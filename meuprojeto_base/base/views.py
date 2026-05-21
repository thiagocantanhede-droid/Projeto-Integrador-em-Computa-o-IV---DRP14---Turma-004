from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from django.contrib import messages
from .models import Item, Armario, Usuario, Material, Celular, Notebook
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from urllib.parse import urlsplit
from django.urls import resolve, path, Resolver404
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from weasyprint import HTML
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
import pandas as pd
from django.db.models import Q


# Create your views here.

def home(request):

    
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    itens = Item.objects.filter(
        Q(name__icontains=q) |
        Q(patrimônio__icontains=q) |
        Q(armario__armario__icontains=q)     
    )
    celulares = Celular.objects.filter(
        Q(cautela__username__icontains=q) |
        Q(IMEI__icontains=q) |
        Q(numero__icontains=q) |
        Q(modelo__icontains=q)
    )
    notebooks = Notebook.objects.filter(
        Q(modelo__icontains=q) |
        Q(cautela__username__icontains=q)
    )
    servidores = Usuario.objects.filter(
        Q(username__icontains=q) |
        Q(matricula__icontains=q)
    )   

    context = {'itens':itens, 'celulares':celulares,
               'notebooks':notebooks, 'servidores':servidores, 'q':q}

    return render(request, 'home.html', context)
    
@login_required
def additem(request):
    items = Item.objects.filter(Q(patrimônio="") | 
                                Q(patrimônio=None))
    quantidade = []
    for i in range(100):
        quantidade.append(i)
    if request.method == 'POST':
        try:
            obj = get_object_or_404(Item, pk=request.POST.get("item"))
        except:
            messages.error(request, 'Os campos não foram devidamente preenchidos!')

        quantidade = request.POST.get("quantidade")
        if not quantidade or quantidade == 0 or quantidade == 'Selecione':
            messages.error(request, 'Os campos não foram devidamente preenchidos!')
            return redirect('Entradas')
        else:
            try:
                form = ItemForm(request.POST, instance=obj)
                if form.is_valid():
                    item = form.save(commit=False)
                    item_obj = Item.objects.get(pk=item.id)
                    item.name = item_obj.name
                    item.quantidade = item_obj.quantidade + int(quantidade)
                    item.armario = item_obj.armario
                    item.cautela_inicial = item_obj.cautela_inicial
                    item.patrimonio = item_obj.patrimônio
                    
                    item.save()
                    return redirect('home')

            except:
                messages.error(request, 'Os campos não foram devidamente preenchidos!')
                return redirect('Entradas')

    context = {'items':items, 'quantidade': quantidade}

    return render(request, 'form_entrada.html', context)

@login_required
def subitem(request):

    usuarios = Usuario.objects.all()
    items = Item.objects.all()
    quantidade = []
    for i in range(100):
        quantidade.append(i)
    try:
        if request.method == 'POST':
            obj = get_object_or_404(Item, pk=request.POST.get("item"))
            nome = obj.name
            tam = obj.tamanho
            quantidade = request.POST.get("quantidade")
            if int(quantidade) == 0:
                messages.error(request, 'Quantidade não pode ser igual a zero!')
                return redirect('Saídas')
            else:
                if obj.quantidade > 0:
                    if int(quantidade) <= obj.quantidade:
                        if not Material.objects.filter(name=nome).filter(tamanho=tam):
                            name = obj.name
                            cautela = Usuario.objects.get(pk=request.POST.get("cautela"))
                            armario = obj.armario
                            tamanho = obj.tamanho
                            patrimônio = obj.patrimônio
                            Material.objects.create(name=name, quantidade=quantidade, armario=armario, 
                                                cautela=cautela, tamanho=tamanho, 
                                                patrimônio=patrimônio, updated_by=request.user)
                            obj.quantidade = obj.quantidade - int(quantidade)
                            obj.save()

                            return redirect('home')
                        else:
                            mat = get_object_or_404(Material, name=nome, tamanho=tam)
                            print(mat)
                            mat.quantidade += int(quantidade)
                            mat.save()
                            obj.quantidade = obj.quantidade - int(quantidade)
                            obj.save()


                            return redirect('home')
                    else:
                        messages.error(request, f'Não há itens suficientes em estoque! {obj.quantidade} unidades restantes!')
                        return redirect('Saídas')
                else:
                    messages.error(request, 'Os campos não foram devidamente preenchidos!')
                    return redirect('Saídas')
    except:
        messages.error(request, 'Os campos não foram devidamente preenchidos!')
        return redirect('Saídas')

        
    context = {'items':items, 'quantidade': quantidade, 'usuarios':usuarios}

    return render(request, 'form_saida.html', context)

@login_required
def register(request):

    items = ["Algema plástica"," Arame Lacre Laranja"," Barraca NTK Panda 3"," Bermuda Masc.","Boné com Capa",
    "Boné Ibama"," Boné Legionário"," Bota Galocha"," Bota SL Branca"," Bota SL Pró Preta"," Bota Térmica",
    "Botas Seasub","Calça"," Calça Fem."," Calça Masc."," Calça/Bermuda Masc"," Camisa  Fisc. Manga Curta",
    "Camisa  Fisc. Manga Longa "," camisa polo"," Camiseta Branca manga curta"," Camiseta Branca manga longa",
    "Camiseta Verde manga longa"," Cantil"," Capa de Chuva Comum"," Capa de Chuva Morcego Reflexiva",
    "Capa de Chuva Morcego S/Refletores "," Capa de chuva Neon","Capa Externa de Colete Balístico  PROTECTA - VERDE",
    "Capa Externa de Colete Balístico  TAURUS - PRETA"," capa impermeável p/mochila rusher"," Capa para Cantil",
    "Capacete 3M Branco"," Capacete de segurança UMP Amarelo "," Chapéu com Proteção "," Cinto Tático  "," Cinto Tático Underbelt",
    "Cintos Verde"," Colete de Segurança"," Colete em X Verde e Branco "," Colete Fisc."," Colete Flotek"," Colete Laranja e Branco",
    "Colete Reflexivo"," Coturno"," Coturno Prevfogo"," Encaixe Toyota p/ Calota"," Facão"," Fita adesiva larga - IBAMA/MMA"," Gandola ",
    "Japona Térmica"," Jaqueta com forro"," Laminado Respirável"," Lanterna de Cabeça ALFACELL"," Luva Latéx Descartável Volk"," Luva Nitrilica-Tam-Único",
    "Luvas de vaqueta Alseg – CA 25368"," Macacão Flytec"," Macacão Impermeável Laminado"," Manta Alcochoada"," Máscara PFF1"," Mochila"," Mochila de Salvamento",
    "Mochila IBAMA"," Mochila Rusher 40L Verde"," Mochilas de Hidratação KALAHARI"," Mucambo Pro AF 15"," Óculos de proteção Kalipso"," Perneira  "," Perneira Sayro - CA 14750",
    "Porta Rádio"," Porta utilidades P/ Cinto"," Protetor auricular silicone – CA 18189"," Regulador de capacete"," Sapato Couro"," Sobretudo Impemeável "," Touca TNT Descartável",
    "Trena de Fibra"," Headset Logitech"," Camera WEBCAM Gotech"," Kit Identificador de Gás Refrigerante"]
    usuarios = Usuario.objects.all()
    armarios = Armario.objects.all()
    tamanhos = ["XG","Único","PP","P","M","G","EG","52","50","48","46","44","43","42","41","39","38","37","36","35","34","13"]
    quantidade = []
    erro = "Item já existe!"
    for i in range(100):
        quantidade.append(i)
    if request.method == 'POST':
        nome = request.POST.get('item')
        quantity = request.POST.get('quantidade')
        patrimonio = request.POST.get('patrimônio')
        criado_por = request.user
        armario = request.POST.get('armario')
        tamanho = request.POST.get('tamanho')
        cautela_inicial = Usuario.objects.get(username="DIPAM")


        if not nome or not quantity or not armario or not tamanho or quantidade == 0 or armario == "Selecione":
            messages.error(request, 'Os campos não foram devidamente preenchidos!')
        else:    
            if not Item.objects.filter(name=nome, tamanho=tamanho):
                Item.objects.create(
                    name=nome,
                    quantidade=quantity,
                    patrimônio=patrimonio,
                    updated_by=criado_por,
                    cautela_inicial=cautela_inicial,
                    armario=Armario.objects.get(pk=armario),
                    tamanho=tamanho
                )
                return redirect('home')
            else:
                messages.error(request, 'Item já existe!')

    context = {'items':items, 'quantidade': quantidade,
                'armarios':armarios, 'usuarios':usuarios,
                'tamanhos':tamanhos
                }

    return render(request, 'form_cadastro_item.html', context)


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

@login_required
def deslogar(request):
    logout(request)
    return redirect('home')

@login_required
def servidor(request, pk):
    user = Usuario.objects.get(pk=pk)
    materiais = user.material_set.all()
    celulares = user.celular_set.all()
    notebooks = user.cautela_notebooks.all()
    if request.method == "POST":
        material = Material.objects.get(pk=int(request.POST.get('item_id')))
        item = Item.objects.get(name=material.name, tamanho=material.tamanho)
        item.quantidade += material.quantidade
        item.save()
        material.delete()
        return redirect("Página do Servidor", pk=pk)

    context = {'user':user, 'materiais':materiais, 'celulares':celulares, 'notebooks':notebooks}
    return render(request, 'servidor.html', context)

@login_required
def servidor_celular(request, pk):
    if request.method == "POST":
        celular = Celular.objects.get(pk=request.POST.get('celular_id'))
        celular.cautela = Usuario.objects.get(username="DIPAM")
        celular.save()
    
    return redirect("Página do Servidor", pk=pk)

@login_required
def servidor_notebook(request, pk):
    if request.method == "POST":
        notebook = Notebook.objects.get(pk=request.POST.get('notebook_id'))
        notebook.cautela = Usuario.objects.get(username="DIPAM")
        notebook.save()
    
    return redirect("Página do Servidor", pk=pk)


@login_required
def lista_servidores(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios':usuarios}
    return render(request, 'listagem_servidores.html', context)

@login_required
def lista_itens(request):
    itens = Item.objects.all()
    context = {'itens':itens}
    return render(request, 'listagem_item.html', context)

@login_required
def lista_celulares(request):
    itens = Celular.objects.all()
    context = {'itens':itens}
    return render(request, 'listagem_celulares.html', context)

@login_required
def lista_notebooks(request):
    itens = Notebook.objects.all()
    context = {'itens':itens}
    return render(request, 'listagem_notebooks.html', context)

@login_required
def paginaitem(request, pk):
    item = Item.objects.get(pk=pk)

    context = {'item':item}
    return render(request, 'item.html', context)

@login_required
def paginamaterial(request, pk):
    material = Material.objects.get(pk=pk)
    referer_url = request.META.get('HTTP_REFERER')

    if request.method == "POST":
        material = Material.objects.get(pk=pk)
        usuario_id = material.cautela
        item = Item.objects.get(name=material.name, tamanho=material.tamanho)
        item.quantidade += material.quantidade
        item.save()
        material.delete()
        return redirect('Página do Servidor', pk=usuario_id.pk)

    context = {'material':material}
    return render(request, 'material.html', context)


@login_required
def paginacelular(request, pk):
    celular = Celular.objects.get(id=pk)

    usuarios = Usuario.objects.all()
    if request.method == "POST":
        nova_cautela = Usuario.objects.get(pk=int(request.POST.get('cautela')))
        celular.cautela = nova_cautela
        celular.save()


    context = {'celular':celular, 'usuarios':usuarios}
    return render(request, 'celular.html', context)

@login_required
def paginanotebook(request, pk):
    item = Notebook.objects.get(id=pk)

    usuarios = Usuario.objects.all()
    if request.method == "POST":
        nova_cautela = Usuario.objects.get(pk=int(request.POST.get('cautela')))
        item.cautela = nova_cautela
        item.save()


    context = {'item':item, 'usuarios':usuarios}
    return render(request, 'Notebook.html', context)


def breadcrumb(request):
    context = {}
    return render(request, 'breadcrumb.html', context)

@login_required
def entrada_saida(request):
    itens = Material.objects.all()

    context = {'itens':itens}
    return render(request, 'entradas_saidas.html', context)


def generate_pdf_view_lista_itens(request):
    itens = Item.objects.all()
    context = {'itens':itens}
    html_string = render_to_string('pdf/items.html', context)
    pdf = HTML(string=html_string, base_url=request.build_absolute_uri('/')).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="lista_itens.pdf"'
    return response

def generate_sheet_view_lista_itens(request):
    queryset = Item.objects.all().values()

    df = pd.DataFrame(list(queryset))

    df['created'], df['updated'] = df['created'].dt.tz_localize(None), df['updated'].dt.tz_localize(None)



    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="lista_de_itens.xlsx"'
    
    df.to_excel(response, engine='openpyxl', index=False)


    return response

def generate_pdf_view_lista_celulares(request):
    celulares = Celular.objects.all()
    context = {'celulares':celulares}
    html_string = render_to_string('pdf/celulares.html', context)
    pdf = HTML(string=html_string, base_url=request.build_absolute_uri('/')).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="lista_celulares.pdf"'
    return response

def generate_sheet_view_lista_celulares(request):
    queryset = Celular.objects.all().values()

    df = pd.DataFrame(list(queryset))

    df['created'], df['updated'] = df['created'].dt.tz_localize(None), df['updated'].dt.tz_localize(None)



    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="lista_de_celulares.xlsx"'
    
    df.to_excel(response, engine='openpyxl', index=False)


    return response

def generate_pdf_view_lista_notebooks(request):
    notebooks = Notebook.objects.all()
    context = {'notebooks':notebooks}
    html_string = render_to_string('pdf/notebooks.html', context)
    pdf = HTML(string=html_string, base_url=request.build_absolute_uri('/')).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="lista_notebooks.pdf"'
    return response

def generate_sheet_view_lista_notebooks(request):

    queryset = Notebook.objects.all().values()

    df = pd.DataFrame(list(queryset))

    df['created'], df['updated'] = df['created'].dt.tz_localize(None), df['updated'].dt.tz_localize(None)



    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="lista_de_notebooks.xlsx"'
    
    df.to_excel(response, engine='openpyxl', index=False)


    return response

def generate_pdf_view_servidor(request, pk):
    user = Usuario.objects.get(id=pk)
    itens = user.material_set.all()
    celulares = user.celular_set.all()
    notebooks = user.cautela_notebooks.all()
    context = {'itens':itens, 'user':user, 'celulares':celulares, 'notebooks':notebooks}
    html_string = render_to_string('pdf/servidor.html', context)
    pdf = HTML(string=html_string, base_url=request.build_absolute_uri('/')).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="servidor.pdf"'
    return response
