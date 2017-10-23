class Element:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        rep = str(self.value) + '('
        try:
            rep += 'l=' + str(self.left.value)
        except:
            pass
        try:
            rep += 'r=' + str(self.right.value)
        except:
            pass
        rep += ')'
        return rep


def get_binary_list(n):
    """
    Returns a list of 0 and 1.
    0 means go to the left.
    1 means go to the right.
    The first element is linked
    to the root of the heap.
    """
    if n < 2:
        return []
    if n == 2 or n == 3:
        return [n % 2]
    else:
        return get_binary_list(n / 2) + [n % 2]


def add_child(parent, element, child_side):
    """
    Adds a child element on the correct side of the parent.
    """
    if child_side == 0:
        parent.left = element
    elif child_side == 1:
        parent.right = element


def steal_child(stealer_element, stolen_element):
    """
    Used to change the childs of an element when taking its place.
    """
    try:
        stealer_element.left = stolen_element.left
        try:
            stealer_element.right = stolen_element.right
        except:
            pass
    except:
        pass


def is_divisor_of_2(number):
    if number % 2 == 1 or number == 0:
        return False
    elif number == 2:
        return True
    else:
        return is_divisor_of_2(number / 2)


class Light_heap:
    """
    Simple binary heap with child left and right
    """

    def __init__(self, value=None):
        self.root = value
        if value == None:
            self.length = 0
        else:
            self.length = 1

    def __repr__(self):
        rep = ''
        for i in range(self.length):
            if is_divisor_of_2(i + 1):
                rep += '\n'
            item = self.get_i_element(i + 1)
            rep += item.__repr__()
        return rep

    def add(self, value):
        """
        Add an element at the last place of the heap.
        """
        self.length += 1
        if self.length == 1:
            self.root = Element(value)
        else:
            self.add_w_binary_list(value, self.root, get_binary_list(self.length))

    def add_w_binary_list(self, value, current_element, binary_list):
        """
        Used by add function to recursively find the right parent where to add the element.
        """
        if len(binary_list) == 1:
            add_child(current_element, Element(value), binary_list[0])
        else:
            if binary_list[0] == 0:
                self.add_w_binary_list(value, current_element.left, binary_list[1:])
            elif binary_list[0] == 1:
                self.add_w_binary_list(value, current_element.right, binary_list[1:])

    def pop(self, number=None):
        """
        Robust pop that can return any element.
        If no argument, then it returns the last element.
        """
        if number == None or number == self.length:
            return self.pop_last_element().value
        else:
            last_element = self.pop_last_element()
            return self.pop_w_binary_list(self.root, last_element, get_binary_list(number)).value

    def pop_w_binary_list(self, current_element, replace_element, binary_list):
        """
        Used by pop function to recursively pop the element and its link from its parent.
        """
        parent, child_side = self.get_parent_element_and_side(current_element, binary_list)
        if child_side == 0:
            element = parent.left
            parent.left = replace_element
        elif child_side == 1:
            element = parent.right
            parent.right = replace_element
        steal_child(replace_element, element)
        return element

    def pop_last_element(self):
        """
        Used by pop function to return the last element.
        """
        binary_list = get_binary_list(self.length)
        if len(binary_list) == 0:
            element = self.root
            self.root = None
        elif len(binary_list) == 1:
            if binary_list[0] == 0:
                element = self.root.left
            elif binary_list[0] == 1:
                element = self.root.right
        else:
            parent, child_side = self.get_parent_element_and_side(self.root, binary_list)
            if child_side == 0:
                element = parent.left
                del parent.left
            elif child_side == 1:
                element = parent.right
                del parent.right
        self.length -= 1
        return element

    def get_parent_element_and_side(self, current_element, binary_list):
        """
        Returns the parent and the side (a binary number) of the wanted element.
        """
        if len(binary_list) <= 1:
            print "There is only one element so there is no parent"
            return None
        return self.get_element(current_element, binary_list[:-1]), binary_list[-1]

    def get_element(self, current_element, binary_list):
        """
        Returns the wanted element.
        """
        if len(binary_list) == 0:
            return current_element
        elif binary_list[0] == 0:
            return self.get_element(current_element.left, binary_list[1:])
        elif binary_list[0] == 1:
            return self.get_element(current_element.right, binary_list[1:])

    def get_i_element(self, number):
        """
        Returns the i th element.
        """
        return self.get_element(self.root, get_binary_list(number))


class Light_max_heap(Light_heap):
    """
    Heap that has maximum value at the root.
    """

    def add(self, value):
        """
        Add a new element by carefully respecting the maximum heap property.
        """
        self.length += 1
        if self.length == 1:
            self.root = Element(value)
        elif self.length == 2:
            if self.root.value > value:
                self.root.left = Element(value)
            else:
                element = self.root
                self.root = Element(value)
                self.root.left = element
        elif self.length == 3:
            if self.root.value > value:
                self.root.right = Element(value)
            else:
                element = self.root
                self.root = Element(value)
                self.root.left = element.left
                del element.left
                self.root.right = element
        else:
            if self.root.value < value:
                element = self.root
                self.root = Element(value)
                steal_child(self.root, element)
                self.push_elements_down(element, self.root, get_binary_list(self.length))
            else:
                binary_list = get_binary_list(self.length)
                if binary_list[0] == 0:
                    self.add_w_binary_list(value, self.root, self.root.left, binary_list)
                if binary_list[0] == 1:
                    self.add_w_binary_list(value, self.root, self.root.right, binary_list)

    def add_w_binary_list(self, value, parent, current_element, binary_list):
        """
        Used by add function to recursively find the right parent where to add the element.
        It carefully respect the maximum heap property.
        """
        if len(binary_list) == 1:
            add_child(parent, Element(value), binary_list[0])
        else:
            if binary_list[0] == 0:
                if parent.left.value > value:
                    self.add_w_binary_list(value, parent.left, current_element, binary_list[1:])
                else:
                    element = parent.left
                    parent.left = Element(value)
                    steal_child(parent.left, element)
                    self.push_elements_down(element, parent.left, binary_list[1:])
            elif binary_list[0] == 1:
                if parent.right.value > value:
                    self.add_w_binary_list(value, parent.right, current_element, binary_list[1:])
                else:
                    element = parent.right
                    parent.right = Element(value)
                    steal_child(parent.right, element)
                    self.push_elements_down(element, parent.right, binary_list[1:])

    def push_elements_down(self, current_element, parent, binary_list):
        """
        Push the elements down the heap, until the last place to keep the maximum heap property.
        """
        add_child(parent, current_element, binary_list[0])
        if len(binary_list) > 1:
            parent = current_element
            if binary_list[0] == 0:
                current_element = parent.left
            elif binary_list[0] == 1:
                current_element = parent.right
            steal_child(parent, current_element)
            self.push_elements_down(current_element, parent, binary_list[1:])
        if len(binary_list) == 1:
            try:
                del current_element.left
                try:
                    del current_element.right
                except:
                    pass
            except:
                pass

    def pop_w_binary_list(self, current_element, replace_element, binary_list):
        """
        Used by pop function to recursively pop the element and its link from its parent.
        This version of the function keep the maximum heap property.
        """
        # TODO
        parent, child_side = self.get_parent_element_and_side(current_element, binary_list)
        if child_side == 0:
            element = parent.left
            parent.left = replace_element
        elif child_side == 1:
            element = parent.right
            parent.right = replace_element
        steal_child(replace_element, element)
        return element


def heap_sort(L):
    heap = Light_max_heap()
    for i in range(len(L)):
        heap.add(L[i])
        # print heap
        # print ''
    print test_heap_max(heap)
    # print heap
    NL = []
    for i in range(len(L)):
        a = heap.pop()
        NL.append(a)
    return NL[::-1]


def test_heap_max(heap):
    l = heap.length
    for i in range(l / 2 - 1):
        element = heap.get_i_element(i + 1)
        if element.value < element.left.value or element.value < element.right.value:
            print i
            return False
    if l % 2 == 0:
        element = heap.get_i_element(l / 2)
        if element.value < element.left.value:
            print l / 2
            return False
    else:
        element = heap.get_i_element(l / 2)
        if element.value < element.left.value or element.value < element.right.value:
            print l / 2
            return False
    return True


from random import randrange
import numpy as np

n = 100
m = 1000

a = [randrange(0, m) for _ in range(n)]
b = [randrange(0, m) for _ in range(n * 10)]
c = [randrange(0, m) for _ in range(n * 100)]

heap_sort(a)

print ''