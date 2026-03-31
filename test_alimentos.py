import pytest
import sqlite3
from alimentos import gerar_codigo

# Criar conexão e cursor do banco SQLite em memória
conn = sqlite3.connect(":memory:")  # banco temporário em RAM
cursor = conn.cursor()

# Criar tabela para armazenar os resultados
cursor.execute("""
CREATE TABLE resultados (
    pais TEXT,
    grupo1 TEXT,
    grupo2 TEXT,
    numero INTEGER,
    codigo_gerado TEXT
)
""")
conn.commit()

# Função auxiliar para inserir resultado
def inserir_resultado(pais, g1, g2, numero, codigo):
    cursor.execute(
        "INSERT INTO resultados (pais, grupo1, grupo2, numero, codigo_gerado) VALUES (?, ?, ?, ?, ?)",
        (pais, g1, g2, numero, codigo)
    )
    conn.commit()

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

# Hook do pytest para exibir tabela no final
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    terminalreporter.write_sep("-", "Tabela de Resultados dos Testes (Banco SQLite)")
    cursor.execute("SELECT * FROM resultados")
    resultados = cursor.fetchall()
    # Exibir tabela simples
    headers = ["País", "Grupo 1", "Grupo 2", "Número", "Código Gerado"]
    row_format = "{:<5} {:<7} {:<7} {:<6} {:<12}"
    terminalreporter.write_line(row_format.format(*headers))
    terminalreporter.write_line("-" * 42)
    for row in resultados:
        terminalreporter.write_line(row_format.format(*row))

    # Fechar conexão
    conn.close()
