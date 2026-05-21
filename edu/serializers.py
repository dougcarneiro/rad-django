from rest_framework import serializers
from .models import Autor, Editora

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome']
        read_only_fields = ['id']
        
    def validate_nome(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("O nome do autor deve ao menos 2 caracteres.")
        return value

class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = ['id', 'nome']
        read_only_fields = ['id']
        
    def validate_nome(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("O nome da editora deve ao menos 2 caracteres.")
        return value