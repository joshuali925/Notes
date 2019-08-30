# JavaScript
## Tips
- create an array from 0 to n - 1: `Array.from({length: n}, (v, i) => i)`

## Promises
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
