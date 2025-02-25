#!/usr/bin/python3

import dis
import marshal

def extract_pyc_names(pyc_file):
    with open(pyc_file, "rb") as f:
        f.read(16)  # Skip the header (magic number, timestamp, etc.)
        code_obj = marshal.load(f)  # Load compiled bytecode

    for instr in dis.get_instructions(code_obj):
        if instr.opname == "STORE_NAME" and not instr.argval.startswith("__"):
            print(instr.argval)

if __name__ == "__main__":
    extract_pyc_names('hidden_4.pyc')
