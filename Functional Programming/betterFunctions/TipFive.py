
'''
^^ Essa nao é uma ideia sustentavel pois nao da para passar um valor 'D' por exemplo ou excluir o valor 'A' e só passar 'B' e 'C' pois teria que ficar modificando os parametros de def join_text

def join_text(text1: str, text2: str, text3: str, *, sep: str) -> str:
    return sep.join([text1, text2, text3])

def main() -> None:
    print(join_text('A', 'B', 'C', sep='--'))

if __name__ == '__main__':
    main()
'''

def join_text(*strings, sep: str) -> str:
    return sep.join(strings)

def main() -> None:
    print(join_text( 'B', 'C', sep='--'))
    print(join_text('A', 'G', 'K', 'L', 'H', sep='/'))

if __name__ == '__main__':
    main()

