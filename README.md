<h1 align="center">
    <img width="150" src="./PowREPL-logo.png">
    <br/>
    PowREPL
</h1>

<p align="center">The simple REPL for declarative calculations I've been missing</p>

This project is a simple REPL I built with the goal of recreating the experience that is using PowerShell as a calculator (Read-Eval-Print Loop + E/EXP/EEX/Calculator Scientific Notation) and pairing it with some custom operators.

### Changelog

- Feb 18, 2023: PowREPL v0.1.0, pretty unstable.

### Roadmap

- [x] E/EXP/EEX/Calculator Scientific Notation

- [x] A %> B = A% of B

- [x] A %? B = What percent of B is A? | How much of A is part of the whole of B?

- [ ] A % B = A (mod B) | Remainder of A ÷ B

- [ ] Better Result Units

### Known Issues

Custom operators are prematurely evaluated when simplifying input
```plaintext
PowREPL> (5 %? 10) * 10

...

File "<string>", line 1
    (5 %? 10)
        ^
SyntaxError: invalid syntax
```