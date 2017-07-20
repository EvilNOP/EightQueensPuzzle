# EightQueensPuzzle

![Platform](https://img.shields.io/badge/platform-python-orange.svg?style=flat)
![Language](https://img.shields.io/badge/python27-compatible-4BC51D.svg?style=flat)

- [Introduction](#introduction)
- [Usage](#usage)

## Introduction

This is a much loved computer science puzzle: you have a chessboard and eight 
queen pieces to place on it. The only requirement is that none of the queens 
threatens any of the others; that is, you must place them so that no two queens 
can capture each other. 

This is a typical backtracking problem: you try one position for the first 
queen (in the first row), advance to the second, and so on. If you find that you 
are unable to place a queen, you backtrack to the previous one and try another 
position. Finally, you either exhaust all possibilities or find a solution.

## Usage
```python
queens()
```
