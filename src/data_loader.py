import json
import pandas as pd


def load_afrodite(path="data/afrodite.json", n=300):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data).head(n).copy()

    def extrair_ingredientes(secao):
        for s in secao:
            if "Ingrediente" in s["nome"]:
                return s["conteudo"]
        return []

    df["ingredientes"] = df["secao"].apply(extrair_ingredientes)

    df = df[["nome", "ingredientes"]]

    return df


def explode_ingredientes(df):
    df_exploded = df.explode("ingredientes").copy()
    df_exploded.rename(columns={"nome": "receita"}, inplace=True)

    df_exploded = df_exploded[["receita", "ingredientes"]]
    df_exploded.rename(columns={"ingredientes": "ingrediente_raw"}, inplace=True)

    return df_exploded

import re


def limpar_ingredientes(df_exploded):
    df = df_exploded.copy()

    # remover linhas vazias
    df = df[df["ingrediente_raw"].str.strip() != ""]

    # remover títulos tipo RECHEIO, COBERTURA etc
    df = df[~df["ingrediente_raw"].str.isupper()]

    return df

def parse_ingredientes(df):
    df = df.copy()

    pattern = r"(?P<quantidade>\d+)\s*(?P<unidade>g|ml)\s*(de\s)?(?P<alimento>.*)"

    parsed = df["ingrediente_raw"].str.extract(pattern)

    df_parsed = pd.concat([df["receita"], parsed], axis=1)

    # remover linhas onde não conseguimos extrair g ou ml
    df_parsed = df_parsed.dropna(subset=["quantidade", "unidade", "alimento"])

    df_parsed["quantidade"] = df_parsed["quantidade"].astype(float)

    return df_parsed

def load_taco(path="data/taco.csv"):
    df_taco = pd.read_csv(path)

    # padronizar nome para facilitar merge
    df_taco["alimento"] = df_taco["alimento"].str.lower().str.strip()

    return df_taco
