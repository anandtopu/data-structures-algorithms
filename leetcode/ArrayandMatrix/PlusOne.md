Here are both **brute-force** and **optimized** solutions for the **plus-one problem**, where you're given a large integer as an array of digits and need to increment it by one.

---

## 🧪 Brute-Force Solution

### 🔍 Idea:
Convert the array to an integer, add one, then convert back to a list of digits.

### ✅ Code:
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for d in digits:
            num = num * 10 + d
        num += 1
        return [int(x) for x in str(num)]
```

### ⏱ Complexity:
- **Time**: \( O(n) \) — converting to and from string/integer
- **Space**: \( O(n) \) — new list created

### ⚠️ Limitation:
- Not ideal for very large numbers (e.g. 100-digit input), as it relies on integer conversion and string parsing.

---

## ⚡ Optimized In-Place Solution

### 🔍 Idea:
Start from the last digit, add one, and handle carry. If there's no carry, return early. If carry propagates through all digits, insert `1` at the front.

### ✅ Code:
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
```

### 🧠 How It Works:
- If digit < 9 → just increment and return.
- If digit == 9 → set to 0 and continue.
- If all digits are 9 (e.g. [9,9,9]) → result is [1,0,0,0]

### ⏱ Complexity:
- **Time**: \( O(n) \)
- **Space**: \( O(1) \) extra — modifies input in-place

---

## 🧩 Example Walkthrough

### Input: `[9, 9, 9]`
- 9 → 0 (carry)
- 9 → 0 (carry)
- 9 → 0 (carry)
- Insert 1 at front → `[1, 0, 0, 0]`

---