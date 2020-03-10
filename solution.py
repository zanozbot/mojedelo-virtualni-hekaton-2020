import math
import sys
import re

def get_longest_word(words):
    """Vrne najdaljso besedo iz seznama besed words"""    
    return max(words, key=len)

def max_width(words, width, height, text_length):
    """Vrne najmanjso zgornjo mejo sirine(=visine), ki jo lahko zavzame ena crka"""
    return int(min(height/math.ceil(float(text_length)/width), width/len(get_longest_word(words))))

def is_valid(pixels, words, width, height, text_length):
    """Pove, ali je pokritost s podanim stevilom pikslov za eno crko veljavna"""

    """Ce je povrsina enega piksla pomnozeno z dolzino besedila vecja od povrsina 
    pravokotnika lahko takoj vrnemo False"""
    if (pixels * pixels * text_length > width * height):
        return False

    line_length = 0
    current_row = 0

    """Iteriramo skozi besede in preverimo, ce z njimi se lahko zapolnimo vrstice"""
    for word in words:
        if(line_length + len(word) * pixels <= width):
            line_length += len(word) * pixels
        else:
            line_length = len(word) * pixels
            current_row += 1

    return (current_row + 1) * pixels <= height

def get_solution(words, width, height, text_length):
    """Najprej pridobimo maksimalno mozno stevilo pikslov za eno crko in postavimo
    pogoje za bisekcijo"""
    pixels = max_width(words, width, height, text_length)
    high = pixels
    low = 0
    max = 0

    """Ce je maksimalno stevilo pikslov tudi veljavno, je to tudi resitev"""
    if(is_valid(pixels, words, width, height, text_length)):
        return pixels
    
    """Zacnemo z izvajanjem bisekcije nad stevilom pikslov"""
    while (pixels > 1):
        if(is_valid(pixels, words, width, height, text_length)):
            if (pixels == max):
                """To pomeni, da smo v prejsnji iteraciji prisli do enakega rezultata in lahko vrnemo max kot resitev"""
                return max
            elif(pixels > max):
                """Nasli smo vecje stevilo pikslov za eno crko"""
                max = pixels
                
            temp = pixels
            pixels = (high + pixels)/2
            low = temp
        else:
            temp = pixels
            pixels = (low + pixels)/2
            high = temp
    
    """Nismo nasli resitve"""
    return 0


def solve_input(words, width, height):
    """Priprava vhoda za procesiranje"""
    text_length = 0

    """Presledek tretiramo na enak nacin kot ostale besede. Zadnja iteracija doda presledek
    prevec, zato ga tudi odstranimo"""
    words_with_space = []
    for word in words:
        words_with_space.append(word)
        words_with_space.append(' ')
        text_length += len(word) + 1
    
    words_with_space.pop()
    text_length -= 1

    return get_solution(words_with_space, width, height, text_length)

"""Preverimo, ali je v argumentih podano ime datoteke z vhodi"""
try:
    filename = sys.argv[1]
    
    with open(filename) as f:
        for i, line in enumerate(f):
            input = line.split()
            solution = solve_input(input[2:], int(input[0]), int(input[1]))
            print(solution)

except IndexError:
    print('Program zagnan brez vhodne datoteke.\nDelovanje: python solution.py <vhod.txt>')
    sys.exit()