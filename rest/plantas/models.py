from django.db import models

class Familia(models.Model):
    nombre_popular = models.CharField(max_length=200, null=True)
    nombre_cientifico = models.CharField(max_length=200, null=False)

    def __str__(self,):
        return self.nombre_popular if self.nombre_popular else self.nombre_cientifico

class Rotaciones(models.Model):
    anterior = models.ForeignKey(Familia, on_delete=models.SET_NULL, null=True, related_name='anterior')
    actual =  models.ForeignKey(Familia, on_delete=models.SET_NULL, null=True, related_name='actual')
    posterior = models.ForeignKey(Familia, on_delete=models.SET_NULL, null=True, related_name='posterior')

    def __str__(self,):
        return self.actual.nombre_popular if self.actual.nombre_popular else self.actual.nombre_cientifico

class Epoca(models.Model):
    tipo = models.CharField(max_length=200, null=True, choices=[
        ('SE','Semillero'),
        ('SI','Siembra'),
        ('TR','Trasplante'),
        ('CO','Cosecha'),
    ])
    estacion = models.CharField(max_length=200, null=True)
    desde = models.DateField(null=True) # tiene que ser sin año
    hasta = models.DateField(null=True)
    def __str__(self,):
        return self.estacion if self.estacion else 'None'

class Fuente(models.Model):
    autor = models.CharField(max_length=200, null=True)
    cita = models.TextField(null=False)
    url = models.TextField(null=True) # posibilidad de no agregar

    def __str__(self,):
        return self.autor if self.autor else 'None'

class Tip(models.Model):
    descripcion = models.CharField(max_length=200, null=True)
    contenido = models.TextField(null=False)
    fuente = models.ForeignKey(Fuente, on_delete=models.SET_NULL, null=True, related_name='citada_en_tips')

    def __str__(self,):
        return self.descripcion if self.descripcion else 'None'

class Sustrato(models.Model):
    tierra = models.CharField(max_length=200, null=True)
    potasio = models.BooleanField(default=False)
    nitrogeno = models.BooleanField(default=False)
    fosforo = models.BooleanField(default=False)

    def __str__(self,):
        return self.tierra

class Tipo(models.Model):
    nombre = models.CharField(max_length=200, null=False, choices=[
        ('FR','Fruta'),
        ('FL','Flor'),
        ('HO','Hoja'),
        ('RA','Raiz'),
    ])

    def __str__(self,):
        return self.nombre

class Planta(models.Model):
    nombre_cientifico = models.CharField(max_length=200, null=False)
    nombre_popular = models.CharField(max_length=200, null=True)
    especie = models.CharField(max_length=200, null=True) # puede ser variedad
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
    temperatura = models.DecimalField(null=False, max_digits=5,
                                      decimal_places=2) # tiene que ser un rango
    horas_sol = models.DecimalField(null=False, max_digits=5, decimal_places=2) # rango
    riego = models.CharField(max_length=200, null=False, choices=[
        ('c15D','Cada 15 días'),
        ('1xS','Una vez por semana'),
        ('2xS','Dos veces por semana'),
        ('c2D','Cada dos días'),
        ('1xD','Una vez por día'),
        ('2xD','Dos veces por día'),
    ])
    tiempo_cultivo_dias = models.IntegerField(null=False) # semanas
    tutorado = models.BooleanField(default=False)
    
    epoca_semillero = models.ForeignKey(Epoca, on_delete=models.SET_NULL, null=True, related_name='fichas_semillero')
    epoca_siembra = models.ForeignKey(Epoca, on_delete=models.SET_NULL, null=True, related_name='fichas_siembra')
    epoca_trasplante = models.ForeignKey(Epoca, on_delete=models.SET_NULL, null=True, related_name='fichas_trasplante')
    epoca_cosecha = models.ForeignKey(Epoca, on_delete=models.SET_NULL, null=True, related_name='fichas_cosecha')

    sustrato = models.ManyToManyField(Sustrato)
    tips = models.ManyToManyField(Tip)
    fuentes = models.ManyToManyField(Fuente)

    def __str__(self,):
        return self.planta.nombre_popular if self.planta.nombre_popular else self.planta.nombre_cientifico

class Interacciones(models.Model):
    target = models.ForeignKey(Planta, on_delete=models.SET_NULL, null=True,
                               related_name='interaciones')
    tipo = models.CharField(max_length=200, null=False, choices=[
        ('B','Benéfica'),
        ('P','Perjudicial'),
    ])

    actores = models.ManyToManyField(Planta)

    def __str__(self,):
        return self.target.nombre_popular if self.target.nombre_popular else self.target.nombre_cientifico 
