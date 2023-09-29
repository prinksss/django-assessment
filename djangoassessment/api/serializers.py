from rest_framework import serializers
from .models import Invoice, CustomUsers,InvoiceDetail
from django.db import transaction

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, required=False)

    class Meta:
        model = Invoice
        fields = '__all__'

    def create(self, validated_data):
        details_data = validated_data.pop('details', [])
        invoice = Invoice.objects.create(**validated_data)
        
        for detail_data in details_data:
            detail_data['invoice'] = invoice
            InvoiceDetail.objects.create(**detail_data)
        return invoice

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details', [])

        with transaction.atomic():
            instance = super().update(instance, validated_data)
            instance.details.all().delete()

            for detail_data in details_data:
                    InvoiceDetail.objects.create(invoice=instance, **detail_data)

        return instance

    
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUsers
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = CustomUsers(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user