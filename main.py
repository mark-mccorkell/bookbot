def get_book_text(file):
    with open(file) as f:
        return f.read()
    
def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

main()