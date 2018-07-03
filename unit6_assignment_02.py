__author__ = 'Kalyan'

notes='''
 This is a basic problem involving some file reading and writing. You can put what you have learnt in earlier units
 to use here - functions or nested functions, lists, sorting, generators(optional), comprehensions (optional) etc.

1. Review the relevant lessons if you are blocked.
2. Do not modify the given input files :), modify your code to handle them.
3. Write helper routines where as needed.
4. You can write your own test routines like test_sort_words2(), but comment them out before submitting.
5. Review the files lesson and write elegant code. Python api/features makes it possible to write concise and efficient code.
'''

import unit6utils

def sort_words(source, destination):
    """
    Sort the words in the file specified by source and put them in the
    file specified by destination. The output file should have only lower
    case words, so any upper case words from source must be lowered.

    Ignore empty lines or lines starting with #
    """
    pass
    f=open(source,'r')
    l=f.readlines()
    q=[]
    for i in range(0,len(l)):
        if ('#' in l[i])==False and l[i]!='\n':
            s=""
            s=l[i]
            if i==len(l)-1:
                s+='\n'
            q.append(s.lower())

    q.sort()
    f.close()
    f=open(destination,"w")
    f.write(("".join(q)))
def test_sort_words():
    source = unit6utils.get_input_file("unit6_testinput_02.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_02.txt")
    destination = unit6utils.get_temp_file("unit6_output_02.txt")
    sort_words(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
