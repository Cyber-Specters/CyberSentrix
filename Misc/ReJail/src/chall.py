#!/usr/bin/env python3

import builtins as repbelajar



BANNER_DEFAULT = """
Need hint? read some docs : https://docs.python.org
▗▄▄▖ ▗▄▄▄▖   ▗▖ ▗▄▖ ▗▄▄▄▖▗▖   
▐▌ ▐▌▐▌      ▐▌▐▌ ▐▌  █  ▐▌   
▐▛▀▚▖▐▛▀▀▘   ▐▌▐▛▀▜▌  █  ▐▌    INTRODUCTION to REPLICAN JAIL
▐▌ ▐▌▐▙▄▄▖▗▄▄▞▘▐▌ ▐▌▗▄█▄▖▐▙▄▄▖
                              
BETA - V1 [ AUTHOR: REPLICAN ] 
Difficulty : Baby
"""
def version_control():
    global version_control_n
    print(BANNER_DEFAULT)
    if "debug" in BANNER_DEFAULT:
        version_control_n = 10000000000000000
    else:
        version_control_n = 12
        
def main():
    
    version_control()
    blacklist = ["exec", "a", "()", "x", "1", "os", "xa", "_", "b"]
    doubled = ['attr', '"', 'getattr', 'name', 'subprocess', 'import', 'globals', '_', 'debug', 'class', 'ord', 'mro', 'os', 'vars', 'import', 'quit', 'breakpoint', 'next', 'locals', 'warning', 'func_globals', 'input', 'init', 'popen', 'fork', 'open', 'map', 'pass', 'chr', '\\', 'setattr', 'open', 'read', 'error', 'file', 'iter', 'locals', 'exec', 'prompt', 'builtins', 'input', 'print', 'enum', 'dir', 'compile', 'banned', "'", 'filter', 'print', 'globals', 'repr', 'main', 'system', 'len', 'blacklisted_chars', 'eval', 'word', 'object', 'class', 'breakpoint', 'char', 'subclasses', 'doc', 'dir', 'base', 'eval', 'exec', 'unicode', 'builtins', 'sys', 'exit']
    
    tripled = ['M', '>', 'u', '[', 'D', 'n', '`', '0', 'x', ',', 'Q', 'a', 'X', '\r', '~', 'P', 'L', '6', 'H', 'd', 'w', '/', 'f', 'b', '@', '2', '\x0c', "'", '1', '9', 'C', '\n', '"', 'B', '\#', '}', 's', 'J', '%', '\x0b', '\t', 'y', 'W', 'j', 'z', 'g', '7', '!', '=', 'o', 'V', '8', '4', 't', '|', 'S', 'v', '\.', ';', '3', 'U', '{', 'Z', 'F', 'm', '*', 'T', '5', '<', '-', '\\', '&', 'G', 'O', '_', 'c', 'R', 'I', 'q', 'A', 'Y', 'K', 'k', '^', 'i', '?', 'E', '+', ']', '$', 'N']
    
    user_input = input("inpur your payload majesty :")
 
    if not user_input.isprintable() or not user_input.isascii():
        print("gaboleh begitu bang hekel")
        exit(1)
    if any(word in user_input for word in blacklist):
        print("gaboleh begitu bang hekel")
        exit(1)
    if any(word in user_input for word in doubled):
        print("gaboleh begitu bang hekel")
        exit(1)
    if any(word in user_input for word in tripled):
        print("gaboleh begitu bang hekel")
        exit(1)
    if len(user_input) > version_control_n:
        print("gaboleh begitu bang hekel")
        exit(1)
    exec(user_input, {"__builtins__": None, user_input.split(":")[-1]: repbelajar})
 

if __name__ == "__main__":
    main()
