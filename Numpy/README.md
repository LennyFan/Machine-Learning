### Create nxm matrix
- array
- random
- insert
```python
import numpy as np

# self define
np.array([[ 0 for i in range(m) ] for j in range(n) ] )

# random
np.random.rand(n,m)

# zero
np.zeros((n,m))

```

### Add Column

- insert 
```python
# insert 1 at first column
a = np.zeros((n,m))
b = np.insert( a , 0, 1, axis = 1)

```

### LinearAlgebra
- linalg
```python
# dot
a.dot(b)
np.dot(a,b)

# inverse
np.linalg.inv(a)
```
