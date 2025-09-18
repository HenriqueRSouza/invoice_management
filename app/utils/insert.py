from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

server = os.getenv('USER_WRITER_AZURE_SERVER_SECRET')
database = os.getenv('USER_WRITER_AZURE_SERVER_DATABASE')
username = os.getenv('USER_WRITER_AZURE_CLIENT_ID')
password = os.getenv('USER_WRITER_AZURE_CLIENT_SECRET')

connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(connection_string)

with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO invoice.fornecedor (razao_social, nome_fantasia) VALUES (:razao, :fantasia)"),
        {"razao": "Empresa Exemplo LTDA", "fantasia": "Exemplo Comercial"}
    )

print("Registro inserido com sucesso!")
