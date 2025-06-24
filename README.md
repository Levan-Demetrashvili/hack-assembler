# Hack Assembler

A simple assembler for the Hack assembly language, converting `.asm` files to `.hack` binary files.

## Overview

This assembler translates Hack assembly code into 16-bit binary machine code for the Hack computer platform. It handles A-instructions, C-instructions, and symbol resolution.

## Usage

```bash
python app.py (*.asm file)
```

This generates `*.hack` containing the binary machine code.

## Features

- Converts A-instructions (@value) to binary
- Translates C-instructions (dest=comp;jump) to binary
- Resolves labels and variables
- Handles predefined symbols (R0-R15, SCREEN, KBD, etc.)

## Input Format

Hack assembly files (`.asm`) containing:
- A-instructions: `@value` or `@symbol`
- C-instructions: `dest=comp;jump` (dest and jump are optional)
- Labels: `(LABEL)`
- Comments: `// comment`

## Requirements

- Python 3.x
