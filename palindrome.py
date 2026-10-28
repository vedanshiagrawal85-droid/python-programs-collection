import re

def is_palindrome(text: str) -> bool:
    """Checks if a given string is a palindrome (ignoring casing and non-alphanumeric chars)."""
    clean_text = re.sub(r'[^a-zA-Z0-9]', '', str(text)).lower()
    return clean_text == clean_text[::-1]

if __name__ == "__main__":
    samples = ["Racecar", "A man, a plan, a canal: Panama", "12321", "Python", "hello"]
    print("--- Palindrome Verifier ---")
    for s in samples:
        print(f"'{s}' -> Palindrome: {is_palindrome(s)}")
