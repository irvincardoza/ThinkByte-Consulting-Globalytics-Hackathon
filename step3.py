import pandas as pd
import matplotlib.pyplot as plt

# Year range
years = ["2013", "2014", "2015", "2016", "2017", "2017/18", "2018/19", "2019/20", "2020/21", "2021/22", "2022/23"]

# SFU Data (Outbound_Term_Count)
sfu_counts = [253, 252, 289, 252, 283, 251, 292, 259, 0, 11, 264]

# AIESEC Data
aiesec_counts = [30, 28, 35, 25, 32, 24, 36, 28, 2, 5, 28]

# Create DataFrame
df = pd.DataFrame({
    "Year": years,
    "SFU": sfu_counts,
    "AIESEC": aiesec_counts
})

# Plotting both lines with dark background
plt.figure(figsize=(10,6), facecolor='#001f3f')
plt.style.use('default')
plt.rcParams['axes.facecolor'] = '#001f3f'
plt.rcParams['savefig.facecolor'] = '#001f3f'

# SFU line
plt.plot(df["Year"], df["SFU"], marker='o', linestyle='--', linewidth=2, color='#FFDC00', label='SFU')  # Yellow

# AIESEC line
plt.plot(df["Year"], df["AIESEC"], marker='s', linestyle='-', linewidth=2, color='#7FDBFF', label='AIESEC')  # Light blue

# Titles & labels with more padding
plt.title('SFU vs AIESEC Exchange Trends', color='white', fontsize=20, family='Arial', pad=20)
plt.xlabel('Year', color='white', fontsize=12, labelpad=15)
plt.ylabel('Student Count', color='white', fontsize=14, labelpad=20)

# Styling ticks
plt.xticks(rotation=45, color='white')
plt.yticks(color='white')

# Remove grid
plt.grid(False)

# Legend styling
plt.legend(facecolor='#001f3f', edgecolor='white', labelcolor='white', fontsize=10)

plt.tight_layout()
plt.show()
