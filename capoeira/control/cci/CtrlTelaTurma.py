__author__ = 'Leticia'

from capoeira.model.cgt.AplGerenciarTurma import AplGerenciarTurma
from capoeira.view.cih.TelaGerirTurma import TelaGerirTurma


class CtrlTelaTurma(AplGerenciarTurma, TelaGerirTurma):

    def cadastrarAluno(self):
        aplGerenciarTurma = AplGerenciarTurma
        telaGerirTurma = TelaGerirTurma

        #dadosTurma = []
        dadosTurma = telaGerirTurma.cadastrarTurma(self)
        aplGerenciarTurma.cadastrar(dadosTurma)

        telaGerirTurma.mensagem(self,'Cadastro realizado!')

