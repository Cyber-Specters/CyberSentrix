import math

def Reverse_Mwing_square_algorithm(sq_algo_result):
    result = []
    
    for i, item in enumerate(sq_algo_result):
        if i % 2 == 0:
            num = int(item[:-1])  # Remove the "|" and convert to int ( we know | is decoy )
            original_char = chr(int(math.sqrt(num)))  # Take square root and convert to char
            result.append(original_char)
        else:
            result.append(item)
    
    return ''.join(result)

indices = [
    '6889|',
    'E|',
    '6084|',
    'T|',
    '6724|',
    'I|',
    '7744|',
    '{|',
    '10000|',
    '1|',
    '10000|',
    '_|',
    '14641|',
    '0|',
    '13689|',
    '_|',
    '12996|',
    '3|',
    '2704|',
    'd|',
    '9025|',
    'm|',
    '14641|',
    '_|',
    '11881|',
    '3|',
    '10000|',
    'i|',
    '13689|',
    'm|',
    '3969|']

original_string = Reverse_Mwing_square_algorithm(indices)
print(original_string.replace("|","")+"_th4t_w4s_th3_1nt3nd33d_0ne"+"}") # the second part get from decompile the pyc by brute the version