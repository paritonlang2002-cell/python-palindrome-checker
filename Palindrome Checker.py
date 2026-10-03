def is_palindrome(text):
    cleaned = "".join(
        character.lower()
        for character in text
        if character.isalnum()
    )

    return cleaned == cleaned[::-1]


print("Palindrome Checker")
print("-" * 20)

text = input("Enter a word or phrase: ")

if is_palindrome(text):
    print("\nResult: It is a palindrome.")
else:
    print("\nResult: It is not a palindrome.")

input("\nPress Enter to exit...")


