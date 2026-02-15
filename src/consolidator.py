def consolidate_ingredients(df):
    grouped = df.groupby(["ingredient", "unit"]).agg({
        "quantity": "sum",
        "protein": "sum",
        "carbs": "sum",
        "fat": "sum"
    }).reset_index()

    return grouped
