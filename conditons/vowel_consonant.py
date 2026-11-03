# Program to check whether a given character is a Vowel or Consonant

ch = input("Enter a character: ")

# Check if the input is a single alphabet letter
if len(ch) == 1 and ch.isalpha():
    # Convert to lowercase to handle both uppercase and lowercase letters easily
    lower_ch = ch.lower()
    
    if lower_ch in ['a', 'e', 'i', 'o', 'u']:
        print(f"'{ch}' is a Vowel")
    else:
        print(f"'{ch}' is a Consonant")
else:
    print("Invalid input! Please enter a single alphabetic letter (not a number or symbol).")
