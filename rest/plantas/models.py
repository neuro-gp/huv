from django.db import models

class Familia(models.Model):
    nombre_popular = models.CharField(max_length=200, null=True)
    nombre_cientifico = models.CharField(max_length=200, null=False)

    def __str__(self,):
        return self.nombre_popular if self.nombre_popular else self.nombre_cientifico

class Rotaciones(models.Model):
    anterior = models.ForeignKey(Familia, on_delete=models.SET_NULL, null=True, related_name='anterior')
    posterior = models.ForeignKey(Familia, on_delete=models.SET_NULL, null=True, related_name='posterior')

class Epoca(models.Model):
    tipo = models.CharField(max_length=200, null=False, choices=[
        ('SE','Semillero'),
        ('SI','Siembra'),
        ('TR','Trasplante'),
        ('CO','Cosecha'),
    ])
    desde = models.DateField(null=False)
    hasta = models.DateField(null=False)

class Fuente(models.Model):
    cita = models.TextField(null=False)

class Tip(models.Model):
    contenido = models.TextField(null=False)
    fuente = models.ForeignKey(Fuente, on_delete=models.SET_NULL, null=True, related_name='citada_en_tips')

class Sustrato(models.Model):
    tierra = models.CharField(max_length=200, null=True)
    potasio = models.BooleanField(default=False)
    nitrogeno = models.BooleanField(default=False)
    fosforo = models.BooleanField(default=False)

class Tipo(models.Model):
    nombre = models.CharField(max_length=200, null=False, choices=[
        ('FR','Fruta'),
        ('FL','Flor'),
        ('HO','Hoja'),
        ('RA','Raiz'),
    ])

class Planta(models.Model):
    nombre_popular = models.CharField(max_length=200, null=True)
    nombre_cientifico = models.CharField(max_length=200, null=False)

    familia = models.ForeignKey(Familia, on_delete=models.SET_NULL, null=True, related_name='plantas')

    def __str__(self,):
        return self.nombre_popular if self.nombre_popular else self.nombre_cientifico

class Ficha(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.SET_NULL, null=True, related_name='fichas')

    volumen_mazeta_ltr = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    profundidad = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    tamano = models.CharField(max_length=200, null=False, choices=[
        ('S','Chico'),
        ('M','Mediano'),
        ('L','Grande'),
        ('XL','Extra Grande'),
    ])
    distancia = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    temperatura = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    horas_sol = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    riego = models.CharField(max_length=200, null=False, choices=[
        ('c15D','Cada 15 días'),
        ('1xS','Una vez por semana'),
        ('2xS','Dos veces por semana'),
        ('c2D','Cada dos días'),
        ('1xD','Una vez por día'),
        ('2xD','Dos veces por día'),
    ])
    tiempo_cultivo_dias = models.IntegerField(null=False)
    tutorado = models.BooleanField(default=False)
    
    epoca_semillero = models.ForeignKey(Epoca, on_delete=models.SET_NULL, null=True, related_name='fichas_semillero')
    epoca_siembra = models.ForeignKey(Epoca, on_delete=models.SET_NULL, null=True, related_name='fichas_siembra')
    epoca_trasplante = models.ForeignKey(Epoca, on_delete=models.SET_NULL, null=True, related_name='fichas_trasplante')
    epoca_cosecha = models.ForeignKey(Epoca, on_delete=models.SET_NULL, null=True, related_name='fichas_cosecha')

    sustrato = models.ManyToManyField(Sustrato)
    tips = models.ManyToManyField(Tip)
    fuentes = models.ManyToManyField(Fuente)

class Interacciones(models.Model):
    target = models.ForeignKey(Planta, on_delete=models.SET_NULL, null=True, related_name='interaciones')
    tipo = models.CharField(max_length=200, null=False, choices=[
        ('B','Benéfica'),
        ('P','Perjudicial'),
    ])

    actores = models.ManyToManyField(Planta)
