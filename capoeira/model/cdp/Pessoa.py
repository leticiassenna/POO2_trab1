__author__ = 'Leticia'

from capoeira.model.cdp.Endereco import Endereco
from capoeira.model.cdp.Corda import Corda

class Pessoa:

    def __init__(self):
        self.nome = ""
        self.rg = ""
        self.data_nascimento = ""
        self.endereco = Endereco
        self.telefone = ""
        self.profissao = ""
        self.grau_escolar = ""
        self.cor_corda = Corda