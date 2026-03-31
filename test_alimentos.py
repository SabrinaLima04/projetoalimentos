from gerador_codigo import gerar_codigo
from conexao import conectar

def test_primeiro_codigo():
    codigo = gerar_codigo("C", "A", "BR")
    print("Código gerado:", codigo)
    assert codigo == "BRC0001A"

def test_incremento():
    gerar_codigo("D", "A", "BR")
    codigo = gerar_codigo("D", "A", "BR")
    assert codigo == "BRD0002A"

def test_ver_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM codigos_sequenciais")
    resultados = cursor.fetchall()

    print("\n📊 CONTEÚDO DA TABELA:")
    for linha in resultados:
        print(linha)

    cursor.close()
    conn.close()

    assert True
