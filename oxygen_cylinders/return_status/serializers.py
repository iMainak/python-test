from rest_framework import serializers
from .models import Sources

class SourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sources
        fields = '__all__'

    def create(self, validate_data):
        dbname = self._context.get("db")

        db = Sources(**validate_data)

        db.save(using=dbname)

        return db
