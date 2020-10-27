# JavaScript Basics
## Arrays
- create an array from 0 to 9
```javascript
let arr = Array.from({ length: 10 }, (v, i) => i)  // [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
```

- spread array to arguments / use apply to find max
```javascript
Math.max(...arr)  // 9
Math.max.apply(null, arr)  // 9
```

- reduce array to calculate sum
```javascript
arr.reduce((a, b) => a + b, 0)  // 45
```

- add to array, push add to the tail, unshift adds to the head, both inplace
```javascript
arr.push(5)
arr.push(...[5, 5, 5])
arr.unshift(...[5, 5, 5])  // arr = [ 5, 5, 5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 5, 5, 5 ]
arr.concat([5, 5, 5])  // [ 5, 5, 5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 5, 5, 5, 5, 5, 5 ], concat returns new array
```

- remove 5
```javascript
arr = arr.filter(num => num !== 5)  // [ 0, 1, 2, 3, 4, 6, 7, 8, 9 ]
```

- remove / insert element at index 2
    - `splice(index, removeHowMany, newItem1, newItem2, ...)`
```javascript
arr.splice(2, 1)  // [ 2 ], arr = [ 0, 1, 3, 4, 6, 7, 8, 9 ]
arr.splice(2, 0, 2)  // [], arr = [ 0, 1, 2, 3, 4, 6, 7, 8, 9 ]
```

- remove first / last element
```javascript
let [first, last] = [arr.shift(), arr.pop()]  // first = 0, last = 9, arr = [ 1, 2, 3, 4, 6, 7, 8 ]
```

- remove duplicate elements
```javascript
arr = arr.filter((val, idx, self) => self.indexOf(val) === i)
```

- last 3 elements
```javascript
arr.slice(-3)  // [ 6, 7, 8 ], NOTE Array.slice and String.slice works similar to python's [i:j] slice
```

- shuffle array
```javascript
arr.sort(() => Math.random() - 0.5)
```

- sort array descending then reverse, inplace
```javascript
arr.sort((a, b) => b - a).reverse()  // [ 1, 2, 3, 4, 6, 7, 8 ]
```

- copy array
```javascript
let newArr = [...arr]
```

- clear array
```javascript
arr.length = 0  // arr = []
```

- flatten 2D array
```javascript
[].concat(...[[1, 2], [3, 4, 5], [6, 7, [8], 9]])  // [ 1, 2, 3, 4, 5, 6, 7, [ 8 ], 9 ]
```

- for element of iterable
```javascript
for (const n of newArr)
    console.log(n)
```

## Strings
### substr, substring, slice
- prefer slice
#### string.substr(start [, length])
```javascript
let str = '0123456789'
str.substr(3)  // '3456789'
str.substr(3, 100)  // '3456789'
str.substr(3, 4)  // '3456'
str.substr(3, -1)  // ''
str.substr(-3, 2)  // '78'
```

#### string.substring(start [, stop]): [start, stop)
- swaps arguments if `start` > `stop`
- uses `0` if either argument is negative or `NAN`
```javascript
str.substring(3)  // '3456789'
str.substring(3, 100)  // '3456789'
str.substring(7, 3) === str.substring(3, 7)  // true ('3456789')
str.substring(3, -1) === str.substring(0, 3)  // true ('012')
```

#### string.slice(start [, stop]): [start, stop)
- behaves like slice in python
```javascript
str.slice(3)  // '3456789'
str.slice(-3)  // '789'
str.slice(3, 100)  // '3456789'
str.slice(3, -3)  // '3456'
str.slice(-3, 3)  // ''
```

## Objects
- merge object using spread
```javascript
let obj1 = { a: 1, b: 2 }
let obj2 = { c: 3, b: 4 }
let obj3 = { ...obj1, ...obj2 }  // { a: 1, b: 4, c: 3 }

- get keys / key value pairs
```javascript
Object.keys(obj3)  // [ 'a', 'b', 'c' ]
Object.entries(obj3)  // [ [ 'a', 1 ], [ 'b', 4 ], [ 'c', 3 ] ]
```

- deconstruct object
```javascript
let { b, c = 'default', d = 'default', e, ...rest } = obj3  // b = 4, c = 3, d = 'default', e = undefined, rest = { a: 1 }
```

- get value using key
```javascript
obj3.b === obj3['b']  // true
obj3.1 = 10  // key is not string, syntax error
obj3['1'] = 10  // this works, same as obj3[1] = 10
```

- delete key
```javascript
delete obj3['1']
```

- computed property name (use variable's string value as key)
```javascript
let s = 'hello'
obj3 = { ...obj3, [s]: 'world' }  // { a: 1, b: 4, c: 3, hello: 'world' }
```

- for key in object
```javascript
for (let key in obj3)
    console.log(key, obj3[key])
```

- use array.forEach loop
```javascript
Object.keys(obj3).forEach(key => console.log(key, obj3[key]));
```

## Random
- random integer in `[min, max]`
```javascript
const randint = (min, max) => Math.floor(Math.random() * (max - min + 1) + min);
```

- random float in `[min, max]`
```javascript
const randfloat = (min, max) => Math.random() * (max - min) + min;
```

- random string
```javascript
const randString = () => Array.from({ length: 10 }, () => Math.random().toString(36).substring(2)).join('');
```

- random pastel color
```javascript
const randColor = () => `#${((Math.random() * 0xFFFFFF + 0xFFFFFF) >> 1).toString(16)}`;
```

## Regex
```javascript
result = /pattern/flags.exec(query)

result = /(abc).*(fgh)/.exec('xxxabcdefghi');
// result == [ 'abcdefgh', 'abc', 'fgh', index: 3, input: 'abcdefghi' ]
// [everything matched, group 1, ..., first index matched, original query]
```

## Promises
- https://javascript.info/async
- simpler callbacks to handle async operations
```javascript
let p = new Promise((resolve, reject) => {
    // long operations
    if (1 + 1 === 2)
        resolve('success')
    else
        reject('failed')
})
p.then(msg => console.log(msg)).catch(msg => console.log(msg))
// multiple promises
Promise.all([p1, p2, p3]).then(msg => console.log(msg)).catch(msg => console.log(msg))
```

| promise functions | description                                 |
|-------------------|---------------------------------------------|
| Promise.all       | runs all given promises                     |
| Promise.race      | runs until the first given promise finishes |

### Using `fetch()`
- fetch returns a Promise, where it `resolve(the response)`
- the response resolved has `.json()` method, which returns another Promise that `resolve(the json data from the response)`
```javascript
fetch('http://example.com/movies.json')
    .then(response => response.json())
    .then(jsonData => console.log(JSON.stringify(jsonData)))
```

### Promise chain
- await on async functions before next execution
```javascript
// sleep sort
const randint = (min, max) => Math.floor(Math.random() * (max - min + 1) + min);
const arr = Array.from({ length: 10 }, (v, i) => randint(1, 10) * 100);
const reducer = (num) => {
  return new Promise((resolve) => setTimeout(() => {
    console.log(num);
    resolve();
  }, num))
};
arr.map((num) => reducer(num)).reduce((chain, func) => chain.then(func), Promise.resolve());

// in one line
arr.map((num) => new Promise((resolve) => setTimeout(() => {
    console.log(num);
    resolve();
  }, num))).reduce((chain, func) => chain.then(func), Promise.resolve());
```

## Async/Await
- `await` only works in `async` functions
```javascript
function request(location) {
    return new Promise((resolve, reject) => {
        if (location === 'google')
            resolve('it is google')
        else
            reject('it is not google')
    })
}
async function work() {
    try {
        const resp = await request('google') 
        console.log(resp)
    } catch (err) {
        console.log('err is the reject parameter ' + err)
    }
}
```

