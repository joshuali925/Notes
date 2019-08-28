## PropTypes and defaultProps
- `Component.propTypes` forces types of props
- `Component.defaultProps` sets the default props
```javascript
import React, { PropTypes } from 'react';
Component.propTypes = {  // note lowercase p
  // format is propName: PropTypes.dataType.isRequired
  age: PropTypes.number.isRequired
};
Component.defaultProps = {
  age: 18
}
```
