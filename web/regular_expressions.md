# Regular Expressions
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
| Quantifiers |                                                    |
|-------------|----------------------------------------------------|
| `a?`        | zero or one occurrance for previous element        |
| `a+`        | one or more occurrances for previous element       |
| `a*`        | zero or more occurrances for previous element      |
| `a+?`       | lazy (the least possible) one or more occurrances  |
| `a*?`       | lazy (the least possible) zero or more occurrances |
| `a{n}`      | `n` occurrances for previous element               |
| `a{n,}`     | `n` or more occurrances for previous element       |
| `a{n,m}`    | `n` to `m` occurrances for previous element        |
| `^abc`      | starts with following pattern                      |
| `abc$`      | ends with previous pattern                         |

| Groups    |                                                          |
|-----------|----------------------------------------------------------|
| `(abc)`   | captures the group in `()` (can be retrieved separately) |
| `(ab\|c)` | captures either group separated by `\|`                  |
| `(?:abc)` | match group in `()` but don't capture                    |

| Characters |                                                        |
|------------|--------------------------------------------------------|
| `.`        | any character, except newline                          |
| `\d`       | numeric, same as `[0-9]`                               |
| `\w`       | alphanumeric, same as `[a-zA-Z0-9_]`                   |
| `\s`       | spaces, same as `[\r\n\t\f\v ]`                        |
| `\D`       | non numeric, same as `[^0-9]`                          |
| `\W`       | non alphanumeric, same as `[^a-zA-Z0-9_]`              |
| `\S`       | non spaces, same as `[^\r\n\t\f\v ]`                   |
| `[abc]`    | matches any character in `[]`, supports `-` as a range |
| `[^abc]`   | matches any character not in `[]`                      |
| `\.`       | escapes following character as plain text              |
| `\t`       | tab                                                    |
| `\n`       | newline                                                |
| `\r`       | carriage return                                        |


| Lookahead & Lookbehind |                                   |
|------------------------|-----------------------------------|
| `a(?=b)`               | `a` in `baby` but not in `bay`    |
| `a(?!b)`               | `a` in `Stan` but not in `Stab`   |
| `(?<=a)b`              | `b` in `crabs` but not in `cribs` |
| `(?<!a)b`              | `b` in `fib` but not in `fab`     |


| Flags    |  |
|----------|--|
| `/abc/g` |  |

## JavaScript
```javascript
result = /(abc).*(fgh)/.exec('xxxabcdefghi');
result = [ 'abcdefgh', 'abc', 'fgh', index: 3, input: 'abcdefghi' ]
// [everything matched, group 1, ..., first index matched, original query]
```

