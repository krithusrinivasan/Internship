#!/usr/bin/env python
# coding: utf-8

# In[70]:


import re 
# import Libraries


# In[4]:


#1 #Sample Text
sample_text ='Python Exercises, PHP exercises.'


# In[6]:


# Replace space, comma, or dot with a colon
expected_output = re.sub(r'[ ,.]', ':', sample_text)


# In[8]:


# Print Output
print(expected_output)


# In[6]:


#2 # import Libraries
import pandas as pd


# In[21]:


# Data input
dictionary = {'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']}


# In[22]:


# dataframe creation
df = pd.DataFrame(dictionary)


# In[52]:


# Function to clean the data
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text) # remove non-alphabetic character and use only words
    text = re.sub(r'\bXXXXX\b', '', text) # remove unwanted words
    return text


# In[53]:


# Apply the clean_text function to the 'SUMMARY' column
df['SUMMARY'] = df['SUMMARY'].apply(clean_text)


# In[54]:


# pritn output
print(df)


# In[55]:


# 3
def find_long_words(text):
    # To find words of at least 4 characters
    string = re.compile(r'\b\w{4,}\b')
    # Find matches in the text
    long_words = string.findall(text)
    return long_words


# In[56]:


text = 'Create a function in python to find all words that are at least 4 characters long in a string.'
result = find_long_words(text)
print(result)


# In[57]:


# 4
def find_specific_length_words(text):
    # Regex pattern to find words with 3, 4, or 5 characters
    pattern = re.compile(r'\b\w{3,5}\b')
    # Find matches in the text
    all_words = pattern.findall(text)
    # Find words that are exactly 3, 4, or 5 characters long
    specific_length_words = [word for word in all_words if 3 <= len(word) <= 5]
    return specific_length_words


# In[58]:


text = 'Create a function in python to find all three, four, and five character words in a string.'
result = find_specific_length_words(text)
print(result)


# In[56]:


# 5
def clean_strings(string_list):
    # Regex pattern to match parentheses and their contents
    pattern = re.compile(r"\(|\)")
    # Process each string in the list
    cleaned_strings = []
    for s in string_list:
        cleaned = re.sub(pattern,"", s)
        cleaned_strings.append(cleaned)
    return cleaned_strings


# In[57]:


# data input
data = ["example (.com)",
    "hr@fliprobo (.com)",
    "github (.com)",
    "Hello (Data Science World)",
    "Data (Scientist)"]


# In[58]:


# Remove parentheses and their contents
output = clean_strings(data)
for item in output:
    print(item)


# In[71]:


# 6 # Define the function with a parameter for the file path
def remove_parentheses_from_file(file_path):
    # Read the text file and store the content in a variable
    with open(file_path, 'r') as file:
        text = file.read()
    # Regular expressions to remove the parenthesis area
    new_text = re.sub(r"\s*\([^)]*\)", "", text)
    # Print the new text
    print(new_text)
    # Optionally, write the cleaned text back to the file
    with open(file_path, 'w') as file:
        file.write(new_text)


# In[74]:


# Specify the file path
file_path = r"C:\Users\user\Desktop\samplefile.txt"


# In[75]:


# Call the function with the file path
remove_parentheses_from_file(file_path)


# In[76]:


# 7 
def split_by_uppercase(input_string):
    # To split at positions where an uppercase letter is followed by lowercase letters
    output = re.findall(r'[A-Z][a-z]*', input_string)
    return output


# In[77]:


# Sample text
sample_text = "ImportanceOfRegularExpressionsInPython"


# In[78]:


# Call the function and print the result
result = split_by_uppercase(sample_text)
print(result)


# In[79]:


# 8
def add_spaces_before_numbers(text_input):
    # To add a space before numbers followed by word characters
    spaced_text = re.sub(r'(\d)', r' \1', text_input)
    return spaced_text


# In[80]:


# Sample input
sentence = "RegularExpression1IsAn2ImportantTopic3InPython"


# In[81]:


# Call the function and print the result
result = add_spaces_before_numbers(sentence)
print(result)


# In[101]:


# 9
def insert_spaces_before_capitals_and_numbers(text_input):
    # To add a space before capital letters and numbers
    spaced_text = re.sub(r'(?<!^)(?<!\s)([A-Z0-9])', r' \1', text_input)
    # Strip leading space if any
    spaced_text = spaced_text.strip()
    return spaced_text


# In[102]:


# Sample input
sample_string = "RegularExpression1IsAn2ImportantTopic3InPython"


# In[103]:


# Call the function and print the result
result = insert_spaces_before_capitals_and_numbers(sample_string)
print(result)


# In[118]:


# 10
import pandas as pd


# In[119]:


# Read the data link
url = 'https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv'
# Read the data into a DataFrame
df = pd.read_csv(url)


# In[120]:


# Extract the first 6 letters of each country and store in a new column name first_five_letters
df['first_five_letters'] = df['Country'].str[:6]


# In[121]:


# Display DataFrame
print(df)


# In[122]:


# 11
def match_string(input_string):
    # Regular expression pattern to match a string containing only letters, numbers, and underscores
    pattern = r'^[A-Za-z0-9_]+$'
    # Use re.match to check if the entire string matches the pattern
    if re.match(pattern, input_string):
        return True
    else:
        return False


# In[125]:


# Test the function
test_string_1 = "Sample_text123"
test_string_2 = "Invalid-Sample!"


# In[126]:


print(match_string(test_string_1))  
print(match_string(test_string_2))  


# In[127]:


# 12
def start_with_number(input_string, number):
    # Regular expression pattern that checks if the string starts with the specific number
    pattern = r'^' + str(number)
    # To check if the string starts with the specific number
    if re.match(pattern, input_string):
        return True
    else:
        return False


# In[131]:


# Test the function
test_string_1 = "123abc"
test_string_2 = "864def"
specific_number = 123


# In[132]:


# Print thr results
print(start_with_number(test_string_1, specific_number))  
print(start_with_number(test_string_2, specific_number))  


# In[133]:


# 13
def remove_leading_zeros(ip_address):
    # Regular expression to remove leading zeros from each block of the IP address
    regex_pattern = r'\b0+(\d)'
    new_ip_address = re.sub(regex_pattern, r'\1', ip_address)
    return new_ip_address


# In[134]:


# Test the function
test_ip_address = "192.168.001.001"
print(remove_leading_zeros(test_ip_address))


# In[135]:


# 14
def extract_date_from_file(file_path):
    # Read the text file content
    with open(file_path, 'r') as file:
        content = file.read()
    # Regular expression to match "Month name followed by day number and year"
    date_pattern = r'\b([A-Z][a-z]+ \d{1,2}(st|nd|rd|th)? \d{4})\b'
    # Search for the date pattern in the content
    match = re.search(date_pattern, content)
    # Return the matched date string if found
    if match:
        return match.group(0)
    else:
        return "No date found in the specified format."


# In[137]:


# Test the function
file_path = r"C:\Users\user\Desktop\sampletextfile.txt"
print(extract_date_from_file(file_path))


# In[138]:


# 15
def search_words(text, words):
    # Join the words to form a regex pattern
    pattern = r'\b(' + '|'.join(words) + r')\b'
    # To find all occurrences of the pattern in the given text
    found_words = re.findall(pattern, text)
    return found_words


# In[139]:


# Sample text and words to search
sample_text = 'The quick brown fox jumps over the lazy dog.'
search_words_list = ['fox', 'dog', 'horse']


# In[140]:


# Call the function
matched_words = search_words(sample_text, search_words_list)
print(matched_words)


# In[141]:


# 16
def search_word_with_location(text, word):
    # Regex pattern for the word
    search_pattern = re.compile(r'\b' + re.escape(word) + r'\b')
    # Search the word in the text
    match = search_pattern.search(text)
    if match:
        return match.group(), match.start(), match.end()
    else:
        return None


# In[142]:


# Sample text and word to search
sample_text = 'The quick brown fox jumps over the lazy dog.'
search_word = 'fox'


# In[143]:


# Call the function
result = search_word_with_location(sample_text, search_word)
if result:
    print(f"Found '{result[0]}' at position {result[1]} to {result[2]}")
else:
    print(f"'{search_word}' not found in the text.")


# In[144]:


#17
def find_substrings(text, pattern):
    # Regex pattern to find all occurrences of the substring
    matches_found = re.finditer(pattern, text)
    # Collect the results in a list
    results = [(match.group(), match.start(), match.end()) for match in matches_found]
    return results


# In[145]:


# Sample text and pattern to search
sample_text = 'Python exercises, PHP exercises, C# exercises'
search_pattern = 'exercises'


# In[146]:


# Call the function
result = find_substrings(sample_text, search_pattern)


# In[147]:


# Print the results
for match, start, end in result:
    print(f"Found '{match}' from position {start} to {end}")


# In[149]:


# 18
def find_occurrences(text, pattern):
    # To get an iterator over all matches
    matches = re.finditer(pattern, text)
    # List creation to store the results
    results = [(match.group(), match.start(), match.end()) for match in matches]
    return results


# In[150]:


# Sample text and pattern to search
sample_text = 'Data Science, Data Science, Data Science'
search_pattern = 'Science'


# In[151]:


# Call the function
result = find_occurrences(sample_text, search_pattern)


# In[152]:


# Print the results
for match, start, end in result:
    print(f"Found '{match}' at position {start}-{end}")


# In[154]:


# 19
from datetime import datetime


# In[155]:


def convert_date_format(date_sample):
    # Input date string to a datetime object
    date_obj = datetime.strptime(date_sample, '%Y-%m-%d')
    # Datetime format object to the desired string format
    new_date_sample = date_obj.strftime('%d-%m-%Y')
    return new_date_sample


# In[156]:


input_date = '2024-08-24'
output_date = convert_date_format(input_date)
print("Converted date:", output_date)


# In[157]:


# 20
def find_decimal_numbers(text):
    # Regular expression pattern
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    # Find all matches in the provided text
    result = pattern.findall(text)
    return result


# In[158]:


# Sample text and output
sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
output = find_decimal_numbers(sample_text)
print("Matched decimal numbers:", output)


# In[159]:


# 21
def find_numbers_and_positions(text):
    # Regular expression pattern to find numbers
    pattern = re.compile(r'\d+')
    # Find all matches with their positions
    matches = pattern.finditer(text)
    # Iterate through the matches and print the numbers with their positions
    for match in matches:
        number = match.group()
        position = match.start()
        print(f"Number: {number}, Position: {position}")


# In[160]:


# Sample text and result
sample_text = "In 2024, I plan to complete 2 upskill course and attend minimum 10 interviews."
find_numbers_and_positions(sample_text)


# In[161]:


# 22
def extract_max_numeric_value(text):
    # Regular expression pattern to find all numbers
    regex_pattern = re.compile(r'\d+') 
    # Find all matches of the pattern in the text
    numbers = regex_pattern.findall(text) 
    # Convert the list of strings to a list of integers
    numbers = [int(num) for num in numbers]
    # Return the maximum number from the list
    max_value = max(numbers)
    return max_value


# In[162]:


# Sample text and result
sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
result = extract_max_numeric_value(sample_text)
print(f"The maximum numeric value is: {result}")


# In[163]:


# 23
def insert_spaces(text):
    # Regular expression to find positions where capital letters are preceded by lowercase letters or another capital letter
    pattern = re.compile(r'(?<=[a-z])(?=[A-Z])') 
    # Insert space at those positions
    spaced_text = pattern.sub(' ', text)
    return spaced_text


# In[164]:


# Sample text and result
sample_text = "RegularExpressionIsAnImportantTopicInPython"
result = insert_spaces(sample_text)
print(result)


# In[167]:


# 24
def find_uppercase_sequences(text):
    # Regular expression to find sequences of one uppercase letter followed by lowercase letters
    regex_pattern = re.compile(r'[A-Z][a-z]+')
    # Find all matching sequences in the text
    matches = regex_pattern.findall(text)
    return matches


# In[169]:


# Sample text and result
sample_text = "This is a Very Important assignment regarding Regular expression In Python."
result = find_uppercase_sequences(sample_text)
print(result)


# In[218]:


# 25
def remove_duplicate_words(sentence):
    # Regular expression to find continuous duplicate words
    pattern = re.compile(r'\b(\w+)\b(?:\s+\1\b)+', re.IGNORECASE)
    # Function to replace the match with just one occurrence of the word
    def replace(match):
        return match.group(1)
    # Replace duplicates with a single occurrence
    cleaned_sentence = pattern.sub(replace, sentence)
    return cleaned_sentence


# In[219]:


# Sample text and result
sample_text = "Hello hello world world"
result = remove_duplicate_words(sample_text)
print(result)


# In[220]:


# 26
def ends_with_alphanumeric(input_string):
    # Regular expression pattern to check if the string ends with an alphanumeric character
    pattern = re.compile(r'\w$')
    # Search for the pattern in the input string
    if pattern.search(input_string):
        return True
    else:
        return False


# In[221]:


# sample text
sample_text_1 = "Hello123"
sample_text_2 = "Hello123!"
sample_text_3 = "Hello_"


# In[222]:


# Print Output
print(ends_with_alphanumeric(sample_text_1))  
print(ends_with_alphanumeric(sample_text_2))  
print(ends_with_alphanumeric(sample_text_3))  


# In[223]:


# 27
def extract_hashtags(text):
    # Regex pattern to match hashtags
    pattern = r'#\w+'
    # Find all hashtags in the text
    hashtags = re.findall(pattern, text)
    return hashtags


# In[224]:


# Sample text
sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""


# In[225]:


# Output
output = extract_hashtags(sample_text)
print(output)


# In[226]:


# 28
def remove_unwanted_symbols(text):
    # Regular expression to match the pattern <U+..>
    pattern = r'<U\+[A-F0-9]{4}>'
    # Replace the matched patterns with an empty string
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text


# In[227]:


# Sample text
sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"


# In[228]:


# Removing <U+..> symbols
result = remove_unwanted_symbols(sample_text)
print(result)


# In[229]:


# 29
def extract_dates(file_path):
    # Read the content of the text file
    with open(file_path, 'r') as file:
        content = file.read()
    # Regular expression pattern to match dates in the format dd-mm-yyyy
    date_pattern = re.compile(r'\b\d{2}-\d{2}-\d{4}\b')
    # Find all dates that match the pattern
    dates = date_pattern.findall(content)
    return dates


# In[232]:


# Specify the path file
file_path = r"C:\Users\user\Desktop\samplefile.txt" 


# In[233]:


# Call the function to extract dates
extracted_dates = extract_dates(file_path)


# In[234]:


# Print the extracted dates
print(extracted_dates)


# In[235]:


# 30
def remove_short_words(text):
    # Regex pattern to match words of length 2 to 4
    pattern = re.compile(r'\b\w{2,4}\b')
    # Replace the matched words with an empty string
    result = pattern.sub('', text)
    # Remove any extra spaces that might be left after removing words
    cleaned_text = re.sub(r'\s{2,}', ' ', result).strip()
    return cleaned_text


# In[236]:


# Sample text
sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."


# In[237]:


# Call the function and print the result
output = remove_short_words(sample_text)
print(output)


# In[ ]:




