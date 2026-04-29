# Logo Language Parser & Interpreter

A simple Logo language parser and interpreter written in Python from scratch. Features a hand-crafted **LL(1) recursive descent parser**, AST-based evaluation, scoped symbol table, and semantic error detection.

Built as part of a compilers course, based on Chapter 4 of the Dragon Book (*Compilers: Principles, Techniques, and Tools*).

---

## Architecture

```
Source Code (.txt)
      │
      v
  ┌────────┐
  │ Lexer  │  Tokenizes input (handles keywords, operators, literals)
  └────────┘
      │ tokens
      v
  ┌────────┐
  │ Parser │  LL(1) Recursive Descent — validates syntax & builds AST
  └────────┘
      │ AST nodes
      v
  ┌────────────┐
  │ Translator │  AST node definitions (Numeric, Logic, Void)
  └────────────┘
      │ eval(env)
      v
  ┌─────────────┐
  │ SymbolTable │  Scoped variable storage — lookup, insert, set
  └─────────────┘
```

---

## Features

- **Lexer** with dual-buffer reads, comment handling (`%`), and support for all Logo tokens
- **LL(1) Recursive Descent Parser** built by hand from a BNF grammar
- **AST construction** — every expression and statement builds a node tree
- **Symbol Table** with scope chaining for nested environments
- **Semantic error detection**:
  - Duplicate variable declarations
  - Use of undeclared variables
- **Syntactic error detection**:
  - Invalid operators
  - Malformed expressions
  - Unclosed parentheses

---

## Supported Language Features

### Declarations
```logo
VAR x, y, z
```

### Assignments
```logo
x := 10
y := (x * 2) + 1
```

### Expressions
| Category | Operators |
|---|---|
| Arithmetic | `+` `-` `*` `/` `MOD` |
| Relational | `<` `<=` `>` `>=` |
| Equality | `=` `<>` |
| Logical | `AND` `OR` `NOT` |
| Unary | `-` `!` |
| Literals | numbers, `#T`, `#F` |

### Statements
```logo
PRINT(x + y)
PRINT((x > y) AND (x < z))
```

---

## Project Structure

```
├── Lexer.py          # Tokenizer with dual-buffer
├── Parser.py         # LL(1) recursive descent parser + AST builder
├── Translator.py     # AST node classes with eval()
├── SymbolTable.py    # Scoped symbol table
├── Type.py           # Type enum (NUMBER, BOOLEAN)
├── main.py           # Entry point
└── test/
    └──good/   # Valid programs
      └──input02.txt
        ...
     └──bad/   # Invalid program (for error detection)
      └──input04.txt
        ...   
```

---

## Getting Started

**Requirements:** Python 3.x — no external dependencies.

```bash
# Clone the repo
git clone https://github.com/Emiidk01/logo-simple-parser.git
cd logo-simple-parser

# Run with a test file
python main.py
```

To change the input file, edit `main.py`:
```python
parser = Parser("test_cases/good/input02.txt")
parser.analize()
```

---

## Example

**Input (`input02.txt`):**
```logo
VAR x, y, z

x := 1
y := 2
z := 3
PRINT(x > y)
PRINT(x < z)
PRINT((x > y) AND (x < z))
```

**Output:**
```
False
True
False
ACCEPTED
```

---

## Error Detection Examples

**Duplicate declaration:**
```logo
VAR x, y, x   % Error: x declared twice
```
```
Exception: Line 1 - X has already been declared
```

**Undeclared variable:**
```logo
VAR x
y := 5   % Error: y was never declared
```
```
Exception: Line 2 - Y has not been declared
```

**Invalid operator:**
```logo
VAR x, y
x := 5
PRINT(x >> y)   % Error: >> is not valid
```
```
Exception: Line 3 - expected an additive expression before '>'
```

---

## Grammar (BNF)

```bnf
<program>            ::= <declaration-sequence> <statement-sequence>
<declaration-sequence> ::= VAR <identifier> <identifier-list>
<identifier-list>    ::= ',' <identifier> <identifier-list> | ε
<statement-sequence> ::= <statement> <statement-sequence> | ε
<statement>          ::= <assignment-statement> | <text-statement>
<assignment-statement> ::= <identifier> ':=' <expression>
<text-statement>     ::= PRINT '(' <expression> ')'
<expression>         ::= <conditional-expression>
```
*(Full grammar available in `grammar.txt`)*

---

## References

- Aho, Lam, Sethi, Ullman — *Compilers: Principles, Techniques, and Tools* (2nd ed.), Chapter 4
