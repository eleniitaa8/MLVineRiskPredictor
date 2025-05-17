# src/eda.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(df: pd.DataFrame, output_dir: str):
    """
    Plot and save a histogram for each numeric column in df.
    """
    os.makedirs(output_dir, exist_ok=True)
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        plt.figure(figsize=(6,4))
        sns.histplot(df[col].dropna(), bins=30, kde=False)
        plt.title(f"Histogram of {col}")
        plt.xlabel(col); plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f"hist_{col}.png"))
        plt.close()

def plot_correlation_matrix(df: pd.DataFrame, output_path: str):
    """
    Compute df.corr(), plot a heatmap, and save it.
    """
    corr = df.corr()
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Feature Correlation Matrix")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
