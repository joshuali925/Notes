# Scraping Using Requests with BeautifulSoup
## Importing
```python
import requests
from bs4 import BeautifulSoup
from lxml import html
import http.cookiejar as cookielib
import pickle
import time
import re
```

# Requests Basics
```python
with requests.Session() as session:
    session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
    response = session.get(url, params=params)
    response = session.post(url, data=payload)
    response.encoding = response.apparent_encoding
```
- `params` in `get()` are `&key=value` parameters in forms of a dict
- `data` in `post()` is the request body in a dict
- `get()` and `post()` also have the `headers` parameter that takes a dict

## Cookies
- dump cookies
```python
with open('cookies.txt', 'wb') as f:
    pickle.dump(session.cookies, f)
```
- load cookies
```python
with open('cookies.txt', 'rb') as f:
    session.cookies.update(pickle.load(f))
# or this, not sure
session.cooikes = cookielib.LWPCookieJar(filename='cookies.txt')
```

# BeautifulSoup Parsing
```python
soup = BeautifulSoup(response.text, 'lxml')
```
| parsers       | description                                    |
|---------------|------------------------------------------------|
| `html.parser` | built-in                                       |
| `lxml`        | C dependency, faster and more lenient          |
| `html5lib`    | slow and most lenient (supports broken `HTML`) |

## Finding Elements
| code                                                             | description                                             |
|------------------------------------------------------------------|---------------------------------------------------------|
| `soup.find_all('div', {'class': 'test'}, {'id': 'ted'})`         | finds `div` that contains `test` class and has `ted` id |
| `soup.find_all('div', class_=lambda c: c and c.startswith('t'))` | class starts with `t`                                   |
| `soup.find_all('div', id=re.compile(r'^te')`                     | id starts with `te`                                     |
| `soup.find('div').get_text()`                                    | `innerHTML` of first `div`                              |
| `soup.find('a')['href']`                                         | URL of `href` attribute of first `a`                    |

# CSS Selectors
# XPath
