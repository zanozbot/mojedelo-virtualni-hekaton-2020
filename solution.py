import math

def get_longest(besede):
    return max(besede, key=len)

# Gets lowest upper limit for bisection based on some heuristics
def max_init_width(words, height, width, text_length):
    return min(height/math.ceil(float(text_length)/width), width/len(get_longest(words)))

def is_valid(pixels, words, height, width, text_length):
    # Ce je povrsina vecja od povrsina pravokotnika lahko takoj vrnemo False
    if (pixels * pixels * text_length > width * height):
        return False
    
    line_length = 0
    current_line = 1
    for word in words:
        if(line_length + len(word) * pixels <= width):
            line_length += len(word)*pixels
        else:
            line_length = len(word)*pixels
            current_line += 1
    return current_line*pixels < height

def get_solution(words, height, width, text_length):
    pixels = max_init_width(words, height, width, text_length)
    high = pixels
    low = 0
    max = 0
    if(is_valid(pixels, words, height, width, text_length)):
        return pixels
    while (pixels > 1):
        if(is_valid(pixels, words, height, width, text_length)):
            if (pixels == max):
                return max
            elif(pixels > max):
                max = pixels
            temp = pixels
            pixels = (high + pixels)/2
            low = temp
        else:
            temp = pixels
            pixels = (low + pixels)/2
            high = temp
    return 0


def init(text, width, height):
    text_length = len(text)
    words = text.split()

    words_with_space = []
    for word in words:
        words_with_space.append(word)
        words_with_space.append(' ')
    words_with_space.pop()

    return get_solution(words_with_space, height, width, text_length)

def test():
    print(init('led display', 20, 6) == 2)
    print(init('led display 2020', 100, 20) == 9)
    print(init('MUST BE ABLE TO DISPLAY', 10, 20) == 1)
    print(init('Can you hack', 55, 25) == 8)
    print(init('display product test', 100, 20) == 8)

test()
