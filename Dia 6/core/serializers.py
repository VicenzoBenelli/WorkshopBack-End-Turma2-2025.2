import re
import requests
from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "cep", "street", "neighborhood", "city", "state"]
        read_only_fields = ["street", "neighborhood", "city", "state"]

    def validate_cep(self, value):
        cep_num = re.sub(r"\D", "", value or "")
        if len(cep_num) != 8:
            raise serializers.ValidationError("CEP deve ter 8 dígitos.")
        return f"{cep_num[:5]}-{cep_num[5:]}"  # normaliza como 00000-000

    def create(self, validated_data):
        cep = validated_data["cep"].replace("-", "")
        
        resp = requests.get(f"https://viacep.com.br/ws/{cep}/json/", verify= False)
        if resp.status_code != 200:
            raise serializers.ValidationError("Falha ao consultar ViaCEP.")

        data = resp.json()
        if data.get("erro"):
            raise serializers.ValidationError("CEP não encontrado no ViaCEP.")

        return Address.objects.create(
            cep=f"{cep[:5]}-{cep[5:]}",
            street=data.get("logradouro", ""),
            neighborhood=data.get("bairro", ""),
            city=data.get("localidade", ""),
            state=data.get("uf", ""),
        )
