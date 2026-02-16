from pathlib import Path
import pandas as pd
import json
import re


# -------------------------
# AFRODITE
# -------------------------

def load_afrodite(path="data/afrodite.json", n=300):
    base_dir = Path(__file__).resolve().parent.parent
    full_path = base_dir / path

    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data).head(n).copy()

    def extrair_ingredientes(secao):
        for s in secao:
            if "Ingrediente" in s["nome"]:
                return s["conteudo"]
        return []

    df["ingredientes"] = df["secao"].apply(extrair_ingredientes)

    return df[["nome", "ingredientes"]]


def explode_ingredientes(df):
    df_exploded = df.explode("ingredientes").copy()
    df_exploded.rename(columns={"nome": "receita"}, inplace=True)
    df_exploded.rename(columns={"ingredientes": "ingrediente_raw"}, inplace=True)
    return df_exploded


def limpar_ingredientes(df):
    df = df.copy()

    df = df[df["ingrediente_raw"].notna()]
    df = df[df["ingrediente_raw"].str.strip() != ""]
    df = df[~df["ingrediente_raw"].str.isupper()]

    return df


def parse_ingredientes(df):
    df = df.copy()

    pattern = r"(?P<quantidade>\d+)\s*(?P<unidade>g|ml)\s*(de\s)?(?P<alimento>.*)"

    parsed = df["ingrediente_raw"].str.extract(pattern)

    df_parsed = pd.concat([df["receita"], parsed], axis=1)

    df_parsed = df_parsed.dropna(subset=["quantidade", "unidade", "alimento"])

    df_parsed["quantidade"] = df_parsed["quantidade"].astype(float)
    df_parsed["alimento"] = (
        df_parsed["alimento"]
        .str.lower()
        .str.strip()
    )

    return df_parsed


# -------------------------
# TACO
# -------------------------

def load_taco():
    base_dir = Path(__file__).resolve().parent.parent
    path = base_dir / "data" / "taco.csv"

    df_taco = pd.read_csv(
        path,
        sep=",",
        decimal=".",
        engine="python",
        on_bad_lines="skip"  # ← ADICIONE ISSO
    )

    df_taco.columns = df_taco.columns.str.strip()

    df_taco.rename(columns={"Nome": "alimento"}, inplace=True)

    df_taco["alimento"] = (
        df_taco["alimento"]
        .str.lower()
        .str.strip()
    )

    return df_taco


# -------------------------
# MERGE
# -------------------------

def integrar_taco(df_parsed, df_taco):
    df_merged = df_parsed.merge(
        df_taco,
        on="alimento",
        how="inner"
    )

    return df_merged
