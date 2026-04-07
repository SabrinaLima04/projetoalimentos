import mysql.connector


# CONEXÃO COM O BANCO

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="alimentos"
    )


# GERAR SEC POR GRUPO

def gerar_sec(grupo_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT MAX(sec)
        FROM alimentos
        WHERE grupo_id = %s
    """, (grupo_id,))

    resultado = cursor.fetchone()

    if resultado[0] is None:
        sec = 1
    else:
        sec = int(resultado[0]) + 1

    conn.close()
    return sec


# GERAR CÓDIGO

def gerar_codigo(pais, grupo_id, tipo_alimento, sec):

    return f"{pais}{grupo_id}{sec:04d}{tipo_alimento}"


# INSERIR NO BANCO

def inserir_alimento(grupo_id, tipo_alimento, pais):

    conn = conectar()
    cursor = conn.cursor()

    sec = gerar_sec(grupo_id)
    codigo = gerar_codigo(pais, grupo_id, tipo_alimento, sec)

    sql = """
    INSERT INTO alimentos (cod, sec, grupo_id, tipo_alimento, pais)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (codigo, sec, grupo_id, tipo_alimento, pais))
    conn.commit()

    conn.close()

    print("\nAlimento inserido com sucesso!")
    print("SEC:", sec)
    print("Código:", codigo)

    return codigo


# PROGRAMA PRINCIPAL

def main():

    print("Cadastro de Alimentos\n")

    grupo_id = input("Digite o grupo (A, B, C...): ").upper()
    tipo_alimento = input("Digite o tipo de alimento: ").upper()
    pais = input("Digite o país (ex: BR): ").upper()

    inserir_alimento(grupo_id, tipo_alimento, pais)


if __name__ == "__main__":
    main()
