def count_vowels(kata):
    vowel = "aiueo"
    count = 0
    for i in kata:
        if i in vowel: count += 1
    print(count)
    
count_vowels('programmer')
