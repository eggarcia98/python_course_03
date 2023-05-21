from functools import reduce
def read_txt_file(file_name):
    file = open("./file_handling/files/python.txt", "r")
    
    lines_list = file.readlines()
    
    words_list = [line.strip().split(" ") for line in lines_list]
    words_list = sum(words_list, []) #flat list ["hello", "my"m "name"] + ["Erick", ",I'm "] = ["hello", "my"m "name", "Erick", ",I'm "]
    
    lines_count = len(lines_list)
    words_count = len(words_list)
    characters_count = len(" ".join(words_list))

    return {
        " ": lines_count, 
        "words_count": words_count, 
        "characters_count": characters_count}


# 1. Write a Python program that reads a text file and prints the number of
# lines, words, and characters in the file.
content_file = read_txt_file("sda")
print(content_file)