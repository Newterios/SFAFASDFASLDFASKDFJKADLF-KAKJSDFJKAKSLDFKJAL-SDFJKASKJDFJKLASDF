#В этом коде учитываеться приоритет () в скобках ((2 + 2)*5) + 3  и тд будет выполняться !

#В вашем ожданий результата 2 + (3*4)- 5/(1+1) ошибка снизу доказателство
#2 + 12 - 5 * 0.5 (Чтобы не путаться в приоритете выполнений мы всегда делим 1 на делител соответственно / на *)
# 14 - 2.5 = 11.5 и бо 14 - 2 - 0.5 == 12 - 0.5 а это 11.5
# Я не стал дововлять ZeroDevisionEror и тд так как не было в заданий да и компилятор будет сам выводит а сами мы догодаемся

# Читайте код начниная с последнего принта и после снизу верх с функцией main !

def to_do_operator(listr: list) -> int:
    slovar_operatorov = {
        "*": (lambda x, y: x * y, 0),
        "/": (lambda x, y: x / y, 0),
        "+": (lambda x, y: x + y, 0),
        "-": (lambda x, y: x - y, 0)
    }
    new_list = listr.copy()
    for i in listr:
        if i in slovar_operatorov:
            slovar_operatorov[i] = (slovar_operatorov[i][0], slovar_operatorov[i][1] + 1)
    for key in slovar_operatorov:
        while slovar_operatorov[key][1] > 0:
            find_key = new_list.index(key)
            resultat = slovar_operatorov[key][0](new_list[find_key - 1], new_list[find_key + 1])
            new_list[find_key - 1:find_key + 2] = [resultat]
            slovar_operatorov[key] = (slovar_operatorov[key][0], slovar_operatorov[key][1] - 1)
    return new_list[0]

def to_do_without(listr: list) -> int:
    needs_reduce = any(isinstance(item, list) for item in listr)
    if needs_reduce:
        new_list = listr.copy()
        for i, item in enumerate(new_list):
            if isinstance(item, list):
                new_list[i] = to_do_without(item)
        return to_do_operator(new_list)
    else:
        return to_do_operator(listr)

def format_list(listr: list) -> list:
    list_to_return = []
    for item in listr:
        if isinstance(item, list):
            if len(item) == 1 and isinstance(item[0], str) and item[0].isdigit(): 
                list_to_return.append(int(item[0]))
            elif len(item) == 1 and not isinstance(item[0], str):
                list_to_return.append(item)
            else:
                list_to_return.append(format_list(item))
        elif isinstance(item, str) and item.isdigit():
            list_to_return.append(int(item))
        else:
            list_to_return.append(item)
    return list_to_return

def to_do_prioritet_list(string: str) -> list:
    nlist = []
    index_last = -1
    for index, char in enumerate(string):
        if index_last != -1 and index <= index_last:
            continue
        if char == ' ':
            continue
        elif char == '(':
            count_of_recursivity = 1
            list_to_append = []
            index_after = index + 1
            try:
                while count_of_recursivity != 0:
                    if index_after == len(string):
                        raise IndexError
                    if string[index_after] == '(':
                        count_of_recursivity += 1
                        list_to_append.append([])
                    elif string[index_after] == ')':
                        count_of_recursivity -= 1
                    elif string[index_after] != ' ':
                        if count_of_recursivity == 1:
                            list_to_append.append(string[index_after])
                        else:
                            list_to_append[-1].append(string[index_after])
                    index_after += 1
                index_last = index_after - 1
                nlist.append(list_to_append)
            except IndexError:
                print(f'В {string} не хватает закрывающей скобки!')
                return to_do_prioritet_list(input("Try again: \n "))
        else:
            nlist.append(char)
    return nlist
def main(string: str) -> int:
    return to_do_without(format_list(to_do_prioritet_list(string)))
print(main(input("Введите выражение, которое может включать +, -, *, / и скобки (): \n")))