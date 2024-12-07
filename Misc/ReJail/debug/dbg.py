# import string

# # Use string.printable for printable characters
# filtered_chars = [c for c in string.printable if c not in {'h', 'e', 'l', 'p'}]

# print(filtered_chars)
import random

tripled = [ 'unicode', 'name', 'setattr', 'import', 'open', 'enum',
    'char', 'quit', 'getattr', 'locals', 'globals', 'len',
    'exit', 'exec', 'blacklisted_words', 'print', 'builtins',
    'eval', 'blacklisted_chars', 'repr', 'main', 'subclasses', 'file',
    'class', 'mro', 'input', 'compile', 'init', 'doc', 'fork',
    'popen', 'read', 'map', 'dir', 'error', 'warning',
    'func_globals', 'vars', 'filter', 'debug', 'object', 'next',
    'word', 'base', 'prompt', 'breakpoint', 'class', 'pass',
    'chr', 'ord', 'iter', 'banned','breakpoint', 'print', 'input', 'eval', 'exec', 'open', 'import', 'globals', 'locals', 'builtins', 'dir', 'os', 'sys', 'attr', '_', '"', "'", 'system', 'subprocess', '\\']
# Shuffle the list to make it unordered
random.shuffle(tripled)

# Print the shuffled list
print(tripled)
