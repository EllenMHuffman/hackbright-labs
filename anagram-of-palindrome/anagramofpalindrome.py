def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    count_of_letters = {}

    for letter in word:
        count_of_letters[letter] = count_of_letters.get(letter, 0) + 1

    odd_letter = 0

    for letter, count in count_of_letters.iteritems():
        if count % 2 != 0:
            odd_letter += 1
        if odd_letter > 1:
            return False

    return True
