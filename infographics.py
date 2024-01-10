# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:47:37 2024

@author: Abhi
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel("the trends and composition of the company's assets across various categories.xlsx")

df.describe
fig, axs = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Line Plot - Total over Time
sns.lineplot(x='Total', y='Corporate bonds (2)', data=df, marker='o', color='blue', ax=axs[0, 0])
axs[0, 0].set_title('Total vs Corporate Bonds')
axs[0, 0].set_xlabel('Total Asset Value')
axs[0, 0].set_ylabel('Corporate Bonds')
axs[0, 0].grid(True)

# Plot 2: Bar Plot - International securities' vs 'Other securities 
sns.barplot(x='Asset Category', y='Value', data=df[['International securities', 'Other securities     (1)(3)']].melt(var_name='Asset Category', value_name='Value'), color='green', ax=axs[0, 1])
axs[0, 1].set_title('International Securities vs Other Securities')
axs[0, 1].set_xlabel('Asset Category')
axs[0, 1].set_ylabel('Value')
axs[0, 1].grid(True)

# Plot 3: Histogram - Distribution of Federal Government Securities
sns.histplot(df['State/local government securities'], bins=20, kde=True, color='orange', ax=axs[1, 0])
axs[1, 0].set_title('Distribution of State/Local Govt Securities')
axs[1, 0].set_xlabel('State/Local Government Securities')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].grid(True)

# Plot 4: Pie Plot - Composition of Asset Types
asset_types = ['Corporate stocks', 'Corporate bonds', 'Federal government securities', 'International securities', 
               'Mortgages', 'State/local government securities', 'Cash and short-term investments', 'Other securities (1)(3)']
asset_values = [df['International securities'].sum(), df['State/local government securities'].sum(), 
                df['Cash and short-term investments'].sum() if 'Cash and short-term investments' in df.columns else 0,  # Check if the column exists
                df['Other securities     (1)(3)'].sum(),
                df['Corporate stocks (1)'].sum(), df['Corporate bonds (2)'].sum(), 
                df['Federal government securities (2)'].sum(), df['Mortgages'].sum()]

axs[1, 1].pie(asset_values, labels=asset_types, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3', n_colors=len(asset_types)))
axs[1, 1].set_title('Composition of Asset Types')

# Overall Figure Title
fig.suptitle('Asset Analysis - 2016Q2', fontsize=16)

# Adjust layout to prevent overlap of titles
fig.tight_layout(rect=[0, 0.03, 1, 0.95])

# Create a new figure for the description
fig_desc = plt.figure(figsize=(15, 3))
plt.text(0, 0, "Figure Descriptions: The 'Asset Analysis - report visualizes the trends and composition of the company's assets across various categories. It features four distinct plots:\n\n1.Total vs Corporate Bonds : This line plot tracks the growth of the total asset value over time and compares it with the growth of corporate bond assets. By analyzing the relative movement of these two lines, the investment manager can determine if the company's assets are shifting towards more stable investments.(Line Plot):\n"\
         "The blue line plot shows the relationship between the total asset value and corporate bonds over time.\n\n"\
         "2. International Securities vs Other Securities : This green bar plot presents a side-by-side comparison of the total value of international securities and other securities. It allows the investment manager to evaluate the relative size and significance of these two asset categories within the company's portfolio.(Bar Plot):\n"\
         "The green bar plot compares the values of international securities and other securities as different asset categories.\n\n"\
         "3. Distribution of State/Local Govt Securities (Histogram):\n"\
         " The orange histogram illustrates the distribution of state/local government securities in the company's portfolio. By analyzing the histogram, the investment manager can determine the prevalence of these securities, as well as the distribution of their values across the portfolio.The orange histogram represents the distribution of state/local government securities.\n\n"\
         "4. Composition of Asset Types (Pie Plot):\n"\
         " This pie chart showcases the composition of various asset types based on their total values. By comparing the proportions of each asset type in the pie chart, the investment manager can assess the overall balance and diversification of the company's asset portfolio.The pie chart illustrates the composition of various asset types based on their total values.\n\n"\
         "Name: Abhishek Aeera\n"\
         "Student ID: 22097107", 
         ha='left', va='center', fontsize=14, wrap=True)
plt.axis('off')