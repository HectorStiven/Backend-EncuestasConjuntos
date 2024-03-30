from django.db import models

class T001Encuesta(models.Model):
    id = models.AutoField(primary_key=True)
    T001nombre_encuesta = models.CharField(max_length=255)
    T001numero_control = models.CharField(max_length=255)
    id_casa = models.ForeignKey('T002DatosCasa', on_delete=models.CASCADE)
    id_persona = models.ForeignKey('T004Personas', on_delete=models.CASCADE)
    id_tipo_asistencia = models.ForeignKey('T005TipoAsistencia', on_delete=models.CASCADE)
    id_tipo_encuesta = models.ForeignKey('T006TipoEncuesta', on_delete=models.CASCADE)

    class Meta:
        db_table = 'T001Encuesta'

class T002DatosCasa(models.Model):
    id = models.AutoField(primary_key=True)
    T002nombre_casa = models.CharField(max_length=255)
    T002propietario = models.CharField(max_length=255)
    T002ponderacion = models.IntegerField()
    id_conjunto = models.ForeignKey('T003DatosConjunto', on_delete=models.CASCADE)
    id_tipo_casa = models.ForeignKey('T007TiposDeCasa', on_delete=models.CASCADE)

    class Meta:
        db_table = 'T002DatosCasa'

class T003DatosConjunto(models.Model):
    id = models.AutoField(primary_key=True)
    nit = models.CharField(max_length=255, unique=True)
    T003nombre = models.CharField(max_length=255)
    T003direccion = models.CharField(max_length=255)
    T003numero_administracion = models.CharField(max_length=255)
    T003tel = models.CharField(max_length=255)

    class Meta:
        db_table = 'T003DatosConjunto'

class T004Personas(models.Model):
    id = models.AutoField(primary_key=True)
    T004cell = models.CharField(max_length=255)
    T004nombre = models.CharField(max_length=255, null=False)
    T004cc = models.CharField(max_length=255)
    T004correo = models.CharField(max_length=255)
    T004direccion = models.CharField(max_length=255, null=True)  # Campo para la dirección
    T004activo = models.BooleanField(default=False)  # Campo para indicar si está activo o no
    T004coeficiente = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Campo tipo decimal para el coeficiente
    T004genero = models.CharField(max_length=20, null=True)  # Campo para el género

    class Meta:
        db_table = 'T004Personas'

class T005TipoAsistencia(models.Model):
    id = models.AutoField(primary_key=True)
    T005tipo = models.CharField(max_length=255)

    class Meta:
        db_table = 'T005TipoAsistencia'

class T006TipoEncuesta(models.Model):
    id = models.AutoField(primary_key=True)
    T006tipo_encuesta = models.CharField(max_length=255)

    class Meta:
        db_table = 'T006TipoEncuesta'

class T007TiposDeCasa(models.Model):
    id = models.AutoField(primary_key=True)
    T007NombreTipoo = models.CharField(max_length=255)

    class Meta:
        db_table = 'T007TiposDeCasa'