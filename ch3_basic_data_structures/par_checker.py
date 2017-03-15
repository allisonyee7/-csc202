from linear_adts import Stack


def par_checker(symbol_str):
    """
    Check argument string for balanced paranthesis
      >>> par_checker('(())')
      True
      >>> par_checker('())')
      (False, 'Cannot begin parentheses with ")"')
      >>> par_checker('((())')
      (False, 'Parentheses are not closed')
      >>> par_checker('(3 + 5)')
      True
      >>> par_checker('(3 + 5) * (5 * (7 - 4))')
      True
      >>> par_checker('(3 + 5) * (5 * ((7 - 4))')
      (False, 'Parentheses are not closed')
      >>> par_checker(')(')
      (False, 'Cannot begin parentheses with ")"')
    """
    s = Stack()
    index = 0

    while index < len(symbol_str):
        symbol = symbol_str[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if symbol != '(' and symbol != ')':
                None
            elif s.is_empty():
                return False, 'Cannot begin parentheses with ")"'
            else:
                s.pop()
        index += 1
    if s.is_empty() == False:
        return False, 'Parentheses are not closed'
    return s.is_empty()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
