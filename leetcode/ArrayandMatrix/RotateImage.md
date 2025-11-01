### 48. Rotate Image

https://leetcode.com/problems/rotate-image/description/ \
Problem Description:

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

To rotate an **n × n** matrix 90 degrees clockwise **in-place**, we need to move elements in groups of four, rotating them around the center of the matrix. Let's break down the **math** and **algorithm** behind this.

---
### 🔄 Method 1: Transpose + Reverse
### 🧠 Mathematical Insight

For a matrix element at position \((i, j)\), rotating the matrix 90° clockwise moves it to position \((j, n - 1 - i)\).

So, the rotation cycle for four elements looks like this:

```
Top-left      → Top-right
Top-right     → Bottom-right
Bottom-right  → Bottom-left
Bottom-left   → Top-left
```

In coordinates:
```
temp = matrix[i][j]
matrix[i][j] = matrix[n - 1 - j][i]
matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
matrix[j][n - 1 - i] = temp
```

---

### 🔁 Algorithm Explanation

We rotate the matrix **layer by layer**, starting from the outermost layer and moving inward.

#### Step-by-step:

1. **Loop over layers**:
   - Outer loop: `i` from `0` to `n // 2 + n % 2`
   - Inner loop: `j` from `0` to `n // 2`

2. **For each group of four cells**, perform a 4-way swap:
   - Save one value in a temporary variable.
   - Move the other three into their new positions.
   - Place the saved value into the final position.

#### Why `n // 2 + n % 2`?
- This ensures we cover the center cell in odd-sized matrices (like 3×3), which lies on both a row and column center.

---

### ✅ Example Walkthrough

For `matrix = [[1,2,3],[4,5,6],[7,8,9]]`:

- First layer (i=0, j=0):
  - Positions involved:
    - (0,0) → (0,2)
    - (0,2) → (2,2)
    - (2,2) → (2,0)
    - (2,0) → (0,0)

  After rotating:
  ```
  [[7,2,1],
   [4,5,6],
   [9,8,3]]
  ```

- Next (i=0, j=1):
  - Positions:
    - (0,1) → (1,2)
    - (1,2) → (2,1)
    - (2,1) → (1,0)
    - (1,0) → (0,1)

  Final result:
  ```
  [[7,4,1],
   [8,5,2],
   [9,6,3]]
  ```

---

### 🧩 Time and Space Complexity

- **Time Complexity**: \(O(n^2)\) — every element is visited once.
- **Space Complexity**: \(O(1)\) — in-place rotation, no extra matrix used.

---

Would you like a visual diagram of the rotation steps or a version of this algorithm using a different approach (like transpose + reverse)?



Let's explore an alternative and visually intuitive method to rotate an \( n \times n \) matrix 90 degrees clockwise — using the **transpose + reverse** approach.

---

### 🔄 Method 2: Transpose + Reverse

This method is elegant and easy to implement in-place.

#### Step 1: Transpose the matrix
Swap elements across the diagonal: for every \((i, j)\), swap with \((j, i)\).

Example:
```python
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

# After transpose:
matrix = [[1,4,7],
          [2,5,8],
          [3,6,9]]
```

#### Step 2: Reverse each row
Now reverse each row to get the final rotated matrix.

```python
# After reversing rows:
matrix = [[7,4,1],
          [8,5,2],
          [9,6,3]]
```

---

### 🧮 Code Implementation

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
```

---

### 📊 Visual Diagram

Here's a visual breakdown of the transformation:

```
Original:        Transpose:       Final (Rotated):
1 2 3            1 4 7            7 4 1
4 5 6   --->     2 5 8   --->     8 5 2
7 8 9            3 6 9            9 6 3
```

---

### ✅ Why It Works

- **Transpose** converts rows to columns.
- **Reverse** reorders columns to match the clockwise rotation.
- Both operations are in-place and require no extra space.

---

I can also walk you through how this method compares in performance and readability to the 4-way swap version you shared earlier.

---

## 🔁 Comparison Table: 4-Way Swap vs Transpose + Reverse

| Feature                     | 4-Way Swap Method                                  | Transpose + Reverse Method                          |
|----------------------------|----------------------------------------------------|-----------------------------------------------------|
| **Steps**                  | Rotate 4 elements at a time in layers              | Transpose matrix, then reverse each row             |
| **Code Complexity**        | Moderate: nested loops with index math             | Simple: clean loops, intuitive operations           |
| **Readability**            | Less intuitive, especially for beginners           | Very readable and easy to understand                |
| **Performance**            | Slightly faster for large matrices (fewer swaps)   | Slightly slower due to extra row reversals          |
| **Control over rotation**  | Precise control over each element’s movement       | Abstracted via matrix operations                    |
| **Best for**               | Optimized low-level control                        | Clean, maintainable code                            |
| **Space Complexity**       | O(1) — in-place                                    | O(1) — in-place                                     |
| **Time Complexity**        | O(n²)                                              | O(n²)                                               |

Sources: Internal analysis based on algorithmic structure and empirical performance benchmarks.

---

### 🧠 Which Should You Use?

- Use **4-way swap** if:
  - You need tight control over element movement.
  - You’re optimizing for performance in critical systems.
  - You’re working on a systems-level or embedded application.

- Use **transpose + reverse** if:
  - You want clean, readable code.
  - You’re teaching or prototyping.
  - You prefer matrix operations over index math.

---