def reverse_words_approach1(sentence):
    # Split the sentence into words, removing extra spaces
    words = sentence.strip().split()
    reverse_words = words[::-1]

    return " ".join(reverse_words)

def reverse_words_approach2(sentence):
    result = sentence.split()
    left, right = 0, len(result) - 1

    while left <= right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1

    return " ".join(result)


def main():
    string_to_reverse = ["Hello World",
                        "a   string   with   multiple   spaces",
                        "Case Sensitive Test 1234",
                        "a 1 b 2 c 3 d 4 e 5",
                        "     trailing spaces",
                        "case test interesting an is this"]

    for i in range(len(string_to_reverse)):
        print(i + 1, ".\tOriginal string: '" + "".join(string_to_reverse[i]), "'", sep='')
        Result = reverse_words_approach2(string_to_reverse[i])

        print("\tReversed string: '" + "".join(Result), "'", sep='')
        print("-" * 100)