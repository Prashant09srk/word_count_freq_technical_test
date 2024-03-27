import os
import re

def word_counter(file_name):
    try:
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"Error: File {file_name} is not available")
        
        if not file_name.lower().endswith('.txt'):
            raise ValueError("Error: File {file_name} must be of .txt")
        
        if os.path.getsize(file_name) == 0:
            raise ValueError(f"Error: File '{file_name}' is empty.")
        
        dict_word_count = {}
        
        with open(file_name, 'r' ) as file:
            for line in file:
                line = re.sub(r'[^a-zA-Z\s]', '', line)
                line_list = line.lower().split()
                line_list = [item for item in line_list if len(item) != 1] # remove single characters
                
                for word in line_list:
                    dict_word_count[word] = dict_word_count.get(word, 0) + 1 

            dict_word_count = dict(sorted(dict_word_count.items()))
            dict_word_count_final  = dict(sorted(dict_word_count.items(), key=lambda item: item[1], reverse=True))
            
            if len(dict_word_count_final) == 0:
                raise ValueError(f"Error: The file '{file_name}' consists only of whitespace characters, special characters or numbers")

            for key, val in dict_word_count_final.items():
                print(f"{key.ljust(15)} : {val*'*'}")
                       
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    except ValueError as e:
        raise ValueError(e)
    except Exception as err:
        raise Exception(f"An error occurred: {err}")

# provide the filename
file_name = r"word_file.txt"

word_counter(file_name)
