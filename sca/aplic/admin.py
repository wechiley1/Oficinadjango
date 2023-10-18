from django.contrib import admin
from .models import Cliente, Pagamento, OrdemDeServico, Recibo, Funcionario, Cargo, Peca, Veiculo, Carro, Moto, Caminhao


admin.site.register(Cliente)
admin.site.register(Pagamento)
admin.site.register(OrdemDeServico)
admin.site.register(Recibo)
admin.site.register(Funcionario)
admin.site.register(Cargo)
admin.site.register(Peca)
admin.site.register(Veiculo)
admin.site.register(Carro)
admin.site.register(Moto)
admin.site.register(Caminhao)



class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'cpf', 'email', 'telefone1']
    list_filter = ['cidade', 'estado']
    search_fields = ['nome', 'sobrenome', 'cpf', 'email']

class PagamentoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'valor final servico', 'status pagamento']
    list_filter = ['status pagamento']
    search_fields = ['cliente__nome', 'cliente__sobrenome', 'cliente__cpf']


class OrdemDeServicoAdmin(admin.ModelAdmin):
    list_display = ['pagamento', 'status servico', 'dt_hora_entrada', 'dt_hora_saida']
    list_filter = ['status servico']
    search_fields = ['pagamento__cliente__nome', 'pagamento__cliente__sobrenome']


class ReciboAdmin(admin.ModelAdmin):
    list_display = ['ordem de servico', 'valorecibo', 'datahoraemissao']
    list_filter = ['ordem de servico__status servico']
    search_fields = ['ordem de servico__pagamento__cliente__nome', 'ordem de servico__pagamento__cliente__sobrenome']


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome funcionario', 'cargo funcionario']
    list_filter = ['cargo funcionario']
    search_fields = ['nome funcionario']




class PecaAdmin(admin.ModelAdmin):
    list_display = ['Tipo Peca', 'Marca Peca', 'Modelo Peca', 'Estoque Atual', 'Preco Compra', 'Preco Venda Final']
    list_filter = ['Tipo Peca', 'Marca Peca']
    search_fields = ['Tipo Peca', 'Marca Peca', 'Modelo Peca']
    ordering = ['Tipo Peca']

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'Tipo Veiculo', 'Placa Veiculo', 'Ano Veiculo']
    list_filter = ['Tipo Veiculo', 'Placa Veiculo']
    search_fields = ['Tipo Veiculo', 'Placa Veiculo']


class CarroAdmin(admin.ModelAdmin):
    list_display = ['Tipo Veiculo', 'Placa Veiculo', 'Ano Veiculo', 'cavalos']


class MotoAdmin(admin.ModelAdmin):
    list_display = ['Tipo Veiculo', 'Placa Veiculo', 'Ano Veiculo', 'cilindrada']



class CaminhaoAdmin(admin.ModelAdmin):
    list_display = ['Tipo Veiculo', 'Placa Veiculo', 'AnoVeiculo', 'capacidade']



