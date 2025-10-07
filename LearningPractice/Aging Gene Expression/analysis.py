import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os



# **Loading data**

# Paths relative script location
script_dir = Path(os.path.dirname(__file__))
data_path = script_dir / "Data" / "mouse_expression.csv"

df = pd.read_csv(data_path)

# Expression change with aging
df["Change"] = df["Old"] - df["Young"]

# Summary
print("Top genes changing with aging:")
print(df.sort_values("Change", ascending=False))

# Visualization 1: Bar plot
plt.figure(figsize=(10, 5))
colors = ["red" if x > 0 else "green" for x in df["Change"]]
plt.bar(df["Gene"], df["Change"], color=colors)
plt.axhline(0, color="black", linestyle="--")
plt.title("Gene Expression Change with Aging (Old - Young)")
plt.ylabel("Change in Expression")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization 2: Heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(df.set_index("Gene")[["Young", "Old"]],
            cmap="coolwarm", annot=True, fmt=".1f")
plt.title("Expression Levels in Young vs Old Mice")
plt.tight_layout()
plt.show()
