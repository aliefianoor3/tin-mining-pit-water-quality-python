import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("water_data.csv")

print("=== Simulated Water Quality: Former Tin-Mining Pits ===")
print("This dataset is simulated for learning purposes.")
print()

print("First five rows:")
print(df.head())

print()
print("Missing values:")
print(df.isna().sum())

print()
print("Summary statistics:")
print(df.describe())

print()
print("=== Key Findings ===")

lowest_ph_row = df.loc[df["pH"].idxmin()]
highest_iron_row = df.loc[df["Iron_mg_L"].idxmax()]

print(
    "Lowest pH:",
    lowest_ph_row["pH"],
    "at",
    lowest_ph_row["Pit_ID"]
)

print(
    "Highest iron concentration:",
    highest_iron_row["Iron_mg_L"],
    "mg/L at",
    highest_iron_row["Pit_ID"]
)

print()
print("=== Correlation Matrix ===")

selected_columns = [
    "Pit_Age_Years",
    "pH",
    "Dissolved_Oxygen_mg_L",
    "Turbidity_NTU",
    "TDS_mg_L",
    "Iron_mg_L",
    "Manganese_mg_L"
]

correlation_matrix = df[selected_columns].corr()

print(correlation_matrix)

print()
print("=== Plot: pH vs Iron Concentration ===")

plt.figure(figsize=(8, 5))

plt.scatter(
    df["pH"],
    df["Iron_mg_L"],
    color="darkorange",
    s=70
)

plt.title("Simulated Former Tin-Mining Pits: pH vs Iron Concentration")
plt.xlabel("pH")
plt.ylabel("Iron Concentration (mg/L)")
plt.grid(True, alpha=0.3)

plt.savefig("ph_vs_iron.png", dpi=300, bbox_inches="tight")

plt.show()

print()
print("=== Plot: Pit Age vs pH ===")

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Pit_Age_Years"],
    df["pH"],
    color="seagreen",
    s=70
)

plt.title("Simulated Former Tin-Mining Pits: Pit Age vs pH")
plt.xlabel("Pit Age (Years)")
plt.ylabel("pH")
plt.grid(True, alpha=0.3)

plt.savefig("pit_age_vs_ph.png", dpi=300, bbox_inches="tight")

plt.show()

print()
print("=== Saving Summary Statistics ===")

summary_statistics = df.describe()

summary_statistics.to_csv("water_quality_summary.csv")

print("Summary statistics saved as water_quality_summary.csv")

print("\n=== pH Category Summary ===")

def classify_ph(value):
    if value < 5.5:
        return "Acidic"
    elif value < 7.0:
        return "Slightly acidic"
    else:
        return "Near neutral or alkaline"

df["pH_category"] = df["pH"].apply(classify_ph)

ph_category_counts = df["pH_category"].value_counts()

category_order = [
    "Acidic",
    "Slightly acidic",
    "Near neutral or alkaline"
]

ph_category_counts = ph_category_counts.reindex(category_order, fill_value=0)

print(ph_category_counts)

plt.figure(figsize=(8, 5))

plt.bar(
    ph_category_counts.index,
    ph_category_counts.values,
    color=["#d73027", "#fc8d59", "#91cf60"]
)

plt.title("Number of Simulated Pits by pH Category")
plt.xlabel("pH category")
plt.ylabel("Number of pits")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.savefig("ph_category_count.png", dpi=300)
plt.close()

print("pH category chart saved as ph_category_count.png")