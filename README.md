# bsapi

A Python implementation of the models in the Battlesnake webhook API.

# Example Usage (with Bottle web server)

```python
import bottle

from random import choice
from bsapi.models import *

app = bottle.app()

@app.post('/move')
def move():
    request = SnakeRequest(bottle.request.json)
    return MoveResponse(choice(['left', 'right', 'up', 'down']))
```
