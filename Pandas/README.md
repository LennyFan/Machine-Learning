
### Create matrix

```python
import pandas as pd

pd.DataFrame( 0.0, index = [0,1,2], columns = [0,1,2] )

pd.DataFrame( df )
```

### Joint matrix

```python
pd.concat( [df1,df2] , axis = 1 ) # 0-straight , 1-harizon
```

### max/sum

- max/sum
```python
df.sum(0) # 0-straight , 1-harizon
df.max(0) # 0-straight , 1-harizon
```
