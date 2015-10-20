from capoeira.model.cgd.DAO import DAO
from capoeira.model.cgd.DAOGeneric import DAOGeneric
from capoeira.model.cdp.Aluno import Aluno

__author__ = 'Gustavo'
import sqlite3
from capoeira.model.cdp.Aluno import Aluno


class DAOAluno(Aluno):

    def salvar(self, aluno):
        dao = DAOGeneric()
        dao.execute_insert_delete("""
        INSERT INTO pessoa (nome, data_nascimento , telefone , profissao , grau_escolaridade , rg , cor, id_grupo)
        VALUES (%r,%r,%r,%r,%r,%r,%r,%r)
        """ % (aluno.nome, aluno.data_nascimento, aluno.telefone, aluno.profissao, aluno.grau_escolar, aluno.rg,
               aluno.cor_corda, aluno.grupo))
        dao.execute_insert_delete("""
        INSERT INTO filiacao (nome_pai, nome_mae , rg)
        VALUES (%r,%r,%r)
        """ % (aluno.pai, aluno.mae, aluno.rg))
        self.id_endereco = dao.execute_insert_delete("""
        INSERT INTO endereco (logadouro, numero , bairro, cidade, complemento)
        VALUES (%r,%r,%r,%r,%r)
        """ % (aluno.endereco.logradouro, aluno.endereco.numero, aluno.endereco.bairro, aluno.endereco.cidade,
               aluno.endereco.complemento))
        dao.execute_insert_delete("""
        INSERT INTO pessoa_endereco  (id_endereco, rg)
        VALUES (%r,%r)
        """ % (self.id_endereco, aluno.rg))
