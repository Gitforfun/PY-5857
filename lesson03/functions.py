# def my_print(name):
#     print(f"10.00.2010: {name}")
#
#
# my_print("Artur")
# my_print("Artur")
# my_print("Artur")
# my_print("Artur")


def check_string_length(content='empty'):
    """
    Описание функции
    :param content: описание аргумента
    :return: строка
    """
    if content == 'empty':
        return 'Invalid argument!'

    string_content = str(content)
    content_length = len(string_content)

    # if content_length > 0:
    #     return f'Length is {content_length}'
    # else:
    #     return 'Error'

    return f'Length is {content_length}' if content_length > 0 else 'Error'


result = check_string_length('askdjhaksdjhakjshd')
result = check_string_length()
print(result)
