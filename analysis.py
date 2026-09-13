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