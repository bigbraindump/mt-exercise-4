import pandas as pd
import matplotlib.pyplot as plt

def plot_ppl_data(csv_file):
    df = pd.read_csv(csv_file)
    plt.figure(figsize=(10, 6))
    for column in df.columns[1:]:
        plt.plot(df['validation ppl'], df[column], marker='o', label=column)
    plt.title('Perplexity Score by Model Over Steps')
    plt.xlabel('Validation PPL')
    plt.ylabel('Perplexity')
    plt.legend(title="Model")  
    plt.grid(True)
    plt.savefig('ppl_plot.png')
    plt.show()

if __name__ == "__main__":
    csv_file_path = 'ppl.csv'  
    plot_ppl_data(csv_file_path)