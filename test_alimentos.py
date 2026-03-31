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

def test_zerofill_funciona():
    codigo = gerar_codigo("BR", "C", "D", 12)
    inserir_resultado("BR", "C", "D", 12, codigo)
    assert codigo == "BRC0012D"

def test_numero_maior():
    codigo = gerar_codigo("BR", "A", "C", 123)
    inserir_resultado("BR", "A", "C", 123, codigo)
    assert codigo == "BRA0123C"

# TESTE FINAL: imprime a tabela no terminal
def test_mostrar_tabela_final():
    cursor.execute("SELECT cod, sec, grupo_id, tipo_alimento, pais FROM alimentos")
    resultados = cursor.fetchall()
    headers = ["Código", "Número", "Grupo", "Tipo", "País"]
    row_format = "{:<8} {:<6} {:<6} {:<6} {:<4}"
    sys.stdout.write("\n" + "-"*50 + "\n")
    sys.stdout.write("Tabela de Resultados dos Testes (MySQL)\n")
    sys.stdout.write("-"*50 + "\n")
    sys.stdout.write(row_format.format(*headers) + "\n")
    sys.stdout.write("-"*50 + "\n")
    for row in resultados:
        sys.stdout.write(row_format.format(*row) + "\n")
    sys.stdout.write("\n")
    conn.close()
