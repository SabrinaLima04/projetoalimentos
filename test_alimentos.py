import pytest
import mysql.connector
from alimentos import gerar_codigo
import sys

# Conexão com o MySQL
conn = mysql.connector.connect(
    host="localhost",     # altere se necessário
    user="root",          # seu usuário
    password="root",      # sua senha
    database="db_alimentos"
)
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS alimentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cod VARCHAR(8) UNIQUE NOT NULL,
    sec INT(4) ZEROFILL NOT NULL,
    grupo_id VARCHAR(1) NOT NULL,
    tipo_alimento CHAR(1) NOT NULL,
    pais VARCHAR(2) NOT NULL
)
""")
conn.commit()

# Limpar tabela antes dos testes
cursor.execute("TRUNCATE TABLE alimentos")
conn.commit()

# Função para inserir resultado
def inserir_resultado(pais, grupo_id, tipo_alimento, numero, codigo):
    cursor.execute("""
        INSERT INTO alimentos (cod, sec, grupo_id, tipo_alimento, pais)
        VALUES (%s, %s, %s, %s, %s)
    """, (codigo, numero, grupo_id, tipo_alimento, pais))
    conn.commit()

# TESTES
def test_codigo_primeiro_registro():
    codigo = gerar_codigo("BR", "A", "C", 1)
    inserir_resultado("BR", "A", "C", 1, codigo)
    assert codigo == "BRA0001C"

def test_codigo_segundo_registro():
    codigo = gerar_codigo("BR", "A", "B", 2)
    inserir_resultado("BR", "A", "B", 2, codigo)
    assert codigo == "BRA0002B"

def test_codigo_outro_grupo():
    codigo = gerar_codigo("BR", "B", "A", 1)
    inserir_resultado("BR", "B", "A", 1, codigo)
    assert codigo == "BRB0001A"

def
