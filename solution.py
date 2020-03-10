import math
import sys

class Solution:

    def __init__(self, words, width, height, start_new_line_with_space):
        """Inicializacija vhoda za procesiranje"""
        self.text_length = 0

        """Presledek tretiramo na enak nacin kot ostale besede. Zadnja iteracija doda presledek
        prevec, zato ga tudi odstranimo"""
        self.words = []
        for word in words:
            self.words.append(word)
            self.words.append(' ')
            self.text_length += len(word) + 1

        self.words.pop()
        self.text_length -= 1
        self.width = width
        self.height = height
        self.start_new_line_with_space = start_new_line_with_space

    def __get_longest_word(self):
        """Vrne najdaljso besedo iz seznama besed words"""    
        return max(self.words, key=len)

    def __max_width(self):
        """Vrne najmanjso zgornjo mejo sirine(=visine), ki jo lahko zavzame ena crka"""
        return int(min(self.height/math.ceil(float(self.text_length)/self.width), self.width/len(self.__get_longest_word())))

    def __is_valid(self, pixels):
        """Pove, ali je pokritost s podanim stevilom pikslov za eno crko veljavna"""

        """Ce je povrsina enega piksla pomnozeno z dolzino besedila vecja od povrsina 
        pravokotnika lahko takoj vrnemo False"""
        if (pixels * pixels * self.text_length > self.width * self.height):
            return False

        line_length = 0
        current_row = 0

        """Iteriramo skozi besede in preverimo, ce z njimi se lahko zapolnimo vrstice"""
        for word in self.words:
            if(line_length + len(word) * pixels <= self.width):
                line_length += len(word) * pixels
            else:
                line_length = 0
                if (word == ' ' and self.start_new_line_with_space) or word != ' ':
                    line_length = len(word) * pixels
                    
                current_row += 1

        return (current_row + 1) * pixels <= self.height

    def get_solution(self):
        """Najprej pridobimo maksimalno mozno stevilo pikslov za eno crko in postavimo
        pogoje za bisekcijo"""
        pixels = self.__max_width()
        high = pixels
        low = 0
        max = 0

        """Ce je maksimalno stevilo pikslov tudi veljavno, je to tudi resitev"""
        if(self.__is_valid(pixels)):
            return pixels
        
        """Zacnemo z izvajanjem bisekcije nad stevilom pikslov"""
        while (pixels > 1):
            if(self.__is_valid(pixels)):
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

"""Preverimo, ali je v argumentih podano ime datoteke z vhodi"""
try:
    filename = sys.argv[1]
    start_new_line_with_space = sys.argv[2]

    with open(filename) as f:
        for i, line in enumerate(f):
            input = line.split()
            s = Solution(input[2:], int(input[0]), int(input[1]), start_new_line_with_space == 'True')
            print(s.get_solution())

except IndexError:
    print('''Vhodna datoteka ni bila podana.
Delovanje: python solution.py <vhod.txt> <zacni_novo_vrstico_s_presledkom>
<vhod.txt> - Ime datoteke z vhodi
<zacni_novo_vrstico_s_presledkom> - False ali True''')
except IOError:
    print('Vhodna datoteka "{}" ni bila najdena.'.format(filename))
