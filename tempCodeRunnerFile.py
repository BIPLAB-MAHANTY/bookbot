def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     chars_dict = get_chars_dict(text)
#     print(chars_dict)
#     print_a_report(book_path,text,num_words,chars_dict)



# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def get_chars_dict(text):
#     chars = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars

# def print_a_report(book_path,text,num_words,chars_dict):
#     print(f"--- Begin report of {book_path} ---")
#     print(f"{num_words} words found in the document\n\n")

#     english_alphabets = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

#     for key,value in chars_dict.items():
#         if key in english_alphabets:
#             print(f"The '{key}' character was found {value} times")

#     print("--- End report ---")



# def get_book_text(path):
#     with open(path) as f:
#         return f.read()


# main()