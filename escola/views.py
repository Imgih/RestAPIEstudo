from rest_framework import viewsets
from escola.models import Aluno
from escola.models import Curso
from escola.serializer import AlunoSerializer
from escola.serializer import CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Endpoint para exebir dados dos alunos"""
    queryset = Aluno.objects.all() # seria um objeto 
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Endpoint para exebir dados dos cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer