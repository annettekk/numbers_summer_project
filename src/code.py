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
    new_file_name = input("Enter the results file name: ")
    new_file = results_dir + new_file_name
    #os.mkdir(results_dir)
    with open(new_file, 'w') as f_out:
        f_out.write(str(sum))

#new_file = os.path.join(results_dir, new_file_name)