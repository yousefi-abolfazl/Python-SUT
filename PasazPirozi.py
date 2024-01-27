from collections import Counter, defaultdict

def remove_punctuation(word):
    return ''.join(char for char in word if char.isalnum() or char == '_')

def find_matching_words(n, letters, lst_words):
    matching_words = defaultdict(int)
    letters_counter = Counter(letters)

    for word in lst_words:
        word = remove_punctuation(word)
        word_length = len(word)
        word_counter = Counter(word)

        for char, count in word_counter.items():
            matching_words[word] += min(count, letters_counter[char])

        matching_words[word] = word_length - matching_words[word]

    return [word for word, diff in matching_words.items() if diff <= n]

if __name__ == "__main__":
    n = int(input())
    lst_words = input().replace('.', '').replace('،', '').split()
    letters = list(input())

    result = find_matching_words(n, letters, lst_words)
    
    for word in result:
        print(word)
#clean_code