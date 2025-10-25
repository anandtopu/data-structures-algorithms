from collections import deque


def levelOrderMarker(root):
    if not root:
        return []

    queue = deque([root, None])
    result = []
    level = []

    while queue:
        node = queue.popleft()

        if node is None:
            result.append(level)
            level = []
            if queue:
                queue.append(None)
        else:
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def levelOrderTwoQueues(root):
    if not root:
        return []

    current_queue = deque([root])
    next_queue = deque()
    result = []
    level = []

    while current_queue:
        node = current_queue.popleft()
        level.append(node.val)

        if node.left:
            next_queue.append(node.left)
        if node.right:
            next_queue.append(node.right)

        if not current_queue:
            result.append(level)
            level = []
            current_queue, next_queue = next_queue, deque()

    return result




def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


def levelOrderDFS(root):
    result = []

    def dfs(node, level):
        if not node:
            return
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result