from data_loader import load_data
from consolidator import consolidate_ingredients

df = load_data("data/recipes.csv")

weekly_dishes = input("Digite os pratos da semana separados por vírgula: ").split(",")

weekly_dishes = [dish.strip() for dish in weekly_dishes]

filtered_df = df[df["dish"].isin(weekly_dishes)]

shopping_list = consolidate_ingredients(filtered_df)

print(shopping_list)
