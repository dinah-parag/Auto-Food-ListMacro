import json
import pandas as pd

with open("data/afrodite.json", "r", encoding="utf-8") as f:
    data = json.load(f)

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

    return df[["nome", "ingredientes"]]
