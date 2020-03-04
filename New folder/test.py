import json
from urllib.request import urlopen

with urlopen("http://localhost:5000/add_empleado") as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))

