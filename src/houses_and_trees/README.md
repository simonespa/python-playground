Given in input a 2-dimensional array of size `N x M` containing strings, and an integer `A`. Each cell of the grid can only contain one the following values:

- `0` indicates free land;
- `*` indicates a tree;
- an integer greater than 0 that indicates a house;

Verify that the following conditions are all met:

- The total number of trees in the grid is equal to `A`;
- The number of houses in each row is strictly greater than the number of trees
- For each cell, the number of adjacent cells containing trees must be equal to the number indicated by the cell itself

If all the condition are met, the function must return `True`, otherwise `False`

**Example 1**

A = 2

```
1  1  0  0  0
*  1  0  1  1
1  1  0  1  *
```

returns True

**Example 2**

A = 0

```
1  1  0  0  0
*  1  0  1  1
1  1  0  1  *
```

returns `False` because the total number of trees in the grid is 2 and it is different from the value of `A`.
