import streamlit as st
import pandas as pd

taco = pd.read_csv("data/taco.csv")
recipes = pd.read_csv("data/recipes.csv")

merged = recipes.merge(
    taco,
    left_on="ingredient",
    right_on="alimento",
    how="left"
)

merged["proteina_total"] = (merged["proteina_g"] * merged["quantity_g"]) / 100
merged["carbo_total"] = (merged["carboidrato_g"] * merged["quantity_g"]) / 100
merged["gordura_total"] = (merged["gordura_g"] * merged["quantity_g"]) / 100

grouped = merged.groupby("ingredient").agg({
    "quantity_g": "sum",
    "proteina_total": "sum",
    "carbo_total": "sum",
    "gordura_total": "sum"
}).reset_index()


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

if filtered_df.empty:
        st.error("❌ Receita não encontrada na base de dados.")
else:
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

    txt_content = ""

for _, row in grouped.iterrows():
    txt_content += f"{row['ingredient']} - {row['quantity']} {row['unit']}\n"

st.download_button(
    label="📥 Baixar lista (.txt)",
    data=txt_content,
    file_name="lista_de_compras.txt",
    mime="text/plain"
)

