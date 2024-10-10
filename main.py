def main():
    text = book_text()
    num_words = book_words(text)      
    #print(f"{num_words} words found in the document!")
    num_chars = book_characters(text)
    #print(f"The amount of each character is: {num_chars}")
    organized = sort_mess(num_words,num_chars)

def sort_mess(num_words,num_chars):


def book_characters(text):
    chars = {}
    low_text = text.lower()
    for char in low_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars        

def book_words(text):
    words = text.split()
    return len(words)

def book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

main()