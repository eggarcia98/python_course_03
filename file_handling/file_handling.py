import csv




def read_txt_file(file_name):
    file = open(f"./file_handling/files/{file_name}", "r")
    
    lines_list = file.readlines()
    
    words_list = [line.strip().split(" ") for line in lines_list]
    words_list = sum(words_list, []) #flat list ["hello", "my"m "name"] + ["Erick", ",I'm "] = ["hello", "my"m "name", "Erick", ",I'm "]
    
    lines_count = len(lines_list)
    words_count = len(words_list)
    characters_count = len(" ".join(words_list))

    return {
        "lines_count": lines_count, 
        "words_count": words_count, 
        "characters_count": characters_count}

def read_csv_file(file_name):
    file = open(f"./file_handling/files/{file_name}", "r")

    reader = csv.reader(file.readlines(), quotechar='"', delimiter=',')


    header = next(reader)
    
    rows_dict = []
    for row_data in reader:
        key_par_values = []
        for column_index in range(0, len(row_data)):
            key_par_values.append((header[column_index], row_data[column_index]))
        rows_dict.append(dict(key_par_values))
    
    return rows_dict

# 1. Write a Python program that reads a text file and prints the number of
# lines, words, and characters in the file.
content_file = read_txt_file("python.txt")
print(content_file)

# 2. Write a Python program that reads a CSV file and converts it into a dictionary. 
# Each row of the CSV file should be a key-value pair in the dictionary.
csv_data = read_csv_file("enterprise-survey.csv")
print(len(csv_data))

