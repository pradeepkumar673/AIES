# Implement Vowel Identification using rule-based logic.

def identify_vowels(sentence):
    vowels = set('aeiouAEIOU')
    result = []
    for char in sentence:
        if char.isalpha():
            if char in vowels:
                result.append((char, 'Vowel'))
            else:
                result.append((char, 'Consonant'))
    return result

def count_vowels(sentence):
    vowels = set('aeiouAEIOU')
    return sum(1 for c in sentence if c in vowels)

def extract_vowels(sentence):
    vowels = set('aeiouAEIOU')
    return [c for c in sentence if c in vowels]

sentence = "Artificial Intelligence and Expert Systems"

print("Vowel Identification - Rule-Based Logic")
print(f"Sentence: {sentence}\n")

classifications = identify_vowels(sentence)
print("Character Classification:")
for char, label in classifications:
    print(f"  '{char}' -> {label}")

print(f"\nTotal Vowels: {count_vowels(sentence)}")
print(f"Vowels Found: {extract_vowels(sentence)}")
