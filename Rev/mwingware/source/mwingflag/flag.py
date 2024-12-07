import math

def Mwing_star_algorithm(indices=[]):
    result = []
    for i, c in enumerate(indices):
        if i % 2 == 0:
            extra_ordinary = ord(c)*123*i+1
            result.append(extra_ordinary)
        else:
            result.append(str(ord(c))+"|")
    return result

def Reverse_Mwing_star_algorithm(indices=[]):
    result = []
    for i, c in enumerate(indices):
        if i % 2 == 0:
            transformed_value = c 
            original_char = chr((transformed_value - 1) // (123 ** i))
            result.append(original_char)
        else:
            result.append(chr(c))
    
    return ''.join(result)

def Mwing_sum_algorithm(numbers=[]):
    even_sum = sum(numbers[i] for i in range(0, len(numbers), 2))
    odd_sum = sum(numbers[i] for i in range(1, len(numbers), 2))
    print(f"Final Algorithm ( SUPER EFFICIENT, ENCRYPT ALL LETTER WITH ONLY RESULT JUST SUPER SHORT): {even_sum}|Key: {odd_sum}")


def Mwing_reverse_algorithm(elements=[]):
    for el in reversed(elements):
        print(el, end="!")

def Mwing_square_algorithm(numbers=[]):
    result = []
    for i, num in enumerate(numbers):
        if i % 2 == 0:
            result.append(str(ord(num)**2) + "|")
        else:
            result.append(str(num) + "|")
    return result



def Mwing_char_sum_algorithm(chars=[]):
    ascii_sum = sum(ord(c) for i, c in enumerate(chars) if i % 2 == 0)
    for i, c in enumerate(chars):
        if i % 2 == 0:
            print(ascii_sum, end="|")
        else:
            print(c, end="|")



