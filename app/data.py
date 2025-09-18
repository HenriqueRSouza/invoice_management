import pandas as pd
from datetime import datetime
from app.utils.insert import get_engine

# --------------------
# LOAD FUNCTIONS
# --------------------
def load_suppliers() -> pd.DataFrame:
    engine = get_engine()
    query = "SELECT razao_social, nome_fantasia FROM invoice.fornecedor"
    return pd.read_sql(query, engine)


def load_pos() -> pd.DataFrame:
    engine = get_engine()
    query = """
        SELECT po_code, descricao, fornecedor, valor_total,
               valor_utilizado, saldo_disponivel, data_abertura, conta_contabil
        FROM invoice.pos
    """
    df = pd.read_sql(query, engine)
    if "data_abertura" in df.columns:
        df["data_abertura"] = pd.to_datetime(df["data_abertura"])
    return df


def load_notes() -> pd.DataFrame:
    engine = get_engine()
    query = """
        SELECT nota_numero, po_code, descricao, valor,
               data_emissao, data_vencimento, status_pagamento, fornecedor, codigo_for
        FROM invoice.notas
    """
    return pd.read_sql(query, engine)


# --------------------
# SAVE FUNCTIONS
# --------------------
def save_data(df: pd.DataFrame, kind: str) -> None:
    engine = get_engine()
    if kind == "pos":
        df.to_sql("pos", engine, if_exists="replace", index=False)
    elif kind == "notas":
        df.to_sql("notas", engine, if_exists="replace", index=False)
    elif kind == "fornecedores":
        df.to_sql("fornecedores", engine, if_exists="replace", index=False)


# --------------------
# HELPER
# --------------------
def create_po_row(po_code: str, descricao: str, fornecedor: str, valor_total: float) -> pd.DataFrame:
    return pd.DataFrame([[po_code, descricao, fornecedor, valor_total, 0, valor_total, datetime.today()]],
                        columns=["po_code", "descricao", "fornecedor", "valor_total",
                                 "valor_utilizado", "saldo_disponivel", "data_abertura"])
