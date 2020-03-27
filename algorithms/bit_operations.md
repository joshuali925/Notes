# Bit Operations
| Operation                    | Code                            |
|------------------------------|---------------------------------|
| set union                    | <code>A &#124; B</code>         |
| set intersection             | `A & B`                         |
| set subtraction              | `A & ~B`                        |
| set negation                 | `~A`                            |
| get all 1-bits               | `~0`                            |
| set bit                      | <code>A &#124;= 1 << bit</code> |
| clear bit                    | `A &= ~(1 << bit)`              |
| test bit                     | `(A & 1 << bit) != 0`           |
| least significant bit        | `A & -A`, `A & ~(A - 1)`        |
| remove least significant bit | `A & (A - 1)`                   |
| test power of 2              | `A != 0 && A & (A - 1) == 0`    |

## Count Bits
```python
def count_bits(n):
    if n == 0: return 0
    return 1 + count_bits(n & (n - 1))
```

## Most Significant Bit
```python
# 273 => 256
def most_significant_bit(n):
    return 2**(int(math.log(n, 2)))
```

## Toggle i-th Bit From the Right (i = 0, 1, ...)
```python
def toggle_bit(n, i):
    if (n & (1 << i)) == 0:
        return n | (1 << i)
    return n & ~(1 << n)
```
