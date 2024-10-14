# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    count = get_word_count(file_contents)
    char_counts = get_char_count(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document.\n\n")
    
    for item in char_counts:
        print(f"The '{item['char']}' character was found {item['num']} times")



# Split into array of words and return count
def get_word_count(string):
    words = string.split()
    count = len(words)

    return count

# Takes a dict and returns a sorted array of dicts.
def get_char_count(source_dict):
    lowered = source_dict.lower()
    counts = {}
    retval = []

    # As long as the character is an alphabet character, add or increment count.
    for char in lowered:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    
    # Build array of dictionaries.
    for char in counts:
        retval.append({"char": char, "num": counts[char]})

    # Sort by character counts
    retval.sort(reverse=True, key=sort_on)

    return retval


main()