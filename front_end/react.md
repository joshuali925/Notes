# React
## JSX html tags
- use `className` instead of `class`
- `style` takes objects instead of strings, properties use `camelCase` instead of `kebab-case` (https://reactjs.org/docs/dom-elements.html)
```javascript
function Clock(props) {
    let styles = {
        color: "#FF8C00", 
        backgroundColor: "black"
    }
    return (
        <h1 className="header" style={styles}>It's {`${new Date().getHours()}:${props.minute}`}!</h1>
    )
}
ReactDOM.render(<Clock minute="30" />, document.findElementById("root"))
```
## Class components
- class components have states where function components don't
- state stores data, should only be changed by `this.setState()`
- `this.setState(prev => {})` returns a new state object, and updates values of previous state (doesn't touch values not mentioned in new state)
```javascript
import React, {Component} from 'react'
class App extends Component {
    constructor() {
        super()
        this.state = { num: 1 }
        this.handleClick = this.handleClick.bind(this)  // bind so that 'this' refers to the class instance
    }
    
    // handleClick = (id) => {...} is a newer syntax, do not need to bind 'this'
    handleClick(id) {
        console.log('id = ' + 3);
        this.setState(prevState => {
            return { num: prevState.num + 1 }
        })
    }
    
    render() {
        return (
            <div onClick={(event) => this.handleClick(3)}>{this.state.num}</div>
        )
    }
}
```

## PropTypes and defaultProps
- `Component.propTypes` forces types of props
- `Component.defaultProps` sets the default props
```javascript
import React, { PropTypes } from 'react';
Component.propTypes = {  // p is lowercase
  // <propName>: PropTypes.<dataType>.isRequired
  age: PropTypes.number.isRequired  // p is uppercase
};
Component.defaultProps = {
  age: 18
}
```

## Events
https://reactjs.org/docs/events.html#supported-events
- onChange, onClick, onMouseOver, ...
## Life cycle methods
https://engineering.musefind.com/react-lifecycle-methods-how-and-when-to-use-them-2111a1b692b1

| life cycle methods                            | description                               |
|-----------------------------------------------|-------------------------------------------|
| render                                        | runs whenever state or props changes      |
| componentDidMount                             | runs when component first shows up (init) |
| shouldComponentUpdate(nextProps, nextState)   | return boolean if component should update |
| componentWillUnmount                          | cleanup before component disappears       |
| static getDerivedStateFromProps(props, state) |                                           |
| getSnapshotBeforeUpdate()                     | create a backup                           |

## Forms
https://reactjs.org/docs/forms.html
- forms with `value` are controlled inputs
- use formik to make it easier
- `checkbox` has `checked` instead of `value`
```javascript
constructor() {
    super()
    this.state = {
        firstName: "",
        lastName: "",
        flag: true
    }
}
handleChange(event) {
    // event.target.id === "inputBox" or null
    // event.target.name === "firstName" or "lastName"
    const {name, value, type, checked} = event.target
    const result = type === "checkbox" ? checked : value;
    this.setState({
        // [event.target.name]: event.target.value  // avoid bug do not use
        [name]: result
    })
}
render() {
    <form onSubmit={(event) => { event.preventDefault() }}>
        <input type="text" name="firstName" value={this.state.firstName} id="inputBox" onChange={this.handleChange}>
        <input type="text" name="lastName" value={this.state.lastName} onChange={this.handleChange}>
        <textarea />
        <input type="checkbox" name="flag" checked={this.state.flag} onChange={this.handleChange}>
        <button>Submit</button>
    </form>
}
```

## Use `map` to render array of elements
```javascript
const arr = [1, 2, 3];
return (
  <>
    {arr.length > 0 ? (
      arr.map((x, i) => <div key={i}>{x}</div>)
    ) : (null)}

    {arr.length > 0 ? (
      arr.map((x, i) => {
        x = x + 1;
        return (
          <div key={i}>{x}</div>
        )
      })
    ) : (null)}
  </>
```

## Resources for newer features
- Official React Context API - https://reactjs.org/docs/context.html
- Error Boundaries - https://reactjs.org/docs/error-boundaries.html
- render props - https://reactjs.org/docs/render-props.html
- Higher Order Components - https://reactjs.org/docs/higher-order-components.html
- React Router - https://reacttraining.com/react-router/core/guides/philosophy
- React Hooks - https://reactjs.org/docs/hooks-intro.html
- React lazy, memo, and Suspense - https://reactjs.org/blog/2018/10/23/react-v-16-6.html

## Project ideas
- https://medium.freecodecamp.org/every-time-you-build-a-to-do-list-app-a-puppy-dies-505b54637a5d
- https://medium.freecodecamp.org/want-to-build-something-fun-heres-a-list-of-sample-web-app-ideas-b991bce0ed9a
- https://medium.freecodecamp.org/summer-is-over-you-should-be-coding-heres-yet-another-list-of-exciting-ideas-to-build-a95d7704d36d
