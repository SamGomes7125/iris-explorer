from preswald import connect, get_df, table, text, slider, plotly
import pandas as pd
import plotly.express as px

# Connect and load dataset (with headers)
connect()
df = get_df("iris")

# Confirm dataset loaded
text(f"✅ Iris Dataset Loaded: {len(df)} rows")

# App title
text("# Iris Dataset Explorer 🌸")

# Slider to filter by petal length
petal_length_threshold = slider("Minimum Petal Length", min_val=0.0, max_val=7.0, default=1.0)

# Filter the dataset
filtered_df = df[df["petal_length"] >= petal_length_threshold]

# Display filtered data
table(filtered_df, title="Filtered Iris Data")

# Scatter plot
fig = px.scatter(
    filtered_df,
    x="petal_length",
    y="petal_width",
    color="species",
    title="Petal Length vs. Petal Width"
)

# Show plot
plotly(fig)
