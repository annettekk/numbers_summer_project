#import os

def sum_num(filename):
    with open(filename, 'r') as f:
        total = sum(float(line.strip()) for line in f)
        return total 

if __name__ == "__main__":
    data_filename = "./data/input_file.txt"
    sum = sum_num(data_filename)
    print(f"Sum of numbers in the file {data_filename}: {sum}")
    
    
    results_dir = './results/'
    while True:
        new_file_name = input("Enter the results file name: ").strip()
        if new_file_name:
            break
        print("Filename cannot be empty. Please enter a valid name.")
    
    if not new_file_name.endswith(".txt"):
        new_file_name += ".txt"
    new_file = results_dir + new_file_name
    with open(new_file, 'w') as f_out:
        f_out.write(str(sum))

#new_file = os.path.join(results_dir, new_file_name)