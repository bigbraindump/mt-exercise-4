import pandas as pd
import matplotlib.pyplot as plt

import os
import sys
import re

def process_log_files(file_path):
    data = {'Epoch': [], 'Perplexity': []}
    epoch = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if "EPOCH" in line:
                    epoch += 1
                match = re.search(r"ppl:\s*(\d+\.\d+|\d+)", line)
                if match:
                    ppl = float(match.group(1))
                    data['Epoch'].append(epoch)
                    data['Perplexity'].append(ppl)
        df = pd.DataFrame(data)
        if not df.empty:
            print(f'Data loaded from {file_path}')
        return df
    except Exception as e:
        print(f'Error reading log file: {e}')
        return pd.DataFrame()

def plot(data, title, ylabel, output_filename):
    plt.figure(figsize=(10,6))
    plt.plot(data['Epoch'], data['Perplexity'], marker='o', label='Perplexity')
    plt.title(title)
    plt.xlabel('Epoch')
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.savefig(output_filename)
    plt.close()
    print(f"Plot saved: {output_filename}")

def main(log_folder):
    log_files = [f for f in os.listdir(log_folder) if f.endswith('.log')]
    for file in log_files:
        file_path = os.path.join(log_folder, file)
        data = process_log_files(file_path)
        if not data.empty:
            plot(data, 'Validation Perplexities', 'Perplexity',
                 os.path.join(log_folder, f'perplexities_{file.replace(".log", "")}.png'))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Use: python3 ./scripts/plots.py ./models')
    else:
        log_folder = sys.argv[1]
        main(log_folder)