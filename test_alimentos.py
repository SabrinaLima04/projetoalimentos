import pytest
import sqlite3
from alimentos import gerar_codigo

# Conectar ao banco SQLite em memória
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Criar tabela
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

# Fixture para finalizar a sessão e imprimir a tabela
@pytest.fixture(scope="session", autouse=True)
def mostrar_tabela_no_final(request):
    # Função que será executada ao final da sessão
    def finalizador():
        print("\n" + "-"*50)
        print("Tabela de Resultados dos Testes (Banco SQLite)")
        print("-"*50)
        cursor.execute("SELECT * FROM resultados")
        resultados = cursor.fetchall()
        headers = ["País", "Grupo 1", "Grupo 2", "Número", "Código Gerado"]
        row_format = "{:<5} {:<7} {:<7} {:<6} {:<12}"
        print(row_format.format(*headers))
        print("-"*50)
        for row in resultados:
            print(row_format.format(*row))
        conn.close()
    request.addfinalizer(finalizador)


# Função auxiliar para inserir resultados
def inserir_resultado(pais, g1, g2, numero, codigo):
    cursor.execute(
        "INSERT INTO resultados (pais, grupo1, grupo2, numero, codigo_gerado) VALUES (?, ?, ?, ?, ?)",
        (pais, g1, g2, numero, codigo)
    )
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
