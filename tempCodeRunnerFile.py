import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# STEP 0: Load the Excel Dataset
# -----------------------------
file_path = 'EP_data_SFU_cleaned.xlsx'
df = pd.read_excel(file_path)

# STEP 1: Merge faculties where Realized < 2 into "Other"
df['Backgrounds'] = df['Backgrounds'].str.strip()
df_grouped = df.copy()
df_grouped.loc[df_grouped['Realized'] < 2, 'Backgrounds'] = 'Other'

# Group and aggregate
df_final = df_grouped.groupby('Backgrounds', as_index=False)['Realized'].sum()

# Force 'Other' to bottom
df_main = df_final[df_final['Backgrounds'] != 'Other'].sort_values(by='Realized', ascending=True)
df_other = df_final[df_final['Backgrounds'] == 'Other']
df_final_sorted = pd.concat([df_other, df_main], ignore_index=True)

# Calculate 50% projected increase
df_final_sorted['Projected_50%'] = df_final_sorted['Realized'] * 0.5

# -----------------------------
# 🌌 Dark Blue Background Visualization
# -----------------------------
plt.style.use('default')
plt.figure(figsize=(10, 7))
ax = plt.gca()

# Set dark blue background
dark_blue = '#001f3f'  # Navy/dark blue shade
ax.set_facecolor(dark_blue)
plt.gcf().patch.set_facecolor(dark_blue)

# Blue bars (current realized)
bars1 = plt.barh(df_final_sorted['Backgrounds'], df_final_sorted['Realized'], 
                 color='#3498db', label='Current Realized')

# Green bars (projected increase)
bars2 = plt.barh(df_final_sorted['Backgrounds'], df_final_sorted['Projected_50%'], 
                 left=df_final_sorted['Realized'], color='#2ecc71', label='Projected 50% Increase')

# Title & Axis Labels (in white)
plt.title('🚀 Realized + 50% Projected Increase by Faculty', fontsize=16, weight='bold', pad=20, color='white')
plt.xlabel('Number of Realized Exchanges', fontsize=13, color='white')
plt.ylabel('Faculty / Background', fontsize=13, color='white')
plt.xticks(fontsize=11, color='white')
plt.yticks(fontsize=11, color='white')

# Grid
plt.grid(axis='x', linestyle='--', alpha=0.3, color='white')

# Add bar labels (values) on top of green bars
for idx in range(len(df_final_sorted)):
    total = df_final_sorted['Realized'].iloc[idx] + df_final_sorted['Projected_50%'].iloc[idx]
    plt.text(total + 1, idx, f"{int(total)}", va='center', fontsize=10, color='white')

# Style tweaks
plt.legend(loc='best', fontsize=11, frameon=False, facecolor=dark_blue, labelcolor='white')
plt.tight_layout()

plt.show()
