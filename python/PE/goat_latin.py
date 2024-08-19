# Goat Latin is a made-up language based off of English, sort of like Pig Latin. The rules of Goat Latin are as follows: 
# 1. If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add 'ma'. For example, the word 'goat' becomes 'oatgma'. 
# 2. If a word begins with a vowel (a, e, i, o, or u), append 'ma' to the end of the word. For example, the word 'I' becomes 'Ima'. 
# 3. Add one letter "a" to the end of each word per its word index in the sentence, starting with 
# 1. That is, the first word gets "a" added to the end, the second word gets "aa" added to the end, the third word in the sentence gets "aaa" added to the end, 
# and so on. Write a function that, given a string of words making up one sentence, returns that sentence in Goat Latin. 
# For example: string_to_goat_latin('I speak Goat Latin') would return: 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa

def string_to_goat_latin(sentence):
    # Helper function to check if a letter is a vowel
    def is_vowel(char):
        return char.lower() in 'aeiou'
    
    # Split the sentence into words
    words = sentence.split()
    
    # Process each word and apply Goat Latin rules
    goat_latin_words = []
    for index, word in enumerate(words):
        if is_vowel(word[0]):
            # Rule 2: If word starts with a vowel
            goat_word = word + 'ma'
        else:
            # Rule 1: If word starts with a consonant
            goat_word = word[1:] + word[0] + 'ma'
        
        # Rule 3: Add 'a' repeated (index + 1) times
        goat_word += 'a' * (index + 1)
        
        # Add the transformed word to the result list
        goat_latin_words.append(goat_word)
    
    # Join the transformed words into a single sentence
    return ' '.join(goat_latin_words)

# Example usage
sentence = 'I speak Goat Latin'
result = string_to_goat_latin(sentence)
print(result)  # Output: 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'
