ch = input("Enter a character: ")

if len(ch) == 1 and ch.isalpha():
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(f"'{ch}' is a Vowel")
    else:
        print(f"'{ch}' is a Consonant")
else:
    print("Invalid input! Please enter a single alphabetic letter (not a number or symbol).")
