from capoeira.model.cgd.DAO import DAO
from capoeira.model.cgd.Conexao import Conexao
import copy
__author__ = 'Gustavo'


class DAOCorda(DAO):
    def clone(self):
        return copy.copy(self)

    def salvar(self, corda):

        try:
            dao = Conexao()
            dao.execute_insert_delete("""
            INSERT INTO corda (cor)
            VALUES (%r)
            """ % (corda.cor))
        except ValueError:
            raise


