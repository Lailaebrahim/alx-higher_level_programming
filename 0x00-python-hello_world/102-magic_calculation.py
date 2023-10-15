#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    result = 98  # LOAD_CONST 1 (98)
    result = result ** a  # BINARY_POWER
    result = result + b  # BINARY_ADD
    return result
