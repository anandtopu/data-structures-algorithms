"""
Stack Implementation using List

Time Complexity:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Search: O(n)

Space Complexity: O(n)
"""


class Stack:
    """Stack implementation using Python list."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0
    
    def push(self, item):
        """Push item onto stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item from stack."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]
    
    def size(self):
        """Return number of items in stack."""
        return len(self.items)
    
    def __str__(self):
        """String representation of stack."""
        return str(self.items)


def is_balanced_parentheses(expression):
    """
    Check if parentheses in expression are balanced.
    
    Example: "((()))" -> True, "(()" -> False
    """
    stack = Stack()
    matching = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in matching:
            stack.push(char)
        elif char in matching.values():
            if stack.is_empty():
                return False
            if matching[stack.pop()] != char:
                return False
    
    return stack.is_empty()


def reverse_string(s):
    """Reverse a string using stack."""
    stack = Stack()
    
    for char in s:
        stack.push(char)
    
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str


if __name__ == "__main__":
    # Example usage
    stack = Stack()
    
    print("Pushing elements:")
    for i in range(1, 6):
        stack.push(i * 10)
    print(f"Stack: {stack}")
    print(f"Size: {stack.size()}")
    
    print("\nPeek top element:")
    print(f"Top: {stack.peek()}")
    
    print("\nPopping elements:")
    print(f"Popped: {stack.pop()}")
    print(f"Stack: {stack}")
    
    print("\n--- Balanced Parentheses ---")
    expressions = ["(())", "(()", "{[()]}", "{[(])}"]
    for expr in expressions:
        print(f"{expr}: {is_balanced_parentheses(expr)}")
    
    print("\n--- String Reversal ---")
    text = "Hello World"
    print(f"Original: {text}")
    print(f"Reversed: {reverse_string(text)}")
