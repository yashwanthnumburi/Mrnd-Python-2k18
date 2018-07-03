__author__ = 'Kalyan'

notes = '''
1. Read instructions for each function carefully.
2. Feel free to create new functions if needed. Give good names!
3. Use builtins and datatypes that we have seen so far.
4. If something about the function spec is not clear, use the corresponding test
   for clarification.
5. Many python builtin functions allow you to pass functions to customize their behavior. This makes it very productive
   to get things done in python.
'''

# Given a list of age, height of various people [(name, years, cms), .... ]. Sort them in decreasing by age and increasing by height.
# NOTE: define a function and pass it to the builtin sort function (key) to get this done, don't do your own sort.
# Do the sort in-place (ie) don't create new lists.
def getKey(item):
    return item[1]
def get(item):
    return item[2]
def custom_sort(input):
    pass
    if input==None :
        return None
    if len(input)==0:
        return input

    input=list(input)
    input=sorted(sorted(input,key=get,reverse=False),key=getKey,reverse=True)
    return input


def single_custom_sort_test(input, expected):
    input=custom_sort(input) # sorts in place

    assert input == expected

def test_custom_sort():
    # boundary cases
    single_custom_sort_test(None, None)
    single_custom_sort_test([], [])

    # no collisions
    single_custom_sort_test(
        [("Ram", 25, 160), ("Shyam", 30, 162), ("Sita", 15, 130)],
        [("Shyam", 30, 162), ("Ram", 25, 160), ("Sita", 15, 130)])

    # collisions in age
    single_custom_sort_test(
        [("Ram", 25, 165), ("Shyam", 30, 162), ("Ravi", 25, 160), ("Gita", 30, 140)],
        [("Gita", 30, 140), ("Shyam", 30, 162), ("Ravi", 25, 160), ("Ram", 25, 165)])

    # collisions in age and height, then initial order is maintained in stable sorts.
    single_custom_sort_test(
        [("Ram", 25, 165), ("Shyam", 30, 140), ("Ravi", 25, 165), ("Gita", 30, 140)],
        [("Shyam", 30, 140), ("Gita", 30, 140), ("Ram", 25, 165), ("Ravi", 25, 165)])


VOWELS = set("aeiou")

# returns the word with the maximum number of vowels, in case of tie return
# the word which occurs first. Use the builtin max function and pass a key func to get this done.
def max_vowels(words):
    pass
    if words==None:
        return None
    if words==[]:
        return None
    i=0
    j=0
    count=0
    max=-1
    index=0
    for i in range(len(words)):
        count=0
        str=words[i]
        for j in range(len(str)):
            if str[j]=='a' or str[j]=='e' or str[j]== 'i' or str[j]=='o' or str[j]=='u':
                count+=1
        if count>max:
            index=i
            max=count
    return words[index]
def test_max_vowels():
    assert None == max_vowels(None)
    assert None == max_vowels([])

    assert "hello" == max_vowels(["hello", "pot", "gut", "sit"])
    assert "engine" == max_vowels(["engine", "hello", "pot", "gut", "sit"])

    assert "automobile" == max_vowels(["engine", "hello", "pot", "gut", "sit", "automobile"])

    assert "fly" == max_vowels(["fly", "pry", "ply"])


