# Сложность Q(n)
# Инициализируем счетчик для того чтобы понимать когда нужно записывать символы
# Идем по каждому символу из s
# Если скобка ) то счетчик уменьшается
# Если счетчик больше 1, то есть уже есть одна открытая скобка, то записывается все, что внутри нее.
# Если скобка (, то счетчки увеличивается
def removeOuterParentheses(s):
    res = []
    cnt = 0
    for i in s:
        if i == ')':
            cnt -= 1
        if cnt >= 1:
            res.append(i)
        if i == '(': cnt += 1
    return ''.join(res)

print(removeOuterParentheses('(()())(())(()(()))'))