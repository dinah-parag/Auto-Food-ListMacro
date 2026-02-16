from data_loader import (
    load_afrodite,
    explode_ingredientes,
    limpar_ingredientes,
    parse_ingredientes,
    load_taco,
    integrar_taco
)


def main():
    df = load_afrodite()
    df_exploded = explode_ingredientes(df)
    df_limpo = limpar_ingredientes(df_exploded)
    df_parsed = parse_ingredientes(df_limpo)

    df_taco = load_taco()

    df_final = integrar_taco(df_parsed, df_taco)

    print("Linhas após merge:", len(df_final))
    print(df_final.head())


if __name__ == "__main__":
    main()
