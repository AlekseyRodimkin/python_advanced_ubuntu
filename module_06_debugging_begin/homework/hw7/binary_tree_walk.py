"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход путь до файла с логами
    и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, хранящиеся в бинарном дереве уникальны
"""
import itertools
import logging
import random
from collections import deque
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    """Класс бинарного дерева"""
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    """Обходит все узлы в последовательности дерева и пишет логи"""
    queue = deque([root])  # список узлов в последовательности дерева

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(1, 10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)
    node_right = get_tree(max_depth - 1, level=level + 1)
    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    with open(path_to_log_file, 'r') as file:  # читаем файл с логами
        root_num = int(file.read()[30:36])  # получаем номер узла
        root = BinaryTreeNode(val=root_num, left=None, right=None)  # создаем новое дерево
        queue = deque([root])  # список узлов в последовательности
        tree = {root_num: root}  # словарь с узлами
        for line in file:
            while queue:  # пока есть узлы в последовательности
                if line.startswith('INFO'):
                    node_num = int(line[30:36])
                    tree[node_num] = BinaryTreeNode(node_num)
                    queue.popleft()
                elif line.startswith('DEBUG') and 'right' in line:
                    node_num = int(line[22:28])
                    node = BinaryTreeNode(val=node_num, left=None, right=queue[0])
                    queue.append(node)
                elif line.startswith('DEBUG') and 'left' in line:
                    node_num = int(line[22:28])
                    node = BinaryTreeNode(val=node_num, left=queue[0], right=None)
                    queue.append(node)

    return tree


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename="walk_log_4.txt",
    )

    root = get_tree(7)
    walk(root)
    print(restore_tree("walk_log_4.txt"))
