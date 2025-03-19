def get_sentence_input():
    return input("Enter a sentence: ")

def count_words(sentence):
    words = sentence.split()
    return len(words)

def main():
    sentence = get_sentence_input()
    word_count = count_words(sentence)
    print(f"The sentence has {word_count} words.")

main()
