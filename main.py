def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = book_words(text)      
    num_chars = book_characters(text)
    organized = sort_mess(num_chars)

    print(f"=== Begin report of {book_path} ===")
    print(f"{num_words} words found in the document!")
    print()
    for char in organized:
        print(f"The '{char['char']}' character was found {char['amount']} times")
    print("=== End report ===")

def sort_on(dict):
    return dict["amount"]

def sort_mess(num_chars):
    mess = []
    for char, num in num_chars.items():
        mess.append({"char": char, "amount": num})
    mess.sort(reverse=True, key=sort_on)
    return mess

def book_characters(text):
    chars = {}
    low_text = text.lower()
    for char in low_text:
        if char in chars:
            chars[char] += 1
        elif char.isalpha():
            chars[char] = 1
    return chars        

def book_words(text):
    words = text.split()
    return len(words)

def book_text(path):
    with open(path) as f:
        return f.read()

main()