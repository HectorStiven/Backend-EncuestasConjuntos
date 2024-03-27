from rest_framework import serializers
from estudiantes.models import  T001Encuesta, T002DatosCasa, T003DatosConjunto,T004Personas,T005TipoAsistencia,T006TipoEncuesta,T007TiposDeCasa


class T001EncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = T001Encuesta
        fields = '__all__'

class T002DatosCasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = T002DatosCasa
        fields = '__all__'

class T003DatosConjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = T003DatosConjunto
        fields = '__all__'

class T004PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = T004Personas
        fields = '__all__'

class T005TipoAsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = T005TipoAsistencia
        fields = '__all__'

class T006TipoEncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = T006TipoEncuesta
        fields = '__all__'

class T007TiposDeCasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = T007TiposDeCasa
        fields = '__all__'
