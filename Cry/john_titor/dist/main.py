from Crypto.Util.number import getPrime, inverse, long_to_bytes
import random
import time

soal = {
    "Who is John?":"John Titor is an alias used by a person that claims to be a time traveler from the year 2036. He appears at different times depending on the Attractor Field, appearing in the year 2010 in the Alpha Attractor Field, and the year 2000 in the Beta Attractor Field.",
    "Why John want time travel?":"came to meet her father in 2010. Her mission is to go back to the year 1975 and recover an IBN 5100 to stop SERN, but she took a break by the year 2010 to search for her father",
    "What's name of this Event?":"Cyber Sentrix is a competitive capture the flag event organized by Cyber Specters",
    "Who is Author for this challenge?":"raphael, is a one of genius man in the world who hack everything he want. He is a man who craft and collect 0day for fun"
}

def cook():
    return random.getrandbits(32) << 512

def generator(x):
    p = getPrime(512)  
    q = getPrime(512)  
    e = 65537  
    phi_n = (p - 1) * (q - 1)  
    n = p * q  
    n2 = (p - x) * (q - x) 
    d = inverse(e, phi_n)  
    return n, e, n2, d

def menu():
    return """
##########################
# 1.Leak The Random      #
# 2.Verify The Signature #
##########################
"""

def main():
    signature = b'John_Titor_Administrator_Time_Machine'  
    while True:
        next_random = cook() 
        n, e, n2, d = generator(next_random)  
        key, value = random.choice(list(soal.items()))
        end = 15
        s = time.time()
        soalan = input(f"{key}")
        ended = time.time() - s
        if (ended< end) and (soalan == value):
            print(f"""
{menu()}
n = {n}
e = {e}
n2 = {n2}
""")
            us = input("choose> ")
            if us == '1':
                print(next_random)
            elif us == '2':
                verify_sig = input("verify#> ")
                verify_sig = pow(bytes_to_long(signature), 65537, next_random)
                if verify_sig == pow(bytes_to_long(signature),65537,next_random):
                    print(f"Confirmed as John Titor. Here is your Key: {pow(bytes_to_long(open('flag.txt').read().encode()),e,n)}")
                else:
                    print("Signature verification failed.")
        else:
            print("Time Limit or the Answer is Incorrect")
if __name__ == "__main__":
    main()

