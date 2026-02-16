from data_loader import load_afrodite, explode_ingredientes, limpar_ingredientes, parse_ingredientes

def main():
    df = load_afrodite()
    df_exploded = explode_ingredientes(df)
    df_limpo = limpar_ingredientes(df_exploded)
    df_parsed = parse_ingredientes(df_limpo)

    print(df_parsed.head(10))
    print("Total após parsing:", len(df_parsed))


if __name__ == "__main__":
    main()
