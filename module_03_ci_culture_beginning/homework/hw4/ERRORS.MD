## Errors:  

### False:

```python
12
return self.yob - now.year

18
self.sername = self.sername

21
self.address == address

5
__init__(self, name: str, year_of_birth: int, address: str = '')

8
self.address: str = address
```


### True:

```python
12
return abs(self.yob - now.year)

18
self.sername = name

21
self.address = address

5
__init__(self, name: str, year_of_birth: int, address: bool = None)

8
self.address: str | bool = address
```
