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

def convert_file_to_hexadecimal_string(file_name):
    file = open(f"./file_handling/files/{file_name}", "rb")
    
    lines_list = file.read()
    print(lines_list)

def BinaryToDecimal(binary):
    string = int(binary, 2)
    return string

def convert_binary_file_to_hex_string(file_name):
    hex_string = ""
    with open(f"./file_handling/files/{file_name}", "rb") as file:
        binary_data = file.read()
        decimal_data = int(binary_data,2)
        hex_string = hex(decimal_data).split("x")[1]
    
    return hex_string

def convert_hex_string_to_text(hex_string):
    string_value = bytes.fromhex(hex_string).decode('utf-8')
    return string_value

def write_text_file(text_content, filename):
    with open(filename, 'w') as output:
       output.write(text_content)
    print("Conversion completed successfully.")

def calculate_sum_of_nums_from_string(filename):
    file = open(f"./file_handling/files/{filename}", "r")

    lines_list = file.readlines();
    
    words_list = [line.replace("\n", " ").strip().split(" ") for line in lines_list]
    words_list = sum(words_list, []) #flat list ["hello", "my"m "name"] + ["Erick", ",I'm "] = ["hello", "my"m "name", "Erick", ",I'm "]

    number_list = []
    for word in words_list:
        try:
            number = int(word)
            number_list.append(number)
        except:
            print(f"{word} is not a number")
    
    return sum(number_list)


# 1. Write a Python program that reads a text file and prints the number of
# lines, words, and characters in the file.
# content_file = read_txt_file("python.txt")
# print(content_file)

# # 2. Write a Python program that reads a CSV file and converts it into a dictionary. 
# # Each row of the CSV file should be a key-value pair in the dictionary.
# csv_data = read_csv_file("enterprise-survey.csv")
# print(len(csv_data))

# 3. Write a Python program that reads a binary file and converts it into a 
# hexadecimal string. The program should output the hexadecimal string to a text file.
hex_string = convert_binary_file_to_hex_string("python.bin")
string_content = convert_hex_string_to_text(hex_string)
write_text_file(string_content, "hex_to_text_file.txt")

#  4. Write a Python program that reads a text file containing numbers and calculates 
# the sum of all the numbers in the file.
sum_of_numbers = calculate_sum_of_nums_from_string("numbers_file.txt")
print(sum_of_numbers)




## KEY SHORTCUTS CTRL + P + L