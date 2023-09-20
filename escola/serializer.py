from rest_framework import serializer
from escola.models import Aluno, Curso

class AlunoSerializer(serializer.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome','rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializer.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'