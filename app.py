import streamlit as st
import pandas as pd

# Simulando base de dados
data = {
    "dish": ["Frango", "Frango", "Omelete", "Omelete"],
    "ingredient": ["Frango", "Arroz", "Ovo", "Queijo"],
    "quantity": [200, 100, 2, 50],
    "unit": ["g", "g", "un", "g"],
    "protein": [40, 2, 12, 10],
    "carbs": [0, 28, 1, 1],
    "fat": [5, 1, 10, 8]
}

df = pd.DataFrame(data)

st.title("🍽️ Gerador de Lista de Compras")

dishes_input = st.text_input(
    "Digite os pratos da semana separados por vírgula:",
    "Frango, Omelete"
)

if st.button("Gerar Lista"):

    weekly_dishes = [d.strip() for d in dishes_input.split(",")]
    filtered_df = df[df["dish"].isin(weekly_dishes)]

    grouped = filtered_df.groupby(["ingredient", "unit"]).agg({
        "quantity": "sum",
        "protein": "sum",
        "carbs": "sum",
        "fat": "sum"
    }).reset_index()

    st.subheader("📋 Lista Consolidada")
    st.dataframe(grouped[["ingredient", "quantity", "unit"]])

    st.subheader("📊 Macros Totais")

    total_protein = grouped["protein"].sum()
    total_carbs = grouped["carbs"].sum()
    total_fat = grouped["fat"].sum()

    st.write(f"Proteína: {total_protein} g")
    st.write(f"Carboidratos: {total_carbs} g")
    st.write(f"Gordura: {total_fat} g")
