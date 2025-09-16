import os
import mysql.connector
from dotenv import load_dotenv

# carregar variáveis logo no início
load_dotenv()

def run_migration(sql_file: str):
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASS", "1234"),
        database=os.getenv("DB_NAME", "vaga-forecast")
    )
    cursor = conn.cursor()

    with open(sql_file, "r", encoding="utf-8") as f:
        sql_script = f.read()

    for statement in sql_script.split(";"):
        stmt = statement.strip()
        if stmt:
            try:
                cursor.execute(stmt)
            except Exception as e:
                print(f"Erro executando: {stmt}\n{e}")

    conn.commit()
    cursor.close()
    conn.close()
    print("Migração executada com sucesso!")

if __name__ == "__main__":
    sql_archive = os.getenv("SQL_ARCHIVE", "./database/migrate.sql")
    run_migration(sql_archive)
