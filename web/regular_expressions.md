# Regular Expressions
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
| Regex     | Description                                              |
|-----------|----------------------------------------------------------|
| `.`       | any character                                            |
| `?`       | zero or one occurrance (previous element optional)       |
| `+`       | one or more occurrances for previous element             |
| `*`       | zero or more occurrances for previous element            |
| `+?`      | lazy (the least possible) one or more occurrances        |
| `*?`      | lazy (the least possible) zero or more occurrances       |
| `{n}`     | `n` occurrances for previous element                     |
| `{n,}`    | `n` or more occurrances for previous element             |
| `{n,m}`   | `n` to `m` occurrances for previous element              |
| `\a`      | escapes following character as plain text                |
| `^abc`    | starts with following pattern                            |
| `abc$`    | ends with previous pattern                               |
|-----------|----------------------------------------------------------|
| `(abc)`   | captures the group in `()` (can be retrieved separately) |
| `(ab\|c)` | captures either group separated by `\|`                  |
| `[abc]`   | matches one character in `[]`, supports `-` as a range   |
| `[^abc]`  | matches one character not in `[]`                        |
|-----------|----------------------------------------------------------|
| `\d`      | numeric, same as `[0-9]`                                 |
| `\w`      | alphanumeric, same as `[a-zA-Z0-9_]`                     |
| `\s`      | spaces, same as `[\r\n\t\f\v ]`                          |
| `\D`      | non numeric, same as `[^0-9]`                            |
| `\W`      | non alphanumeric, same as `[^a-zA-Z0-9_]`                |
| `\S`      | non spaces, same as `[^\r\n\t\f\v ]`                     |


| Flags    | Description |
|----------|-------------|
| `/abc/g` |             |

## JavaScript
```javascript
result = /(abc).*(fgh)/.exec('xxxabcdefghi');
result = [ 'abcdefgh', 'abc', 'fgh', index: 3, input: 'abcdefghi' ]
// [everything matched, group 1, ..., first index matched, original query]
```

