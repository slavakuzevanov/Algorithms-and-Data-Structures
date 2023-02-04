'''
RUS: Для решения данной задачи идеально подходит структура данных -- СТЭК.
Идея решения в следующем: Решаем задачу единственным проходом по массиву скобок. Если на шаге встречаем
открывающую скобку, то добавляем её в СТЭК. Если встречаем закрывающую скобку, то смотрим на последний элемент в стэке.
Если ВИД скобки совпадает, то удаляем открывающую скобку из СТЭКа. Если же ВИД скобок не совпадает, то останавливаем
програму, так как встречена ошибка.
В python реализовать структуру данных СТЕК можно с помощью list.
Здесь, вместо операции push() можно использовать append() для добавления элемента в коннец СТЕКа.
Использование метода pop() также удаляет последний добавленный элемент в массив.

Функции, связанные со стеком:
empty() — возвращает, пуст ли стек — временная сложность: O(1)
size() — возвращает размер стека — временная сложность: O(1)
top() / peek() — возвращает ссылку на самый верхний элемент стека — временная сложность: O(1)
push(a) — вставляет элемент «a» в верхнюю часть стека — временная сложность: O(1)
pop() — удаляет самый верхний элемент стека — временная сложность: O(1)

ENG: The data structure STACK is ideal for solving this problem.
The idea of the solution is as follows: We solve the problem with a single pass through the array of brackets.
If we meet on the step opening bracket, then add it to the STACK. If we meet a closing bracket, then we look at the last
element on the stack. If the TYPE of the bracket matches, then remove the opening bracket from the STACK.
If the type of brackets does not match, then stop program because an error has been encountered.
Python’s built-in data structure list can be used as a stack. Instead of push(), append() is used to add elements
to the top of the stack while pop() removes the element in LIFO order.

The functions associated with stack are:
empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)
'''

class Stack():

    def __init__(self):
        self.list = []

    def empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.list)

    def top(self):
        return self.list[-1]

    def push(self, a):
        self.list.append(a)

    def pop(self):
        return self.list.pop()


# Task Solution

bracket_sequence = input()
stack = Stack()


def isBalanced(bracket_sequence: str) -> str or int:
    for i in range(1, len(bracket_sequence)+1):
        elem = bracket_sequence[i-1]
        if elem in {'(', '[', '{'}:
            stack.push(elem)
        elif elem not in {')', ']', '}'}:
            continue
        elif stack.empty():
            return i
        else:
            top = stack.pop()
            if (elem == ')' and top != '(') \
                    or (elem == ']' and top != '[') \
                    or (elem == '}' and top != '{'):
                return i
    if stack.empty():
        return 'Success'
    else:
        return i


print(isBalanced(bracket_sequence))
