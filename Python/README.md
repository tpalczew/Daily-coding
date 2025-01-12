# Python exercises

## Typing and annotations:

* youtube: https://www.google.com/search?q=python+typing+annotations+explained+youtube+&sca_esv=6ea0299b7e47179f&rlz=1C5CHFA_enUS1094US1094&sxsrf=ADLYWIKB6v3nqRzDRewGSWQbKYXyqbz1LQ%3A1736715923826&ei=ky6EZ-yTMrCw0PEPzoHmmAY&ved=0ahUKEwisqdz9ivGKAxUwGDQIHc6AGWMQ4dUDCBA&uact=5&oq=python+typing+annotations+explained+youtube+&gs_lp=Egxnd3Mtd2l6LXNlcnAiLHB5dGhvbiB0eXBpbmcgYW5ub3RhdGlvbnMgZXhwbGFpbmVkIHlvdXR1YmUgMgUQIRigATIFECEYoAEyBRAhGKABMgUQIRigATIFECEYoAEyBRAhGJ8FMgUQIRifBTIFECEYnwVIokRQwARYnENwAXgBkAEAmAGuAaABuBuqAQUyNy4xMLgBA8gBAPgBAZgCJqACuRzCAgoQABiwAxjWBBhHwgILEAAYgAQYkQIYigXCAg4QABiABBiRAhixAxiKBcICDRAAGIAEGLEDGBQYhwLCAggQABiABBixA8ICBRAAGIAEwgIKEAAYgAQYFBiHAsICCBAAGBYYChgewgIGEAAYFhgewgILEAAYgAQYhgMYigXCAggQABiiBBiJBcICCBAAGIAEGKIEwgIFEAAY7wXCAgUQIRirApgDAOIDBRIBMSBAiAYBkAYIkgcFMjcuMTGgB47YAQ&sclient=gws-wiz-serp#fpstate=ive&vld=cid:a4527cec,vid:QORvB-_mbZ0,st:0 

* https://www.youtube.com/watch?v=c63aia0Ir_c

* https://www.youtube.com/watch?v=Y9fT4HVdCuQ 



Commonly used types:

Built-in Types: int, float, str, bool, list, tuple, dict, etc.

Typing Module: List, Tuple, Dict, Set, Optional, Union, Any, Callable, etc.


Example:
Python

```
from typing import List, Dict

def process_data(data: List[Dict[str, int]]) -> int:
    total = 0
    for item in data:
        total += item["value"]
    return total
```
