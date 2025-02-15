import collections
def main(file_path):
    with open(f"{file_path}") as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_characters(text):
    lowered_test = text.lower()
    count_dic = {}
    charset = set(lowered_test)
    for character in charset:
        count_dic.update({f"{character}" : lowered_test.count(f"{character}")})
    return count_dic

def sort_on(dic):
    return len(dic)

if __name__ == '__main__':
    file_path = "books/frankenstein.txt"
    #print(f"--- Begin report of {file_path} ---")
    #print(f"{word_count(main(file_path))} words found in the document")
    #print()
    #print()
    count_dic = count_characters(main(file_path))
    return_set = set(count_dic)
    return_list = list(return_set)
    new_return_list = []
    for char in return_list:
        if char.isalpha():
            new_return_list.append(char)
    new_return_list.sort()
    for value_set in new_return_list:
        if value_set.isalpha():
            print(f"The \'{value_set}\' character was found {count_dic.get(value_set)} times")
    #print("--- End report ---")