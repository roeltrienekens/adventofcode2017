inputfile = "in4a.txt"
# testfile = ""
# test2file = ""

import unittest



def isValid(passphrase):
    dict = {}
    for word in passphrase.split(" "):
#        print(word)
        if dict.has_key(word):
            return False
        else:
            dict[word] = 1
    return True

def isValid2(passphrase):
    dict = {}
#    print(passphrase)
    for word in passphrase.split(" "):
#        print(''.join(sorted(word)))
        if dict.has_key(''.join(sorted(word))):
            return False
        else:
            dict[''.join(sorted(word))] = 1
    return True


# Testcases

class MyTest(unittest.TestCase):
    def test(self):

        self.assertTrue(isValid("aa bb cc dd ee"))
        self.assertFalse(isValid("aa bb cc dd aa"))
        self.assertTrue(isValid("aa bb cc dd aaa"))
        self.assertFalse(isValid("bneh ylltsc vhryov lsd hmruxy ebnh pdln vdprrky lsd lsd"))

        self.assertTrue(isValid2("abcde fghij"))
        self.assertFalse(isValid2("abcde xyz ecdab"))
        self.assertTrue(isValid2("a ab abc abd abf abj"))
        self.assertTrue(isValid2("iiii oiii ooii oooi oooo"))
        self.assertFalse(isValid2("oiii ioii iioi iiio"))



if __name__ == '__main__':

    f = open(inputfile, 'r')
    ans = 0
    ans2 = 0
    for line in f.read().split("\n"):
        if line != "\n":
#            print(isValid(line))
            if isValid(line):
                ans += 1
            if isValid2(line):
                ans2 += 1
#            print(ans)
    print("There are " + str(ans - 1) + " valid passphrases.")
    print("There are " + str(ans2 - 1) + " valid passphrases using the new policy.")


    unittest.main()
