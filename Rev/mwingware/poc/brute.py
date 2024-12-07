# dapetin dari https://github.com/python/cpython/blob/main/Include/internal/pycore_magic_number.h
magic_number = """
    Python 3.0a4: 3111 (WITH_CLEANUP optimization).
    Python 3.0b1: 3131 (lexical exception stacking, including POP_EXCEPT
                          #3021)
    Python 3.1a1: 3141 (optimize list, set and dict comprehensions:
                        change LIST_APPEND and SET_ADD, add MAP_ADD #2183)
    Python 3.1a1: 3151 (optimize conditional branches:
                        introduce POP_JUMP_IF_FALSE and POP_JUMP_IF_TRUE
                          #4715)
    Python 3.2a1 3160 (add SETUP_WITH #6101)
    Python 3.2a2 3170 (add DUP_TOP_TWO, remove DUP_TOPX and ROT_FOUR #9225)
    Python 3.2a3 3180 (add DELETE_DEREF #4617)
    Python 3.3a1  3190 (__class__ super closure changed)
    Python 3.3a1  3200 (PEP 3155 __qualname__ added #13448)
    Python 3.3a1  3210 (added size modulo 2**32 to the pyc header #13645)
    Python 3.3a2  3220 (changed PEP 380 implementation #14230)
    Python 3.3a4  3230 (revert changes to implicit __class__ closure #14857)
    Python 3.4a1  3250 (evaluate positional default arguments before
                       keyword-only defaults #16967)
    Python 3.4a1  3260 (add LOAD_CLASSDEREF; allow locals of class to override
                       free vars #17853)
    Python 3.4a1  3270 (various tweaks to the __class__ closure #12370)
    Python 3.4a1  3280 (remove implicit class argument)
    Python 3.4a4  3290 (changes to __qualname__ computation #19301)
    Python 3.4a4  3300 (more changes to __qualname__ computation #19301)
    Python 3.4rc2 3310 (alter __qualname__ computation #20625)
    Python 3.5a1  3320 (PEP 465: Matrix multiplication operator #21176)
    Python 3.5b1  3330 (PEP 448: Additional Unpacking Generalizations #2292)
    Python 3.5b2  3340 (fix dictionary display evaluation order #11205)
    Python 3.5b3  3350 (add GET_YIELD_FROM_ITER opcode #24400)
    Python 3.5.2  3351 (fix BUILD_MAP_UNPACK_WITH_CALL opcode #27286)
    Python 3.6a0  3360 (add FORMAT_VALUE opcode #25483)
    Python 3.6a1  3361 (lineno delta of code.co_lnotab becomes signed #26107)
    Python 3.6a2  3370 (16 bit wordcode #26647)
    Python 3.6a2  3371 (add BUILD_CONST_KEY_MAP opcode #27140)
    Python 3.6a2  3372 (MAKE_FUNCTION simplification, remove MAKE_CLOSURE
                        #27095)
    Python 3.6b1  3373 (add BUILD_STRING opcode #27078)
    Python 3.6b1  3375 (add SETUP_ANNOTATIONS and STORE_ANNOTATION opcodes
                        #27985)
    Python 3.6b1  3376 (simplify CALL_FUNCTIONs & BUILD_MAP_UNPACK_WITH_CALL
                          #27213)
    Python 3.6b1  3377 (set __class__ cell from type.__new__ #23722)
    Python 3.6b2  3378 (add BUILD_TUPLE_UNPACK_WITH_CALL #28257)
    Python 3.6rc1 3379 (more thorough __class__ validation #23722)
    Python 3.7a1  3390 (add LOAD_METHOD and CALL_METHOD opcodes #26110)
    Python 3.7a2  3391 (update GET_AITER #31709)
    Python 3.7a4  3392 (PEP 552: Deterministic pycs #31650)
    Python 3.7b1  3393 (remove STORE_ANNOTATION opcode #32550)
    Python 3.7b5  3394 (restored docstring as the first stmt in the body;
                        this might affected the first line number #32911)
    Python 3.8a1  3400 (move frame block handling to compiler #17611)
    Python 3.8a1  3401 (add END_ASYNC_FOR #33041)
    Python 3.8a1  3410 (PEP570 Python Positional-Only Parameters #36540)
    Python 3.8b2  3411 (Reverse evaluation order of key: value in dict
                        comprehensions #35224)
    Python 3.8b2  3412 (Swap the position of positional args and positional
                        only args in ast.arguments #37593)
    Python 3.8b4  3413 (Fix "break" and "continue" in "finally" #37830)
    Python 3.9a0  3420 (add LOAD_ASSERTION_ERROR #34880)
    Python 3.9a0  3421 (simplified bytecode for with blocks #32949)
    Python 3.9a0  3422 (remove BEGIN_FINALLY, END_FINALLY, CALL_FINALLY, POP_FINALLY bytecodes #33387)
    Python 3.9a2  3423 (add IS_OP, CONTAINS_OP and JUMP_IF_NOT_EXC_MATCH bytecodes #39156)
    Python 3.9a2  3424 (simplify bytecodes for *value unpacking)
    Python 3.9a2  3425 (simplify bytecodes for **value unpacking)
    Python 3.10a1 3430 (Make 'annotations' future by default)
    Python 3.10a1 3431 (New line number table format -- PEP 626)
    Python 3.10a2 3432 (Function annotation for MAKE_FUNCTION is changed from dict to tuple bpo-42202)
    Python 3.10a2 3433 (RERAISE restores f_lasti if oparg != 0)
    Python 3.10a6 3434 (PEP 634: Structural Pattern Matching)
    Python 3.10a7 3435 Use instruction offsets (as opposed to byte offsets).
    Python 3.10b1 3436 (Add GEN_START bytecode #43683)
    Python 3.10b1 3437 (Undo making 'annotations' future by default - We like to dance among core devs!)
    Python 3.10b1 3438 Safer line number table handling.
    Python 3.10b1 3439 (Add ROT_N)
    Python 3.11a1 3450 Use exception table for unwinding ("zero cost" exception handling)
    Python 3.11a1 3451 (Add CALL_METHOD_KW)
    Python 3.11a1 3452 (drop nlocals from marshaled code objects)
    Python 3.11a1 3453 (add co_fastlocalnames and co_fastlocalkinds)
    Python 3.11a1 3454 (compute cell offsets relative to locals bpo-43693)
    Python 3.11a1 3455 (add MAKE_CELL bpo-43693)
    Python 3.11a1 3456 (interleave cell args bpo-43693)
    Python 3.11a1 3457 (Change localsplus to a bytes object bpo-43693)
    Python 3.11a1 3458 (imported objects now don't use LOAD_METHOD/CALL_METHOD)
    Python 3.11a1 3459 (PEP 657: add end line numbers and column offsets for instructions)
    Python 3.11a1 3460 (Add co_qualname field to PyCodeObject bpo-44530)
    Python 3.11a1 3461 (JUMP_ABSOLUTE must jump backwards)
    Python 3.11a2 3462 (bpo-44511: remove COPY_DICT_WITHOUT_KEYS, change
                        MATCH_CLASS and MATCH_KEYS, and add COPY)
    Python 3.11a3 3463 (bpo-45711: JUMP_IF_NOT_EXC_MATCH no longer pops the
                        active exception)
    Python 3.11a3 3464 (bpo-45636: Merge numeric BINARY_*INPLACE_* into
                        BINARY_OP)
    Python 3.11a3 3465 (Add COPY_FREE_VARS opcode)
    Python 3.11a4 3466 (bpo-45292: PEP-654 except*)
    Python 3.11a4 3467 (Change CALL_xxx opcodes)
    Python 3.11a4 3468 (Add SEND opcode)
    Python 3.11a4 3469 (bpo-45711: remove type, traceback from exc_info)
    Python 3.11a4 3470 (bpo-46221: PREP_RERAISE_STAR no longer pushes lasti)
    Python 3.11a4 3471 (bpo-46202: remove pop POP_EXCEPT_AND_RERAISE)
    Python 3.11a4 3472 (bpo-46009: replace GEN_START with POP_TOP)
    Python 3.11a4 3473 (Add POP_JUMP_IF_NOT_NONE/POP_JUMP_IF_NONE opcodes)
    Python 3.11a4 3474 (Add RESUME opcode)
    Python 3.11a5 3475 (Add RETURN_GENERATOR opcode)
    Python 3.11a5 3476 (Add ASYNC_GEN_WRAP opcode)
    Python 3.11a5 3477 (Replace DUP_TOP/DUP_TOP_TWO with COPY and
                        ROT_TWO/ROT_THREE/ROT_FOUR/ROT_N with SWAP)
    Python 3.11a5 3478 (New CALL opcodes)
    Python 3.11a5 3479 (Add PUSH_NULL opcode)
    Python 3.11a5 3480 (New CALL opcodes, second iteration)
    Python 3.11a5 3481 (Use inline cache for BINARY_OP)
    Python 3.11a5 3482 (Use inline caching for UNPACK_SEQUENCE and LOAD_GLOBAL)
    Python 3.11a5 3483 (Use inline caching for COMPARE_OP and BINARY_SUBSCR)
    Python 3.11a5 3484 (Use inline caching for LOAD_ATTR, LOAD_METHOD, and
                        STORE_ATTR)
    Python 3.11a5 3485 (Add an oparg to GET_AWAITABLE)
    Python 3.11a6 3486 (Use inline caching for PRECALL and CALL)
    Python 3.11a6 3487 (Remove the adaptive "oparg counter" mechanism)
    Python 3.11a6 3488 (LOAD_GLOBAL can push additional NULL)
    Python 3.11a6 3489 (Add JUMP_BACKWARD, remove JUMP_ABSOLUTE)
    Python 3.11a6 3490 (remove JUMP_IF_NOT_EXC_MATCH, add CHECK_EXC_MATCH)
    Python 3.11a6 3491 (remove JUMP_IF_NOT_EG_MATCH, add CHECK_EG_MATCH,
                        add JUMP_BACKWARD_NO_INTERRUPT, make JUMP_NO_INTERRUPT virtual)
    Python 3.11a7 3492 (make POP_JUMP_IF_NONE/NOT_NONE/TRUE/FALSE relative)
    Python 3.11a7 3493 (Make JUMP_IF_TRUE_OR_POP/JUMP_IF_FALSE_OR_POP relative)
    Python 3.11a7 3494 (New location info table)
    Python 3.11b4 3495 (Set line number of module's RESUME instr to 0 per PEP 626)
    Python 3.12a1 3500 (Remove PRECALL opcode)
    Python 3.12a1 3501 (YIELD_VALUE oparg == stack_depth)
    Python 3.12a1 3502 (LOAD_FAST_CHECK, no NULL-check in LOAD_FAST)
    Python 3.12a1 3503 (Shrink LOAD_METHOD cache)
    Python 3.12a1 3504 (Merge LOAD_METHOD back into LOAD_ATTR)
    Python 3.12a1 3505 (Specialization/Cache for FOR_ITER)
    Python 3.12a1 3506 (Add BINARY_SLICE and STORE_SLICE instructions)
    Python 3.12a1 3507 (Set lineno of module's RESUME to 0)
    Python 3.12a1 3508 (Add CLEANUP_THROW)
    Python 3.12a1 3509 (Conditional jumps only jump forward)
    Python 3.12a2 3510 (FOR_ITER leaves iterator on the stack)
    Python 3.12a2 3511 (Add STOPITERATION_ERROR instruction)
    Python 3.12a2 3512 (Remove all unused consts from code objects)
    Python 3.12a4 3513 (Add CALL_INTRINSIC_1 instruction, removed STOPITERATION_ERROR, PRINT_EXPR, IMPORT_STAR)
    Python 3.12a4 3514 (Remove ASYNC_GEN_WRAP, LIST_TO_TUPLE, and UNARY_POSITIVE)
    Python 3.12a5 3515 (Embed jump mask in COMPARE_OP oparg)
    Python 3.12a5 3516 (Add COMPARE_AND_BRANCH instruction)
    Python 3.12a5 3517 (Change YIELD_VALUE oparg to exception block depth)
    Python 3.12a6 3518 (Add RETURN_CONST instruction)
    Python 3.12a6 3519 (Modify SEND instruction)
    Python 3.12a6 3520 (Remove PREP_RERAISE_STAR, add CALL_INTRINSIC_2)
    Python 3.12a7 3521 (Shrink the LOAD_GLOBAL caches)
    Python 3.12a7 3522 (Removed JUMP_IF_FALSE_OR_POP/JUMP_IF_TRUE_OR_POP)
    Python 3.12a7 3523 (Convert COMPARE_AND_BRANCH back to COMPARE_OP)
    Python 3.12a7 3524 (Shrink the BINARY_SUBSCR caches)
    Python 3.12b1 3525 (Shrink the CALL caches)
    Python 3.12b1 3526 (Add instrumentation support)
    Python 3.12b1 3527 (Add LOAD_SUPER_ATTR)
    Python 3.12b1 3528 (Add LOAD_SUPER_ATTR_METHOD specialization)
    Python 3.12b1 3529 (Inline list/dict/set comprehensions)
    Python 3.12b1 3530 (Shrink the LOAD_SUPER_ATTR caches)
    Python 3.12b1 3531 (Add PEP 695 changes)
    Python 3.13a1 3550 (Plugin optimizer support)
    Python 3.13a1 3551 (Compact superinstructions)
    Python 3.13a1 3552 (Remove LOAD_FAST__LOAD_CONST and LOAD_CONST__LOAD_FAST)
    Python 3.13a1 3553 (Add SET_FUNCTION_ATTRIBUTE)
    Python 3.13a1 3554 (more efficient bytecodes for f-strings)
    Python 3.13a1 3555 (generate specialized opcodes metadata from bytecodes.c)
    Python 3.13a1 3556 (Convert LOAD_CLOSURE to a pseudo-op)
    Python 3.13a1 3557 (Make the conversion to boolean in jumps explicit)
    Python 3.13a1 3558 (Reorder the stack items for CALL)
    Python 3.13a1 3559 (Generate opcode IDs from bytecodes.c)
    Python 3.13a1 3560 (Add RESUME_CHECK instruction)
    Python 3.13a1 3561 (Add cache entry to branch instructions)
    Python 3.13a1 3562 (Assign opcode IDs for internal ops in separate range)
    Python 3.13a1 3563 (Add CALL_KW and remove KW_NAMES)
    Python 3.13a1 3564 (Removed oparg from YIELD_VALUE, changed oparg values of RESUME)
    Python 3.13a1 3565 (Oparg of YIELD_VALUE indicates whether it is in a yield-from)
    Python 3.13a1 3566 (Emit JUMP_NO_INTERRUPT instead of JUMP for non-loop no-lineno cases)
    Python 3.13a1 3567 (Reimplement line number propagation by the compiler)
    Python 3.13a1 3568 (Change semantics of END_FOR)
    Python 3.13a5 3569 (Specialize CONTAINS_OP)
    Python 3.13a6 3570 (Add __firstlineno__ class attribute)
    Python 3.13b1 3571 (Fix miscompilation of private names in generic classes)
    Python 3.14a1 3600 (Add LOAD_COMMON_CONSTANT)
    Python 3.14a1 3601 (Fix miscompilation of private names in generic classes)
    Python 3.14a1 3602 (Add LOAD_SPECIAL. Remove BEFORE_WITH and BEFORE_ASYNC_WITH)
    Python 3.14a1 3603 (Remove BUILD_CONST_KEY_MAP)
    Python 3.14a1 3604 (Do not duplicate test at end of while statements)
    Python 3.14a1 3605 (Move ENTER_EXECUTOR to opcode 255)
    Python 3.14a1 3606 (Specialize CALL_KW)
    Python 3.14a1 3607 (Add pseudo instructions JUMP_IF_TRUE/FALSE)
    Python 3.14a1 3608 (Add support for slices)
    Python 3.14a2 3609 (Add LOAD_SMALL_INT and LOAD_CONST_IMMORTAL instructions, remove RETURN_CONST)
"""

import re
import subprocess

list_magic = {}
for i,mn in enumerate(magic_number.splitlines()):
    find_version_and_magicnum = re.findall(r'Python (.*?) (.*?) ', mn)
    if len(find_version_and_magicnum) == 1 :
        if find_version_and_magicnum[0][1] != "":
            list_magic[f'{i}_Python{find_version_and_magicnum[0][0]}'] = find_version_and_magicnum[0][1]
    # in the doc kadang ada spasi 2 ngeslein bet
    find_version_and_magicnum = re.findall(r'Python (.*?)  (.*?) ', mn)
    if len(find_version_and_magicnum) == 1 :
        if find_version_and_magicnum[0][1] != "":
            list_magic[f'{i}_Python{find_version_and_magicnum[0][0]}'] = find_version_and_magicnum[0][1]
            
def int_to_hex_2s_complement(value: int) -> str:
    original_string = format(value, '04X')
    new_string = original_string[3] + original_string[2] + original_string[0] + original_string[1]
    return new_string
 
import os

def modify_pyc_header(input_file, output_file, new_header):
    new_header_bytes = bytes.fromhex(new_header)
    
    with open(input_file, 'rb') as infile:
        content = infile.read()
    
    modified_content = new_header_bytes + content[2:]
    
    with open(output_file, 'wb') as outfile:
        outfile.write(modified_content)
    
    try:
        result = subprocess.run(['pycdc', output_file], capture_output=True, text=True)
        if 'Source Generated with Decompyle' in result.stdout:
            print(f'found at {new_header} : {output_file}')
            open(f'results/decompiled_{new_header}.txt', 'w').write(result.stdout)
 
        else:
            print(f"Error in decompiling {output_file}: Bad MAGIC!")
    except Exception as e:
        print(f"Error running pycdc: {e}")


if __name__ == "__main__":
    os.mkdir('output')
    os.mkdir('results')
    input_pyc = "library.pyc"
    # output_pyc = "b.pyc"
    for v,n in list_magic.items():
        
        
        output_pyc = "output/"+v+"_"+n+".pyc"
        # print(v,n)
        new_header = int_to_hex_2s_complement(int(n))
        modify_pyc_header(input_pyc, output_pyc, new_header)