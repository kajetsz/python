#Exercises - class 1

def ex1(num):

    if num > 9:
        return 'Too many cookies'
    else:
        return 'Number of cookies: ' + str(num) 

print(ex1(9))

def ex2(input):
    return input[2:-2]

print(ex2('noyesno'))

def ex3(a, b):
    c = a[0:2] + b[2:]
    d = b[0:2] + a[2:]
    return c, d

print(ex3('aasiemano', 'bbcotam'))

def ex4(stringList):
    result = 0
    for s in stringList:
        if len(s) > 2 and s[0] == s[len(s) - 1]:
            result += 1
    return result

testList = ['alfa', 'beta', 'omega', 'epsilon', 'agawa', 'baobab', 'ad']

print(ex4(testList))


testList = ['alfa', 'beta', 'omega', 'epsilon', 'agawa', 'baobab', 'ad']

def ex5(stringList, x):
    startingWithX = []
    for s in stringList:
        if s[0] == x:
            startingWithX.append(s)
            stringList.remove(s)
    return sorted(startingWithX) + sorted(stringList)

print(ex5(testList, 'b'))

testNumbers = [1,1,2,2,3,1,2,3,3,3,3,3]

def ex6(numbers):
    results = []
    for n in range(len(numbers)):
        if numbers[n] != numbers[n-1]:
            results.append(numbers[n])
    return results

print(ex6(testNumbers))

def ex7():
    
    result = {}
    f = open('lista.txt', 'r')
    for line in f:
        key, value = line.split()
        result[key] = value
    f.close()
    return result

print(ex7())

def ex8():
    result = {}
    wordcount = 0
    f = open('test8.txt', 'r')
    for line in f:
        words = line.split()
        for w in words:
            if w in result.keys():
                result[w] = result[w] + 1
            else:
                result[w] = 1
    f.close()
    return result

print(ex8())
