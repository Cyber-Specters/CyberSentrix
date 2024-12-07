from mwingflag.flag import Mwing_star_algorithm, Mwing_sum_algorithm,Mwing_square_algorithm
import random

_1s_34sy_f0r_b3g1n3r_pyth0n = False
_th4t_w4s_th3_1nt3nd33d_0ne = ['6889|', 'E|', '6084|', 'T|', '6724|', 'I|', '7744|', '{|', '10000|', '1|', '10000|', '_|', '14641|', '0|', '13689|', '_|', '12996|', '3|', '2704|', 'd|', '9025|', 'm|', '14641|', '_|', '11881|', '3|', '10000|', 'i|', '13689|', 'm|', '3969|']
_r34lly_1gn0r3_m3  = False
_h0w_did_u_4 = False
_kecoh_jir = False
_wtf_i_do = False

def main():
    if _1s_34sy_f0r_b3g1n3r_pyth0n:
        print("hi guys, assembly reader are you") 

    if _r34lly_1gn0r3_m3:
        print("hi guys, assembly reader are you") 
    elif _h0w_did_u_4:
        print("hi guys, assembly reader are you") 
    elif _kecoh_jir:
        print("hi guys, assembly reader are you") 
    elif _wtf_i_do:
        print("hi guys, assembly reader are you") 
    i_chr = []
    
    print("here is your flag, thank you for playing my rev althrough my rev skill was newbie :), so i decided to encrypte it. go dec it reverse it. ( sure gpt will help u, maybe XD )")
    for f in _th4t_w4s_th3_1nt3nd33d_0ne:
        print(f.replace("|",""),end="")
    print()
    char_per_char = input("INPUT HERE: ")
    for c in char_per_char:
        i_chr.append(c)
    
    lt = Mwing_star_algorithm(indices=i_chr)
    print("mwing star algorithm : "+"".join(str(lt)))
    sqAlgo = Mwing_square_algorithm(i_chr)
    res = []
    for i in sqAlgo:
        unpredictable_flag_encrypted = random.randint(0, 10)
        for i in range(0, unpredictable_flag_encrypted):
            res.append(str(random.randint(0, 10)) + "_"+ str(random.randint(0, 10)) + str(i) + str(random.randint(0, 10))+"|")
    print("mwing star revised algorithm : "+"".join(res), end="\n")
    cx_i = []
    for cx in i_chr:
        cx_i.append(ord(cx))
    Mwing_sum_algorithm(cx_i)
    
if __name__ == "__main__":
    main()
    
