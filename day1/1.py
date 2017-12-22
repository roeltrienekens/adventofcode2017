# noinspection SpellCheckingInspection
inputfile = "input.txt"

puzzle_input = []

for line in open(inputfile, 'r'):
    # noinspection PyRedeclaration
    puzzle_input = list(line.strip())

captchaSum = 0
LENGTH = len(puzzle_input)


def captcha(offset):
    captcha_sum = 0
    for i in range(0, LENGTH):
        if puzzle_input[i] == puzzle_input[(i + offset) % LENGTH]:
            captcha_sum += int(puzzle_input[i])
    return captcha_sum


print("The Captcha for offset is 1 (next character) is: " + str(captcha(1)))
print("The Captcha for offset is 1/2 the length is: " + str(captcha(LENGTH / 2)))
