from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):

    username = models.CharField(max_length=200, null=False, unique=True)
    matricula = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    avatar = models.ImageField(null=True, default="...")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class Armario(models.Model):
    ARMARIOS_STATUS_CHOICES = [
        ("Armário 1","Armário 1"), 
        ("Armário 2 ","Armário 2 "), 
        ("Armário 3","Armário 3"), 
        ("Armário 4","Armário 4"), 
        ("Armário 5","Armário 5"), 
        ("Armário 7","Armário 7"), 
        ("Armário 5 Chefia","Armário 5 Chefia"), 
        ("Armário 17","Armário 17"), 
        ("Armário 8","Armário 8"), 
        ("Armário 20","Armário 20"), 
        ("Armário 16","Armário 16"), 
        ("Armário 19","Armário 19")
    ]
    armario = models.CharField(max_length=30, choices=ARMARIOS_STATUS_CHOICES, null=False)
    def __str__(self):
        return self.get_armario_display()
    

class Tamanho(models.Model):




    SIZE_STATUS_CHOICES = [
        ("XG","XG"), 
        ("Único","Único"), 
        ("PP","PP"), 
        ("P","P"), 
        ("P","P"), 
        ("M","M"), 
        ("G","G"), 
        ("EG","EG"), 
        ("52","52"), 
        ("50","50"), 
        ("48","48"), 
        ("46","46"), 
        ("44","44"), 
        ("43","43"), 
        ("42","42"), 
        ("41","41"), 
        ("39","39"), 
        ("38","38"), 
        ("37","37"), 
        ("36","36"), 
        ("13","13"),
    ]
    tamanho = models.CharField(max_length=100, choices=SIZE_STATUS_CHOICES, null=False)
    def __str__(self):
        return self.tamanho






class Item(models.Model):
    ITEM_STATUS_CHOICES = [

        ("Algema plástica","Algema plástica"),
        ("Arame Lacre Laranja","Arame Lacre Laranja"), 
        ("Barraca NTK Panda 3","Barraca NTK Panda 3"), 
        ("Bermuda Masc.","Bermuda Masc."), 
        ("Boné com Capa","Boné com Capa"), 
        ("Boné Ibama","Boné Ibama"),
        ("Boné Legionário","Boné Legionário"), 
        ("Bota Galocha","Bota Galocha"), 
        ("Bota SL Branca","Bota SL Branca"), 
        ("Bota SL Pró Preta","Bota SL Pró Preta"), 
        ("Bota Térmica","Bota Térmica"), 
        ("Botas Seasub","Botas Seasub"), 
        ("Calça","Calça"), 
        ("Calça Fem.","Calça Fem."), 
        ("Calça Masc.","Calça Masc."), 
        ("Calça/Bermuda Masc.","Calça/Bermuda Masc."), 
        ("Camisa  Fisc. Manga Curta ","Camisa  Fisc. Manga Curta "), 
        ("Camisa  Fisc. Manga Longa ","Camisa  Fisc. Manga Longa "), 
        ("camisa polo","camisa polo"), 
        ("Camiseta Branca manga curta","Camiseta Branca manga curta"), 
        ("Camiseta Branca manga longa","Camiseta Branca manga longa"), 
        ("Camiseta Verde manga longa","Camiseta Verde manga longa"), 
        ("Cantil","Cantil"), 
        ("Capa de Chuva Comum","Capa de Chuva Comum"), 
        ("Capa de Chuva Morcego Reflexiva ","Capa de Chuva Morcego Reflexiva "), 
        ("Capa de Chuva Morcego S/Refletores ","Capa de Chuva Morcego S/Refletores "), 
        ("Capa de chuva Neon","Capa de chuva Neon"), 
        ("Capa Externa de Colete Balístico  PROTECTA - VERDE","Capa Externa de Colete Balístico  PROTECTA - VERDE"), 
        ("Capa Externa de Colete Balístico  TAURUS - PRETA","Capa Externa de Colete Balístico  TAURUS - PRETA"), 
        ("capa impermeável p/mochila rusher","capa impermeável p/mochila rusher"), 
        ("Capa para Cantil","Capa para Cantil"), 
        ("Capacete 3M Branco","Capacete 3M Branco"), 
        ("Capacete de segurança UMP Amarelo ","Capacete de segurança UMP Amarelo "), 
        ("Chapéu com Proteção ","Chapéu com Proteção "), 
        ("Cinto Tático  ","Cinto Tático  "), 
        ("Cinto Tático Underbelt","Cinto Tático Underbelt"), 
        ("Cintos Verde","Cintos Verde"), 
        ("Colete de Segurança","Colete de Segurança"), 
        ("Colete em X Verde e Branco ","Colete em X Verde e Branco "), 
        ("Colete Fisc.","Colete Fisc."), 
        ("Colete Flotek","Colete Flotek"), 
        ("Colete Laranja e Branco","Colete Laranja e Branco"), 
        ("Colete Reflexivo","Colete Reflexivo"), 
        ("Coturno","Coturno"), 
        ("Coturno Prevfogo","Coturno Prevfogo"), 
        ("Encaixe Toyota p/ Calota","Encaixe Toyota p/ Calota"), 
        ("Facão","Facão"), 
        ("Fita adesiva larga - IBAMA/MMA","Fita adesiva larga - IBAMA/MMA"), 
        ("Gandola ","Gandola "), 
        ("Japona Térmica","Japona Térmica"), 
        ("Jaqueta com forro","Jaqueta com forro"), 
        ("Laminado Respirável","Laminado Respirável"), 
        ("Lanterna de Cabeça ALFACELL","Lanterna de Cabeça ALFACELL"), 
        ("Luva Latéx Descartável Volk","Luva Latéx Descartável Volk"), 
        ("Luva Nitrilica-Tam-Único","Luva Nitrilica-Tam-Único"), 
        ("Luvas de vaqueta Alseg – CA 25368","Luvas de vaqueta Alseg – CA 25368"), 
        ("Macacão Flytec","Macacão Flytec"), 
        ("Macacão Impermeável Laminado","Macacão Impermeável Laminado"), 
        ("Manta Alcochoada","Manta Alcochoada"), 
        ("Máscara PFF1","Máscara PFF1"), 
        ("Mochila","Mochila"), 
        ("Mochila de Salvamento","Mochila de Salvamento"), 
        ("Mochila IBAMA","Mochila IBAMA"), 
        ("Mochila Rusher 40L Verde","Mochila Rusher 40L Verde"), 
        ("Mochilas de Hidratação KALAHARI","Mochilas de Hidratação KALAHARI"), 
        ("Mucambo Pro AF 15","Mucambo Pro AF 15"), 
        ("Óculos de proteção Kalipso","Óculos de proteção Kalipso"), 
        ("Perneira  ","Perneira  "), 
        ("Perneira Sayro - CA 14750","Perneira Sayro - CA 14750"), 
        ("Porta Rádio","Porta Rádio"), 
        ("Porta utilidades P/ Cinto","Porta utilidades P/ Cinto"), 
        ("Protetor auricular silicone – CA 18189","Protetor auricular silicone – CA 18189"), 
        ("Regulador de capacete","Regulador de capacete"), 
        ("Sapato Couro","Sapato Couro"), 
        ("Sobretudo Impemeável ","Sobretudo Impemeável "), 
        ("Touca TNT Descartável","Touca TNT Descartável"), 
        ("Trena de Fibra","Trena de Fibra"), 
        ("Headset Logitech","Headset Logitech"), 
        ("Camera WEBCAM Gotech","Camera WEBCAM Gotech"), 
        ("Kit Identificador de Gás Refrigerante","Kit Identificador de Gás Refrigerante"),

    ]
    name = models.CharField(max_length=200, choices=ITEM_STATUS_CHOICES, null=False, blank=True)
    quantidade = models.IntegerField()

    patrimônio = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='created_item')
    # updated_by = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='updated_item')
    # * criar função na view que grava o último usuário que realizou a alteração

    image = models.ImageField(null=True, default='...', blank=True)
    cautela = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    armario = models.ForeignKey(Armario, on_delete=models.CASCADE, null=True, related_name='armarios', blank=True)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.DO_NOTHING, null=False, related_name='tamanhos', blank=True)


    def __str__(self):
        return self.get_name_display()

