from __future__ import annotations

from typing import Union
from functools import reduce

# _INPUT_FILE_NAME = 'sample-input.txt'
_INPUT_FILE_NAME = 'input.txt'


class Number:
    def __init__(self):
        self._parent = None

    def copy(self):
        raise ValueError('Unable to copy abstract class')

    @classmethod
    def from_str(cls, s):
        lst = eval(s)
        return cls.from_list(lst)

    @classmethod
    def from_list(cls, lst):
        if type(lst) == int:
            return Regular(lst)
        elif type(lst) == list:
            return Pair(
                cls.from_list(lst[0]),
                cls.from_list(lst[1]),
            )

    def to_list(self):
        return []

    def _link_parent(self, parent: Union[Number, None]):
        self._parent = parent

    def __str__(self):
        lst = self.to_list()
        return str(lst).replace(' ', '')

    def check_explosions(self, height):
        return None

    def value(self):
        raise ValueError('Not a regular')

    def exec_split(self):
        raise ValueError('Not a regular')

    def is_regular(self):
        return False

    def check_splits(self):
        return None

    @classmethod
    def add(cls, n1: Number, n2: Number):
        n = Pair(n1.copy(), n2.copy())

        while n.reduce_tree():
            pass

        return n

    def magnitude(self):
        return 0


class Regular(Number):
    def __init__(self, value: int):
        super().__init__()
        self._value = value

    def copy(self):
        return Regular(self._value)

    def to_list(self):
        return self._value

    def check_explosions(self, height):
        return None

    def value(self):
        return self._value

    def is_regular(self):
        return True

    def check_splits(self):
        return self if self._value >= 10 else None

    def exec_split(self):
        value = self._value
        left_val = value // 2
        right_val = left_val + (value % 2)
        new_node = Pair(Regular(left_val),
                        Regular(right_val))

        parent_node = self._parent
        if parent_node.left == self:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
        new_node._link_parent(parent_node)

    def magnitude(self):
        return self._value


class Pair(Number):
    def __init__(self,
                 left: Number,
                 right: Number):
        super().__init__()
        self.left = left
        self.right = right
        self.left._link_parent(self)
        self.right._link_parent(self)

    def copy(self):
        copy_left = self.left.copy()
        copy_right = self.right.copy()
        return Pair(copy_left, copy_right)

    def to_list(self):
        return [self.left.to_list(), self.right.to_list()]

    def reduce_tree(self):
        exploded = self.explode_tree()
        if exploded:
            return True
        splitted = self.split_tree()
        return splitted

    def explode_tree(self):
        node = self.check_explosions()
        if node is None:
            return False
        node.exec_explosion()
        return True

    def split_tree(self):
        node = self.check_splits()
        if node is None:
            return False
        node.exec_split()
        return True

    def check_splits(self):
        left = self.left.check_splits()
        if left is not None:
            return left
        right = self.right.check_splits()
        return right

    def check_explosions(self, height=0):
        regular_childs = self.left.is_regular() and self.right.is_regular()
        if height >= 4 and regular_childs:
            return self
        else:
            left_check = self.left.check_explosions(height + 1)
            if left_check is not None:
                return left_check
            else:
                right_check = self.right.check_explosions(height + 1)
                return right_check

    def exec_explosion(self):
        # left explosion
        left_value = self.left.value()
        current_node = self
        parent_node = self._parent
        while parent_node.left == current_node:
            parent_node = parent_node._parent
            current_node = current_node._parent
            if parent_node is None:
                break
        if parent_node is not None:
            target_node = parent_node.left
            while not target_node.is_regular():
                target_node = target_node.right
            target_node._value += left_value

        # right explosion
        right_value = self.right.value()
        current_node = self
        parent_node = self._parent
        while parent_node.right == current_node:
            parent_node = parent_node._parent
            current_node = current_node._parent
            if parent_node is None:
                break
        if parent_node is not None:
            target_node = parent_node.right
            while not target_node.is_regular():
                target_node = target_node.left
            target_node._value += right_value

        node_to_remove = self
        parent_node = node_to_remove._parent
        new_node = Regular(0)
        if parent_node.left == node_to_remove:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
        new_node._link_parent(parent_node)

    def magnitude(self):
        left = self.left.magnitude() * 3
        right = self.right.magnitude() * 2
        res = left + right
        return res


def usecase(filename, expected_number: str, expected_mag: Union[int, None]):
    with open(filename, 'r') as input_file:
        numbers = [Number.from_str(line.strip()) for line in input_file]
    numbersum = reduce(lambda x, y: Number.add(x, y), numbers)
    mag = numbersum.magnitude()
    print(numbersum)
    if expected_number is not None:
        assert expected_number == str(numbersum)
    print(mag)
    if expected_mag is not None:
        assert expected_mag == mag
    nb_numbers = len(numbers)
    max_magn = 0
    for i in range(nb_numbers):
        for j in range(nb_numbers):
            if i != j:
                new_nb = Number.add(numbers[i], numbers[j])
                magn = new_nb.magnitude()
                if magn > max_magn:
                    max_magn = magn
    print(max_magn)


def main():
    n1 = [[[[[9, 8], 1], 2], 3], 4]
    assert Number.from_list(n1).to_list() == n1

    n2 = '[[[[[9,8],1],2],3],4]'
    assert Number.from_str(n2).to_list() == n1
    assert str(Number.from_str(n2)) == n2

    n3 = Number.from_str(n2)
    n3.check_explosions()

    n = Number.from_str('[[[[[9,8],1],2],3],4]')
    n.explode_tree()
    assert str(n) == '[[[[0,9],2],3],4]'

    n = Number.from_str('[7,[6,[5,[4,[3,2]]]]]')
    n.explode_tree()
    assert str(n) == '[7,[6,[5,[7,0]]]]'

    n = Number.from_str('[[6,[5,[4,[3,2]]]],1]')
    n.explode_tree()
    assert str(n) == '[[6,[5,[7,0]]],3]'

    n = Number.from_str('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')
    n.explode_tree()
    assert str(n) == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'

    n = Number.from_str('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
    n.explode_tree()
    assert str(n) == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'

    n1 = Number.from_str('[[[[4,3],4],4],[7,[[8,4],9]]]')
    n2 = Number.from_str('[1,1]')
    n = Number.add(n1, n2)

    n1 = Number.from_str('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]')
    n2 = Number.from_str('[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]')
    n = Number.add(n1, n2)
    assert str(n) == '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'

    n1 = Number.from_str('[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]')
    n2 = Number.from_str('[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]')
    n = Number.add(n1, n2)
    assert str(n) == '[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]'

    n1 = Number.from_str('[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]')
    n2 = Number.from_str('[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]')
    n = Number.add(n1, n2)
    assert str(n) == '[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]'

    n1 = Number.from_str('[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]')
    n2 = Number.from_str('[7,[5,[[3,8],[1,4]]]]')
    n = Number.add(n1, n2)
    assert str(n) == '[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]'

    n1 = Number.from_str('[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]')
    n2 = Number.from_str('[[2,[2,2]],[8,[8,1]]]')
    n = Number.add(n1, n2)
    assert str(n) == '[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]'

    n1 = Number.from_str('[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]')
    n2 = Number.from_str('[2,9]')
    n = Number.add(n1, n2)
    assert str(n) == '[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]'

    n1 = Number.from_str('[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]')
    n2 = Number.from_str('[1,[[[9,3],9],[[9,0],[0,7]]]]')
    n = Number.add(n1, n2)
    assert str(n) == '[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]'

    n1 = Number.from_str('[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]')
    n2 = Number.from_str('[[[5,[7,4]],7],1]')
    n = Number.add(n1, n2)
    assert str(n) == '[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]'

    n1 = Number.from_str('[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]')
    n2 = Number.from_str('[[[[4,2],2],6],[8,7]]')
    n = Number.add(n1, n2)
    assert str(n) == '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'

    assert 1384 == Number.from_str('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]').magnitude()
    assert 3488 == Number.from_str('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]').magnitude()

    usecase('sample-input1.txt', '[[[[1,1],[2,2]],[3,3]],[4,4]]', None)
    usecase('sample-input2.txt', '[[[[3,0],[5,3]],[4,4]],[5,5]]', None)
    usecase('sample-input3.txt', '[[[[5,0],[7,4]],[5,5]],[6,6]]', None)
    usecase('sample-input4.txt', '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]', None)
    usecase('sample-input5.txt', '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]', 4140)
    usecase('input.txt', None, None)


if __name__ == '__main__':
    main()
