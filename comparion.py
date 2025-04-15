import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# STEP 0: Load the Excel Dataset
# -----------------------------
file_path = 'EP_data_SFU.xlsx'
df = pd.read_excel(file_path)

# STEP 1: Clean faculty names
df['Backgrounds'] = df['Backgrounds'].str.strip()

# Filter out rows where Realized <= 1
df = df[df['Realized'] > 1]

# Group and aggregate
df_final = df.groupby('Backgrounds', as_index=False)['Realized'].sum()

# Sort by realized count
df_final_sorted = df_final.sort_values(by='Realized', ascending=True).reset_index(drop=True)

# Calculate 50% projected increase
df_final_sorted['Projected_50%'] = df_final_sorted['Realized'] * 0.5

# -----------------------------
# Set font globally
# -----------------------------
plt.rcParams['font.family'] = 'Arial'

# -----------------------------
# 🌌 Dark Blue Background Visualization
# -----------------------------
plt.style.use('default')
plt.figure(figsize=(10, 7))
ax = plt.gca()

# Set dark blue background
dark_blue = '#001f3f'
ax.set_facecolor(dark_blue)
plt.gcf().patch.set_facecolor(dark_blue)

# Blue bars (current realized)
plt.barh(df_final_sorted['Backgrounds'], df_final_sorted['Realized'], 
         color='#3498db', label='Current Realized')

# Green bars (projected increase)
plt.barh(df_final_sorted['Backgrounds'], df_final_sorted['Projected_50%'], 
         left=df_final_sorted['Realized'], color='#2ecc71', label='Projected 50% Increase')

# Title & Axis Labels (in white)
plt.title('Faculty vs Exchange Students', fontsize=16, weight='bold', pad=20, color='white')
plt.xlabel('Number of Realized Exchanges', fontsize=13, color='white')
plt.ylabel('Faculty / Background', fontsize=13, color='white')
plt.xticks(fontsize=11, color='white')
plt.yticks(fontsize=11, color='white')

# Grid
plt.grid(axis='x', linestyle='--', alpha=0.3, color='white')

# No text inside bars anymore!

# Legend and layout
plt.legend(loc='best', fontsize=11, frameon=False, facecolor=dark_blue, labelcolor='white')
plt.tight_layout()

plt.show()
