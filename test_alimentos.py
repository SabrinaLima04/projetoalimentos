import pytest
from alimentos import gerar_codigo


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

def test_montar_tabela():
    dados = [
        ("BR", "A", "C", 1),
        ("BR", "A", "B", 2),
        ("BR", "B", "A", 1),
        ("BR", "C", "D", 12),
        ("BR", "A", "C", 123),
    ]

    for pais, grupo, tipo, num in dados:
        codigo = gerar_codigo(pais, grupo, tipo, num)
        print(f"{pais}-{grupo}-{tipo}-{num} -> {codigo}")

