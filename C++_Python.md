C++ / Python

## Class

- C++
```c++
class Constructor {
public:
    // initial
    // 1.
    Constructor(vector<int> nums) {
        n.assign(nums.begin(), nums.end());  // n = list(nums)
    }
    // 2.
    Constructor() {
        vector<int> temp (4,0);                       // four ints with value 0
        n.assign(temp.begin(), temp.end());
    }
    
    int function(int i, int j) {
        int ret = 0;
        return i+j+ret;
    }
private:
    vector<int> n;
};
```
- python
```python
class Constructor(object):
    # initial
    def __init__(self, nums = None):
        self.n = list(nums) if nums != None else [0,0,0,0]
        
    def function(self, i, j):
        ret = 0
        return i+j+ret
```

## Vector
- c++
```c++
std::vector<int> first;                                // empty vector of ints
std::vector<int> second (4,100);                       // four ints with value 100
std::vector<int> third (second.begin(),second.end());  // iterating through second
std::vector<int> fourth (third);                       // a copy of third

int myints[] = {16,2,77,29};  // int myints[4] = {16,2,77,29};
std::vector<int> fifth (myints, myints + sizeof(myints) / sizeof(int) );
```
