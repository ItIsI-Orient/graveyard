# This module contains magic needed to handle database with old DDCZ application
# which connects using latin2 connection, but then proceeds to write cp1250
# encoded data into those fields

from django.db import models


class MisencodedTextField(models.TextField):    
    def from_db_value(self, value, expression, connection):
        if isinstance(value, str):
            return value.encode("latin2").decode("cp1250")
        else:
            return value


    def clean(self, value, model_instance):
        super().clean(value, model_instance)
        if isinstance(value, str):
            value = value.encode("cp1250").decode("latin2")
        return value


class MisencodedCharField(models.CharField):    
    def from_db_value(self, value, expression, connection):
        if isinstance(value, str):
            return value.encode("latin2").decode("cp1250")
        else:
            return value


    def clean(self, value, model_instance):
        super().clean(value, model_instance)
        if isinstance(value, str):
            value = value.encode("cp1250").decode("latin2")
        return value

