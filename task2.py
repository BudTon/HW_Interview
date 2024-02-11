class Stack :

    def __init__(self):
        self.items = []

    def is_empty(self):
        return (self.items == [])
    def push(self, item):
        self.items.append(item)

    def pop(self, index):
        return self.items.pop(index)

    def peek(self, index_peek):
        if stack.size() == 0:
            return None
        item = self.items[index_peek-1]
        return item

    def size(self):
        return len(self.items)


def revers_brackets(stack_item):
    if stack_item == ']':
        return '['
    if stack_item == '}':
        return '{'
    if stack_item == ')':
        return '('




def checking_brackets(string_brackets):
    sl = [*string_brackets]
    for el in sl:
        stack.push(el)
    if stack.size()%2 != 0:
        return 'Не сбалансированная последовательность скобок'
    else:
        while not stack.is_empty():
            for stack_item in stack.items:
                if stack_item not in '({[':
                    rev_bracket = revers_brackets(stack_item)
                    index_stack_item = stack.items.index(stack_item)
                    index_stack_item_peek = index_stack_item - 1
                    if rev_bracket == stack.peek(index_stack_item):
                        stack.pop(index_stack_item)
                        stack.pop(index_stack_item_peek)
                        break
                    else:
                        return 'Не сбалансированная последовательность скобок'
    return 'Сбалансированная последовательность скобок'



if __name__ == '__main__':
    stack = Stack()
    '''
    Пример сбалансированных последовательностей скобок:
    '''
    string_brackets_1 = '(((([{}]))))'
    string_brackets_2 = '[([])((([[[]]])))]'
    string_brackets_3 = '{()}'
    string_brackets_4 = '{{[()]}}'

    '''
    Пример несбалансированные последовательности:
    '''
    string_brackets_5 = '}{}'
    string_brackets_6 = '{{[(])]}}'
    string_brackets_7 = '[[{())}]'

    print('string_brackets_1 - ', checking_brackets(string_brackets_1))
    print('string_brackets_2 - ', checking_brackets(string_brackets_2))
    print('string_brackets_3 - ', checking_brackets(string_brackets_3))
    print('string_brackets_4 - ', checking_brackets(string_brackets_4))
    print('string_brackets_5 - ', checking_brackets(string_brackets_5))
    print('string_brackets_6 - ', checking_brackets(string_brackets_6))
    print('string_brackets_7 - ', checking_brackets(string_brackets_7))
