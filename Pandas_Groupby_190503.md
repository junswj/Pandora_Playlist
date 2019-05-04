

```python
import pandas as pd
import numpy as np

grocery = pd.DataFrame({'category':['produce', 'produce', 'meat',
                                    'meat', 'meat', 'cheese', 'cheese'],
                        'item':['celery', 'apple', 'ham', 'turkey',  'lamb',
                                'cheddar', 'brie'],
                        'price':[.99, .49, 1.89, 4.34, 9.50, 6.25, 8.0]})
```

1.Remove all items in categories where the mean price in that category is less than $3.00.


```python
grocery.groupby('category').filter(lambda x : x.mean()>3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>item</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>meat</td>
      <td>ham</td>
      <td>1.89</td>
    </tr>
    <tr>
      <th>3</th>
      <td>meat</td>
      <td>turkey</td>
      <td>4.34</td>
    </tr>
    <tr>
      <th>4</th>
      <td>meat</td>
      <td>lamb</td>
      <td>9.50</td>
    </tr>
    <tr>
      <th>5</th>
      <td>cheese</td>
      <td>cheddar</td>
      <td>6.25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>cheese</td>
      <td>brie</td>
      <td>8.00</td>
    </tr>
  </tbody>
</table>
</div>



2.Find the maximum values in each category for all features.


```python
grocery.groupby('category').max()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>item</th>
      <th>price</th>
    </tr>
    <tr>
      <th>category</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>cheese</th>
      <td>cheddar</td>
      <td>8.00</td>
    </tr>
    <tr>
      <th>meat</th>
      <td>turkey</td>
      <td>9.50</td>
    </tr>
    <tr>
      <th>produce</th>
      <td>celery</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>
</div>




```python
max_index=grocery.groupby('category')['price'].idxmax
```


```python
grocery.loc[max_index]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>item</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>cheese</td>
      <td>brie</td>
      <td>8.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>meat</td>
      <td>lamb</td>
      <td>9.50</td>
    </tr>
    <tr>
      <th>0</th>
      <td>produce</td>
      <td>celery</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>
</div>



3.If the maximum price in a category is more than $3.00, reduce all prices in that category by 10%. Return a Series of the new price column.


```python
grocery.groupby('category')['price'].transform(lambda x: x*.9 if x.mean()>3 else x)
```




    0    0.990
    1    0.490
    2    1.701
    3    3.906
    4    8.550
    5    5.625
    6    7.200
    Name: price, dtype: float64



**Playing around**


```python
grocery.groupby('category').apply(lambda x: x['price']*.9)
```




    category   
    cheese    5    5.625
              6    7.200
    meat      2    1.701
              3    3.906
              4    8.550
    produce   0    0.891
              1    0.441
    Name: price, dtype: float64




```python
grocery.groupby('category')['price'].apply(lambda x: x*.9)
```




    0    0.891
    1    0.441
    2    1.701
    3    3.906
    4    8.550
    5    5.625
    6    7.200
    Name: price, dtype: float64




```python
grocery.groupby('category')['price'].apply(lambda x: x*.9 if x.mean()>3 else x)
```




    0    0.990
    1    0.490
    2    1.701
    3    3.906
    4    8.550
    5    5.625
    6    7.200
    Name: price, dtype: float64


