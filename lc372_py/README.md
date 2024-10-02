372. Super Pow
Medium
Topics
Companies
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

 

Example 1:

Input: a = 2, b = [3]
Output: 8
Example 2:

Input: a = 2, b = [1,0]
Output: 1024
Example 3:

Input: a = 1, b = [4,3,3,8,5,2]
Output: 1
 

Constraints:

1 <= a <= 231 - 1
1 <= b.length <= 2000
0 <= b[i] <= 9
b does not contain leading zeros.




这个函数 `superPow` 的目的是计算一个整数 `a`（基数）在大数 `b`（指数）上的幂，结果对 1337 取模。由于 `b` 可能是一个很大的数（以列表的形式给出），而直接计算 `a^b` 将变得不切实际，所以我们使用了一些数学性质及模运算来优化这一计算过程。

### 详细解释这个算法及变量含义：

1. **模定理**: 
   当我们计算 \( a^b \mod m \) 时，我们可以利用性质：\( (x \cdot y) \mod m = [(x \mod m) \cdot (y \mod m)] \mod m \)。因此，该算法会首先计算 `a` 对 1337 的模值。

2. **特例处理**:
```python
if a == 1:
   return 1
```
   如果 `a` 等于 1，任何数的次方都是 1，因此直接返回 1。

3. **计算 `a` 的模值**:
   ```python
   a %= 1337
   ```
   获取 \( a \mod 1337 \)。这对于后面的计算是至关重要的，因为我们一直都对结果进行模运算来防止数值过大。

4. **找到循环節**:
   ```python
   temp = a * a
   cycle_len = 1
   while temp != a:
       temp = (temp * a) % 1337
       cycle_len += 1
   ```
   在这个部分，我们通过计算 \( a^1, a^2, a^3, \ldots \) 的模值来找到一个"循环"，即当计算到某个指数时，\( a^k \mod 1337 \) 的数值可能会重复。因此，我们需要找到这个循环的长度，即 \( a \) 的幂运算结果重复前的个数。

5. **计算指数的余数**:
   ```python
   remainder = 0
   for i in range(len(b)):
       remainder = (remainder * 10 + b[i]) % cycle_len
   ```
   由于 `b` 是一个大数的数组形式（例如，`[1, 0]` 表示 10），我们将其转换为相应的指数模 `cycle_len` 的值。这一过程是把大数转为实际计算中所需的较小的指数。每次我们将当前的 `remainder` 乘以 10，并加上 `b[i]`，同时对 `cycle_len` 取模。

6. **处理余数为零的特殊情况**:
   ```python
   if remainder == 0:
       remainder = cycle_len
   ```
   如果 `remainder` 为 0，则意味着因为循环的结构，我们可以将其替换为完整的循环长度。

7. **计算最终结果**:
   ```python
   result = 1
   for i in range(remainder):
       result = (result * a) % 1337
   return result
   ```
   最后，通过简单的幂运算（通过循环把 `a` 乘以自己，得到最终的 \( a^{b} \mod 1337 \)），并进行模运算以保持数值稳定。

### 总结
这个算法利用了模运算、循环节以及大数字的数组表示，避免了直接计算一个大数的幂积，优化了计算效率。通过这些步骤，算法能够在任何情况下都高效地求出 `a` 以 `b` 为幂的结果对 1337 的模值。
