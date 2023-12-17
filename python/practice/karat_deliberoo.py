''' 
As you are reading the book multiple times, you notice that you always get bad endings. You start to suspect there is no way to get to the good endings, so you decide to find out.

Good and bad endings will be separate lists of page numbers, like this:

good_endings = [10, 15, 25, 34]
bad_endings = [21, 30, 40]

Given lists of good endings, bad endings, and a list of the choices along with their options, return a collection of all the reachable good endings, if any.

Examples:

choices1 = [[3, 16, 24]]
find_good_endings(good_endings, bad_endings, choices1)
  Start: 1 -> 2 -> 3(choice) -> 16 -> 17... -> 21(bad ending)
                   |
                   -> 24 -> 25(good ending)
Thus it is possible to reach the good ending at 25 but no others, so we return [25].

choices2 = [[3, 16, 20]]
find_good_endings(good_endings, bad_endings, choices2)
  Start: 1 -> 2 -> 3(choice) -> 16 -> 17... -> 21(bad ending)
                   |
                   > 20 -> 21(bad ending)
No good ending is reachable, so return [].

Additional Inputs:
choices3 = [[3, 2, 19], [20, 21, 34]]
choices4 = []
choices5 = [[9, 16, 26], [14, 16, 13], [27, 29, 28], [28, 15, 34], [29, 30, 38]]
choices6 = [[9, 16, 26], [13, 31, 14], [14, 16, 13], [27, 12, 24], [32, 34, 15]]
choices7 = [[3, 9, 10]]

Complexity Variable:
n = number of pages
(endings and choices are bound by the number of pages)

All Test Cases - snake_case:
find_good_endings(good_endings, bad_endings, choices1) => [25]
find_good_endings(good_endings, bad_endings, choices2) => []
find_good_endings(good_endings, bad_endings, choices3) => [34]
find_good_endings(good_endings, bad_endings, choices4) => [10]
find_good_endings(good_endings, bad_endings, choices5) => [15, 34]
find_good_endings(good_endings, bad_endings, choices6) => [15, 25, 34]
find_good_endings(good_endings, bad_endings, choices7) => [10]

All Test Cases - camelCase:
findGoodEndings(goodEndings, badEndings, choices1) => [25]
findGoodEndings(goodEndings, badEndings, choices2) => []
findGoodEndings(goodEndings, badEndings, choices3) => [34]
findGoodEndings(goodEndings, badEndings, choices4) => [10]
findGoodEndings(goodEndings, badEndings, choices5) => [15, 34]
findGoodEndings(goodEndings, badEndings, choices6) => [15, 25, 34]
findGoodEndings(goodEndings, badEndings, choices7) => [10]
 '''
# import queue
def findEnding(endings,choices1,option):
    r=1
    l=len(choices1)
    vis=[]
    # print(l)
    while True:
        vis.append(r)
        n=-1
        # print(r)
        for i in range(l):
            # print(choices1[i-1][0])
            if r == choices1[i-1][0]:
                # print(choices1[l-1])
                n=choices1[i-1][option]
                # print(n)
        if n == -1:
            r=r+1
        else:
            r=n
        if r in endings:
            return r
        elif r in vis:
            return -1
    return True
# print(findEnding(endings,choices1,1))
# print(findEnding(endings,choices1,2))
# print(findEnding(endings,choices2,1))
# print(findEnding(endings,choices2,2))
# print(findEnding(endings,choices3,1))
# print(findEnding(endings,choices3,2))
# print(findEnding(endings,choices4,1))
# print(findEnding(endings,choices4,2))

good_endings = [10, 15, 25, 34]
bad_endings = [21, 30, 40]

choices1 = [[3, 16, 24]]
choices2 = [[3, 16, 20]]
choices3 = [[3, 2, 19], [20, 21, 34]]
choices4 = []
choices5 = [[9, 16, 26], [14, 16, 13], [27, 29, 28], [28, 15, 34], [29, 30, 38]]
choices6 = [[9, 16, 26], [13, 31, 14], [14, 16, 13], [27, 12, 24], [32, 34, 15]]
choices7 = [[3, 9, 10]]

def findGoodEndings(goodEndings,badEndings,choices1):
    r=1
    l=len(choices1)
    vis=[]
    pages=[]
    out=[]
    pages.append(r)
    while len(pages) != 0:
        r=pages.pop(0)
        if r in goodEndings and r not in out:
            out.append(r)
            continue
        elif r in badEndings:
            continue
        vis.append(r)
        n=-1
        for i in range(l):
            if r == choices1[i-1][0]:
                if choices1[i-1][1] not in vis:
                    pages.append(choices1[i-1][1])
                if choices1[i-1][2] not in vis:
                    pages.append(choices1[i-1][2])
        if n == -1:
            if (r+1) not in vis:
                pages.append(r+1)
    return out

print(findGoodEndings(good_endings, bad_endings, choices1))
print(findGoodEndings(good_endings, bad_endings, choices2)) #=> []
print(findGoodEndings(good_endings, bad_endings, choices3)) #=> [34]
print(findGoodEndings(good_endings, bad_endings, choices4)) #=> [10]
print(findGoodEndings(good_endings, bad_endings, choices5)) #=> [15, 34]
print(findGoodEndings(good_endings, bad_endings, choices6)) #=> [15, 25, 34]
print(findGoodEndings(good_endings, bad_endings, choices7)) #=> [10]