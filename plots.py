import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

def plot_from_csv(csv_file_path, output_filename):
    df = pd.read_csv(csv_file_path)
    plt.figure(figsize=(10, 6))
    colors = plt.cm.viridis(np.linspace(0, 1, df.shape[1]))  # Generate colors for each column

    for (column, color) in zip(df.columns, colors):
        plt.plot(df.index, df[column], marker='o', color=color, label=column)
        
    plt.title('Plot of CSV Data')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)
    plt.savefig(output_filename)
    plt.close()
    print(f"Plot saved: {output_filename}")

def main(csv_file_path):
    plot_from_csv(csv_file_path, 'plot_output.png')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 plots.py <path_to_csv>')
    else:
        csv_file_path = sys.argv[0]
        main(csv_file_path)