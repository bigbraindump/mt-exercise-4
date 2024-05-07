import sys
import csv
import re
import os  

def extract_ppl_values(log_file):
    ppl_values = []
    evaluation_pattern = re.compile(r"ppl:\s+([\d.]+)")
    with open(log_file, 'r') as file:
        for line in file:
            match = evaluation_pattern.search(line)
            if match:
                ppl = float(match.group(1))
                ppl_values.append(ppl)
    return ppl_values

def main():
    log_files = sys.argv[1:-1]
    output_csv = sys.argv[-1]

    all_ppl_values = []
    
    log_names = [os.path.splitext(os.path.basename(log_file))[0] for log_file in log_files]
    
    for log_file in log_files:
        print(f"Processing log file: {log_file}")
        ppl_values = extract_ppl_values(log_file)
        all_ppl_values.append(ppl_values)

    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['validation ppl'] + log_names 
        writer.writerow(header)
        
        # initialize step numbers
        step_values = range(500, 40501, 500)
        for step_value, row in zip(step_values, zip(*all_ppl_values)):
            writer.writerow([step_value] + list(row))

if __name__ == "__main__":
    main()
