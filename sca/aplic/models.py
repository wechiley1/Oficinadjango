from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=8)
    cnpj = models.CharField(max_length=14)
    razaosocial = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    telefone1 = models.CharField(max_length=15)
    telefone2 = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Pagamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valorfinalservico = models.DecimalField(max_digits=10, decimal_places=2)
    valorrecebido = models.DecimalField(max_digits=10, decimal_places=2)
    restante = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    anodereferencia = models.PositiveIntegerField()
    totalpago = models.BooleanField(default=False)
    dthorapagamento = models.DateTimeField()
    formapagamento = models.CharField(max_length=50)
    STATUS_PAGAMENTO_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago')
    ]
    statuspagamento = models.CharField(max_length=10, choices=STATUS_PAGAMENTO_CHOICES)

    def save(self, *args, **kwargs):
        self.restante = self.valorfinalservico - self.valorrecebido
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pagamento de {self.cliente}"

class OrdemDeServico(models.Model):
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE, null=True, blank=True)
    defeitoreclamado = models.TextField()
    procedimentorealizado = models.TextField()
    dt_hora_entrada = models.DateTimeField()
    dt_hora_saida = models.DateTimeField(null=True, blank=True)
    valorservico = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_SERVICO_CHOICES = [
        ('PARA FAZER', 'Para Fazer'),
        ('EM ANDAMENTO', 'Em Andamento'),
        ('FINALIZADO', 'Finalizado'),
        ('ENTREGUE', 'Entregue')
    ]
    statusservico = models.CharField(max_length=15, choices=STATUS_SERVICO_CHOICES)

    def __str__(self):
        return f"Ordem de Serviço #{self.id}"

class Recibo(models.Model):
    valorecibo = models.DecimalField(max_digits=10, decimal_places=2)
    datahoraemissao = models.DateTimeField()
    ordensdeservico = models.ManyToManyField(OrdemDeServico)

    def __str__(self):
        return f"Recibo #{self.id}"

class Funcionario(models.Model):
    nomefuncionario = models.CharField(max_length=100)
    cargofuncionario = models.CharField(max_length=50)
    ordensdeservico = models.ManyToManyField(OrdemDeServico)

    def __str__(self):
        return f"{self.nomefuncionario} ({self.cargofuncionario})"

class Cargo(models.Model):
    nomecargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nomecargo

class Peca(models.Model):
    TipoPeca = models.CharField(max_length=100)
    MarcaPeca = models.CharField(max_length=100)
    ModeloPeca = models.CharField(max_length=100)
    EstoqueAtual = models.PositiveIntegerField()
    PrecoCompra = models.DecimalField(max_digits=10, decimal_places=2)
    PrecoVendaFinal = models.DecimalField(max_digits=10, decimal_places=2)
    QtdTotalVendida = models.PositiveIntegerField()
    TotalEmVendas = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.TipoPeca} ({self.MarcaPeca})"

class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    TipoVeiculo = models.CharField(max_length=100)
    PlacaVeiculo = models.CharField(max_length=20)
    AnoVeiculo = models.PositiveIntegerField()
    ModeloVeiculo = models.CharField(max_length=100)
    Potencia = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.TipoVeiculo} - {self.PlacaVeiculo}"

class Carro(Veiculo):
    cavalos = models.PositiveIntegerField()

    def __str__(self):
        return f"Carro - {self.PlacaVeiculo}"

class Moto(Veiculo):
    cilindrada = models.PositiveIntegerField()

    def __str__(self):
        return f"Moto - {self.PlacaVeiculo}"

class Caminhao(Veiculo):
    capacidade = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Caminhão - {self.PlacaVeiculo}"

