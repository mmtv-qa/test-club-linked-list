class List:

    def __init__(self):
        self._head = None
        self._length = 0

    class Node:

        def __init__(self, data):
            self._data = data
            self._next = None

        def get_data(self):
            return self._data

        def get_next(self):
            return self._next

        def add_link(self, link):
            self._next = link

    def add(self, data):
        new_node = self.Node(data)

        if self._head is None:
            self._head = new_node
            self._length += 1
        else:
            node = self._head
            while node.get_next() is not None:
                node = node.get_next()

            node.add_link(new_node)
            self._length += 1

    def get(self, index):
        if index < self._length and index != self._length:
            i = 0
            node = self._head
            while i <= index:
                if i == index:
                    return node.get_data()
                i += 1
                node = node.get_next()
        else:
            return 'Not found'

    def delete(self, index):
        head = self._head
        if self._head is not None:
            match index:
                case 0:
                    self._head = head.get_next()
                    self._length -= 1
                case range(1, self._length):
                    i = 1
                    last_node = head
                    head = head.get_next()
                    while i <= index:
                        if i == index:
                            last_node.add_link(head.get_next())
                            self._length -= 1
                        i += 1
                        last_node = head
                        head = head.get_next()
                case _:
                    print('Wrong index')
        else:
            print('List is empty')

    # def get_length(self) -> int:
    #     return self._length


# if __name__ == '__main__':
#     l = List()
#     l.add(1)
#     l.add(2)
#     l.add(3)
#     print(l.get(3))
#     print(l.get(2))
#     l.delete(2)
#     print(l.get(2))