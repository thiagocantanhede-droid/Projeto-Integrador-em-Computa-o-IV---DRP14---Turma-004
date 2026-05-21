import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meuprojeto.settings')
django.setup()

from base.models import Item, Armario, Usuario, Material, Celular, Notebook

usuario = Usuario.objects.get(username='Thiago Cantanhede')
armario_externo = Armario.objects.get(armario='Externo')
francisco_reno = Usuario.objects.get(username='Francisco de Assis Grillo Reno')
ivan_pereira = Usuario.objects.get(username='Ivan Paulo Ortiz Pereira')
alexandre_costa = Usuario.objects.get(username='Alexandre Gomes da Costa')
luiz_cordeiro = Usuario.objects.get(username='Luis Marcio Heringer Cordeiro')
leticia_andrade = Usuario.objects.get(username='LETÍCIA DE FREITAS ANDRADE')
ana_silva = Usuario.objects.get(username='Ana Carolina Bonifácio da Silva')
cicera_silva = Usuario.objects.get(username='Cícera Tavares da Silva')
orivaldo_paula = Usuario.objects.get(username='Orivaldo José de Paula')
thiago_bianconi = Usuario.objects.get(username='Thiago Eduardo Bianconi')
alexandre_duarte = Usuario.objects.get(username='Alexandre Romariz Duate')
diego_zanini = Usuario.objects.get(username='Diego Augusto Zanini')
edson_tsuhako = Usuario.objects.get(username='Edson Mitsuhide Tsuhako')
eloi_junior = Usuario.objects.get(username='Eloi Norberto Venturini Junior')
fernanda_mecabo = Usuario.objects.get(username='Fernanda Tais Mercabô')
marcos_oliveira = Usuario.objects.get(username='Marcos José de Oliveira')
mauricio_martins = Usuario.objects.get(username='Maurício Pires Martins')
jose_reato = Usuario.objects.get(username='José Ricardo Reato')
jose_filho = Usuario.objects.get(username='José Arnaldo Pittom Filho')
julio_zambao = Usuario.objects.get(username='Júlio Cesar Zambão')
paulo_pravuschi = Usuario.objects.get(username='Paulo Roberto Pravuschi')


def main():
    marcas = ['ACER','ACER','ACER','SINFO','Acer','SINFO','SINFO','SINFO','HP','Microsoft','Dell','Apple','HP','Dell','Apple','Dell','Apple','ACER','ACER','ACER']
    modelos = ['Aspire 5','Aspire 5','Aspire 5','SINFO','Aspire 5','SINFO','SINFO','SINFO','Zbook Fury G7','Surface Laptop 4','Gamming Dell Alienware M17','MacBook Air A2337','PROBOOK 440 G7','Gamming Dell Alienware M17','Macbook Pro 13"','Gamming Dell Alienware M17','Macbook Pro A2338','A515-57-51W5','A515-57-51W5','A515-57-51W5']
    patrimônios = ['328620','328619', '322953','328548','322943','328638','328637','328636','328639','309381','309376','281880','309382','281879','281800','281878','309384','328625','328624','328626']
    updates = [usuario, usuario,usuario,usuario,usuario,usuario,usuario,usuario,usuario,usuario,usuario,usuario,usuario,usuario,usuario,usuario,usuario,usuario,usuario,usuario]
    cautelas = [francisco_reno,ivan_pereira,alexandre_costa,luiz_cordeiro,leticia_andrade,ana_silva,cicera_silva,orivaldo_paula,thiago_bianconi,alexandre_duarte,diego_zanini,edson_tsuhako,edson_tsuhako,fernanda_mecabo,jose_reato,marcos_oliveira,mauricio_martins,jose_filho,julio_zambao,paulo_pravuschi]
    armarios = [armario_externo, armario_externo, armario_externo,armario_externo,armario_externo,armario_externo,armario_externo,armario_externo,armario_externo,armario_externo,armario_externo,armario_externo,armario_externo,armario_externo,armario_externo,armario_externo,armario_externo,armario_externo,armario_externo,armario_externo]
    documentos = ['24560747', '24560590', '24559911','21216603','23377781','22340547','22443846','21407460','21597496','23125087','23125208','23407267','21184764','14624494','14624098','17290589','23120667','22634398','22637158','22637364']

    for i in range(len(patrimônios)):
        
        Notebook.objects.create(marca=marcas[i],modelo=modelos[i],patrimônio=patrimônios[i],updated_by=updates[i],cautela=cautelas[i],armario=armarios[i],documento=documentos[i])
                                
if __name__ == '__main__':
    main()
