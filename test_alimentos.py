import pytest
from alimentos import gerar_codigo
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="seu_banco"
    )

def test_codigo_primeiro_registro():
    assert gerar_codigo("BR", "A", "C", 1) == "BRA0001C"


def test_codigo_segundo_registro():
    assert gerar_codigo("BR", "A", "B", 2) == "BRA0002B"


def test_codigo_outro_grupo():
    assert gerar_codigo("BR", "B", "A", 1) == "BRB0001A"


def test_zerofill():
    assert gerar_codigo("BR", "C", "D", 12) == "BRC0012D"


def test_numero_maior():
    assert gerar_codigo("BR", "A", "C", 123) == "BRA0123C"

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
