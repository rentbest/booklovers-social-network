def camel_case_to_snake_case(camel_word: str) -> str:
    snake_word = []
    start = True
    for el in camel_word:
        if el == el.upper() and not start:
            snake_word.append("_")
        start = False
        snake_word.append(el.lower())
    return ''.join(snake_word)
