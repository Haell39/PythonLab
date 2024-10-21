from enum import Enum

class Quality(Enum):
    LOW: int = 480
    MEDIUM: int = 1080
    HIGH: int = 1440

class Privacy(Enum):
    PRIVATE: str = 'Private'
    UNLISTED: 'Unlisted'
    PUBLIC: 'Public'

def uploud(file: str, quality: Quality, privacy: Privacy) -> None:
    print(f'Uploading: "{file})" in {quality.value}p ({privacy.value})')

def main() ->  None:
    uploud('rex.mp4', Quality.HIGH, Privacy.PUBLIC)

if __name__ == '__main__':
    main()