Here’s a complete breakdown of how to solve this intersection problem efficiently — including the base solution and optimizations for the follow-up scenarios.

---

## ✅ Core Solution: Hash Map Frequency Count

### Goal:
Return elements that appear in both arrays, **as many times as they appear in both**.

### Python Code:
```python
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        result = []
        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1
        return result
```

### 🔍 How It Works:
- Count frequencies of elements in `nums1`.
- Iterate over `nums2`, and for each match in the counter, add to result and decrement the count.

### ⏱ Time & Space:
- **Time**: \( O(n + m) \)
- **Space**: \( O(n) \) — for the counter

---

## 🔁 Follow-Up Optimizations

### 1️⃣ If Arrays Are Sorted

Use **two pointers** to traverse both arrays.

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
```

### Benefits:
- **Time**: \( O(n \log n + m \log m) \) for sorting, then \( O(n + m) \) for traversal
- **Space**: \( O(1) \) extra if sorting in-place

---

### 2️⃣ If `nums1` Is Much Smaller Than `nums2`

Use the **hash map approach**, but build the counter from the smaller array.

```python
if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1
```

This minimizes memory usage and speeds up lookup.

---

### 3️⃣ If `nums2` Is Stored on Disk (Streaming)

You can’t load all of `nums2` into memory. Use a **streaming approach**:

- Load `nums1` into a hash map.
- Stream `nums2` chunk by chunk.
- For each chunk, check against the hash map and build the result.

This is a classic **external memory algorithm** pattern.

---