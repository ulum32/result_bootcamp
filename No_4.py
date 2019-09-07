def groupNumber(number):
    num = []
    no = 1
    for i in number:
        if i.isdigit(): 
            if no <= 3: num.append(i) ;  no += 1
            else : num.append('-') ; no = 1

    if num[len(num)-2] == '-':
        char = num[len(num)-3]
        num[len(num)-3] = '-'
        num[len(num)-2] = char
    
    for c in num:
        print(c,end="")
    
groupNumber("993141 -1 1323 1-42.923")
