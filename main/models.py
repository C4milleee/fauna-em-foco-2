from django.db import models

class Especie(models.Model):
    
    HABITAT_CHOICES = [
        ('Norte', 'Norte'),
        ('Nordeste', 'Nordeste'),
        ('Sul', 'Sul'),
        ('Sudeste', 'Sudeste'),
        ('Centro-Oeste', 'Centro-Oeste'),
    ]
    
    id_especie = models.AutoField(primary_key=True)
    nome_cientifico = models.CharField(max_length=255)
    nome_comum = models.CharField(max_length=255)
    habitat = models.CharField(max_length=255,choices=HABITAT_CHOICES)
    imagem = models.ImageField(upload_to='especies', null=True, blank=True)
    
    def __str__(self):
      return self.nome_cientifico

class Artigo(models.Model):
  id_artigo = models.AutoField(primary_key=True)
  titulo = models.CharField(max_length=255)
  conteudo = models.TextField()
  imagem = models.ImageField(upload_to='artigos', null=True, blank=True)
  data_publicacao = models.DateField()
  autor = models.CharField(max_length=255)
  especies = models.ManyToManyField(Especie, related_name='artigos')

  def __str__(self):
    return self.titulo