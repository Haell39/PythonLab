# Docsctring documentation
# Just use '''''' under the function and open the quotes and the docstring will appear automatically

def get_users() -> dict[int, str]:
    """
    Retrieves the ids and usernames from a database as a dict.

    :return: dict [int, str]
    """

    users: dict[int, str] = {1: "Bob", 2: "Jef", 3: "Tom"}
    return users

def display_users(users: dict[int, str]) -> None:
    """
    Prints each user the console in a nice format.

    :param users: the users to display
    :return:
    """
    for k, v in users.items():
        print(k, v, sep=": ")

def main() -> None:
    users: dict[int, str] = get_users() # hoover here to get more details from the docstring
    display_users(users)

if __name__ == "__main__":
    main()