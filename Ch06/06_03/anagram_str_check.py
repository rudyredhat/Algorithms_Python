import sys
import random


def angramStrCheck1(s1, s2):
    return False


def angramStrCheck2(s1, s2):
    # need the sorted array
    tmp1 = ''.join(sorted(s1))
    tmp2 = ''.join(sorted(s2))
    for i in range(len(tmp1)):
        if tmp1[i] != tmp2[i]:
            return False
    return True


def angramStrCheck3(s1, s2):
    # only for lowercase char a to z
    count = [0]*26
    for i in range(len(s1)):
        # we need to map each char of the string
        # so we need to get the internal code value of char we use = ord
        tmp = ord(s1[i]) - ord('a')
        # now go to the count arr and increment the freq
        count[tmp] += 1
    # now for the second str we need to decrement the char
    for i in range(len(s2)):
        tmp = ord(s2[i]) - ord('a')
        # now go to the count arr and decrement the freq
        if count[tmp] <= 0:
            return False
        count[tmp] -= 1


def randomString(n):
    # initially we do not know the random string , so we have taken as empty
    res = ''
    for i in range(n):
        # take the random range from 0 to 25
        # but we want char out of that number
        # so we need to add ord(a) to each random number, 97 + rand number
        # then we need to finally cast to that to char
        tmp = chr(ord('a') + random.randint(0, 25))
        # append the temp value
        res += tmp
    return res


def main():
    # pycharm - run - edit configuration - set parameter - apply - ok
    n = int(sys.argv[1])
    s1 = randomString(n)
    s2 = randomString(n)
    print(s1)
    print(s2)
    print(angramStrCheck2(s1, s2))
    print(angramStrCheck3(s1, s2))


if __name__ == '__main__':
    main()