'''
def get_users():
    users: dict[int, str] = {1: "Bob", 2: "Jef", 3: "Tom"}
    return users

def get_users():
    return {1: "Bob", 2: "Jef", 3: "Tom"}

print(get_users())

Obs: doing this two ways is not direct enough if you are just reading the code, its simply not enough context
'''
from urllib.parse import uses_query


# Better way to do

def get_users() -> dict[int, str]:
    """Retorna um dicionário de usuários com IDs e nomes."""
    users: dict[int, str] = {1: "Bob", 2: "Jef", 3: "Tom"}
    return users

def display_users(users: dict[int, str]) -> None:
    """Exibe os usuários no formato 'ID: Nome'."""
    for k, v in users.items():
        print(k, v, sep=": ")

def main() -> None:
    """Função principal que obtém e exibe os usuários."""
    users: dict[int, str] = get_users()
    display_users(users)

if __name__ == "__main__":
    main()