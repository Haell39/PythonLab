from enum import Enum

class Quality(Enum):
    LOW = 480
    MEDIUM = 1080
    HIGH = 1440

class Privacy(Enum):
    PRIVATE = 'Private'
    UNLISTED = 'Unlisted'
    PUBLIC = 'Public'

def upload(file: str, *, quality: Quality, privacy: Privacy) -> None: # With the asteristic, now the coder is obligated to user q arguments
    print(f'Uploading: "{file}" in {quality.value}p ({privacy.value})')

def main() -> None:
    upload('rex.mp4', quality=Quality.MEDIUM, privacy=Privacy.PRIVATE)
    # uploud('rex.mp4', Quality.HIGH, Privacy.PUBLIC) can not do this becaus of the *

if __name__ == '__main__':
    main()