from rest_framework import serializers
from cultures_app.models import *


class ClanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clan
        fields = "__all__"


class CulturalKingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CulturalKingdom
        fields = "__all__"


class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethnicity
        fields = "__all__"


class CulturalIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CulturalIdentity
        fields = "__all__"


class EthnicGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EthnicGroup
        fields = "__all__"
