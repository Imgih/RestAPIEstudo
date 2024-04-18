from django.contrib import admin
from escola.models import Aluno
from escola.models import Curso

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    search_fields = ('nome', 'rg', 'cpf')
    list_per_page = 20

class Cursos(admin.ModelAdmin):
    list_display = ('codigo_curso', 'descricao', 'nivel')
    list_display_links = ('codigo_curso', 'descricao', 'nivel')
    search_fields = ('codigo_curso', 'descricao')
    list_per_page = 20

admin.site.register(Aluno, Alunos ) #aluno é o banco de dados/ modelo 
admin.site.register(Curso, Cursos)
# Alunos é a configuração do admin 

# solução do tipo admin 
# Register your models here.
