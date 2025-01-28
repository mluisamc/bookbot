def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    sorted_dict  = dict(sorted(count_characters(file_contents).items()))
    for char in sorted_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {sorted_dict[char]} times")
    print("---End report ---")

def count_words(content):
    return len(content.split())

def count_characters(content):
    result = {}
    for char in content.lower():
        if char in result:
            result[char] += 1
        else :
            result[char] = 1
    return result

main()