__author__ = 'Kalyan'

rubber_duck_debugging = '''
 While this does seem like a joke, it WORKS very well in practice :). The ACT OF DESCRIBING your problem out ALOUD
 verbally or in WRITING often clarifies your thinking and takes you to the solution.

READ THESE LINKS:
 http://blog.codinghorror.com/rubber-duck-problem-solving/
 http://en.wikipedia.org/wiki/Rubber_duck_debugging

 I recommend you to work with a friend on this. DESCRIBE YOUR THINKING PROCESS OUT ALOUD to see this
 in action.
'''

# removes duplicates from input list and return a
# sorted list of the unique elements sorted by length
# there are 2 bugs, fix both of them.
def buggy_dedup_sort_by_len(input):
    if input==None:
        return None
    unique = list(set(input))
    unique.sort(key=len)
    return unique


def test_debug_sort_by_len():
    assert ["a", "ab", "abc", "abcd"] == buggy_dedup_sort_by_len(["ab","a","abcd","a", "abc"])
    assert ["a"] == buggy_dedup_sort_by_len(["a","a"])
    assert None == buggy_dedup_sort_by_len(None)



# Identify the failing input from py test output and walk through the code
# loudly to see what is happening.

# Sort the words list in place by number of vowels in the word in descending order
# for e.g. aba -> has 2 letters which are vowels.
def vowel(word):
    count=0
    for i in word:
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            count+=1
    return count


def sort_by_vowel_count(words):
    if(words!=None):
       words.sort(key=vowel,reverse=True)


def single_sort_by_vc_test(input, result):
    if input==None or result==None:
        return True

    sort_by_vowel_count(input)
    assert result == input

def test_sort_by_vowel_count():
    single_sort_by_vc_test(["engine", "ant", "aeiou"], ["aeiou", "engine", "ant"])
    single_sort_by_vc_test(["engine", "ant", "aeroplane", "key", "bcdgcdbcd"], ["aeroplane", "engine", "ant", "key", "bcdgcdbcd"])
    single_sort_by_vc_test([], [])
    single_sort_by_vc_test(None, None)
    single_sort_by_vc_test(["aunt", "engine", "aeiou"], ["aeiou", "engine", "aunt"])
    single_sort_by_vc_test(["aunt", "ENGINE", "aeiou"], ["aeiou", "ENGINE", "aunt"])

