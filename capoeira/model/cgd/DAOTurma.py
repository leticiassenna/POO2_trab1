from capoeira.model.cgd.DAO import DAO
from capoeira.model.cgd.Conexao import Conexao
import copy
__author__ = 'Leticia'


class DAOTurma(DAO):

    def clone(self):
            return copy.copy(self)

    def salvar(self, turma):
        try:
            dao = Conexao()
            dao.execute_insert_delete("""
            INSERT INTO turma (grau , turno, rg_professor )
            VALUES (%r,%r,%r,%r,%r,%r,%r,%r)
            """ % (turma.nome, turma.dia_semana, turma.rg_professor))
        except ValueError:
            raise

