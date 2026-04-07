import pytest
from alimentos import gerar_codigo
from alimentos import inserir_alimento, conectar


def test_codigo_primeiro_registro():

    codigo = gerar_codigo("BR", "A", "C", 1)

    assert codigo == "BRA0001C"


def test_codigo_segundo_registro():

    codigo = gerar_codigo("BR", "A", "B", 2)

    assert codigo == "BRA0002B"


def test_codigo_outro_grupo():

    codigo = gerar_codigo("BR", "B", "A", 1)

    assert codigo == "BRB0001A"


def test_zerofill_funciona():

    codigo = gerar_codigo("BR", "C", "D", 12)

    assert codigo == "BRC0012D"


def test_numero_maior():

    codigo = gerar_codigo("BR", "A", "C", 123)

    assert codigo == "BRA0123C"

def test_mostrar_tabela():

    conn = conectar()
    cursor = conn.cursor()

    # limpa a tabela antes do teste
    cursor.execute("DELETE FROM alimentos")
    conn.commit()

    # insere alguns dados
    inserir_alimento("A", "C", "BR")
    inserir_alimento("A", "B", "BR")

    # consulta os dados
    cursor.execute("SELECT * FROM alimentos")
    resultados = cursor.fetchall()

    print("\n--- TABELA ALIMENTOS ---")
    for linha in resultados:
        print(linha)

    conn.close()

    # valida se inseriu corretamente
    assert len(resultados) == 2
