'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):
    #if "word" is empty, return the default count of 0
    if word == '':
        return count
    #if the words length is less than or equal to 2 AND the 1st and 2nd element are "th"
    if len(word) >= 2 and (word[0] + word[1]) == 'th':
        #then return 0, plus this function again, now taking in the word from the 3rd element up, add 1 to count
        return 0 + count_th(word[2:], count + 1)
    #else return this function, with the word from the first element up, and the count
    else:
        return count_th(word[1:], count) 
