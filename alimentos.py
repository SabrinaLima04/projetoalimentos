import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="228700",
    database="db_alimentos"
)

cursor = conn.cursor()

def gerar_sec(grupo_id):

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

    return sec

# Gerar Código
def gerar_codigo(pais, grupo_id, tipo_alimento, sec):
    codigo = f"{pais}{grupo_id}{sec:04d}{tipo_alimento}"
    return codigo

# Colocar no Banco de Dados
def inserir_alimento(grupo_id, tipo_alimento, pais):
    sec = gerar_sec(grupo_id)
    codigo = gerar_codigo(pais, grupo_id, tipo_alimento, sec)

    sql = "INSERT INTO alimentos (cod, sec, grupo_id, tipo_alimento, pais) VALUES (%s, %s, %s, %s, %s)"
    valores = (codigo, sec, grupo_id, tipo_alimento, pais)


    cursor.execute(sql, valores)
    conn.commit()

    print("\nAlimento inserido com sucesso!")
    print("SEC:", sec)
    print("Cód:", codigo)

# Coletar Informações - (Main)
def main():
    print("Cadastro de Alimentos\n")

    grupo_id = input("Digite o grupo (A, B, C...): ").upper()
    tipo_alimento = input("Digite o tipo de alimento: ").upper()
    pais = input("Digite o país (ex: BR): ").upper()

    inserir_alimento(grupo_id, tipo_alimento, pais)

if __name__ == "__main__":
    main()
