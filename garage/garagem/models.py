from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True) 
    
    def __str__(self):
        return self.nome.upper() 

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = "Cores"

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = "Acessório"

    class Meta:
        verbose_name_plural = "Acessórios"
        
class Veiculo(models.Model):
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    ano = models.IntegerField(null=True, blank=True, default=0)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    acessorios = models.ManyToManyField(Acessorio, blank=True)

    def __str__(self):
        return f"{self.marca} , {self.categoria} , {self.cor} , {self.ano}"
    
    class Meta:
        verbose_name = "Veículo"

    class Meta:
        verbose_name_plural = "Veículos"