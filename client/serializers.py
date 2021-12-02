from rest_framework import serializers
from .models import Client, Receipts

class ClientSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Client
        read_only_fields = (
            "created_at",
            "created_by",
        ),
        fields = (
            "id",
            "name",
            "email",
            "phone",
            "address1",
            "address2",
            "zipcode",
            "place",
            "country",
            "contact_person",
            "contact_reference"
        )

class ReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receipts
        read_only_fields = (
            "created_at",
            "created_by",
            "modified_at",
        )
        fields = (
            "id",
            "client",
            "client_name",
            "title",
            "description",
            "amount",
        )