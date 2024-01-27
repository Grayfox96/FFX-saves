from os import scandir

TEXT_CHARACTERS = {
    48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7',
    56: '8', 57: '9', 58: ' ', 59: '!', 60: '"', 61: '#', 62: '$', 63: '%',
    64: '&', 65: "'", 66: '(', 67: ')', 68: '*', 69: '+', 70: ',', 71: '-',
    72: '.', 73: '/', 74: ':', 75: ';', 76: '<', 77: '=', 78: '>', 79: '?',
    80: 'A', 81: 'B', 82: 'C', 83: 'D', 84: 'E', 85: 'F', 86: 'G', 87: 'H',
    88: 'I', 89: 'J', 90: 'K', 91: 'L', 92: 'M', 93: 'N', 94: 'O', 95: 'P',
    96: 'Q', 97: 'R', 98: 'S', 99: 'T', 100: 'U', 101: 'V', 102: 'W',
    103: 'X', 104: 'Y', 105: 'Z', 106: '[', 107: '\\', 108: ']', 109: '^',
    110: '_', 111: '`', 112: 'a', 113: 'b', 114: 'c', 115: 'd', 116: 'e',
    117: 'f', 118: 'g', 119: 'h', 120: 'i', 121: 'j', 122: 'k', 123: 'l',
    124: 'm', 125: 'n', 126: 'o', 127: 'p', 128: 'q', 129: 'r', 130: 's',
    131: 't', 132: 'u', 133: 'v', 134: 'w', 135: 'x', 136: 'y', 137: 'z',
    138: '{', 139: '|', 140: '}'
    }


def character_to_id(character: str) -> int:
    for id, textcharacter in TEXT_CHARACTERS.items():
        if character == textcharacter:
            return id
    raise ValueError(f'Not possible to write character {character}')


def write_string(new_string: str, filename: str) -> None:
    """writes the string in the file at the correct offset"""
    if len(new_string) >= 32:
        raise ValueError(f'too many characters: {len(new_string)}')
    ids = ([character_to_id(c) for c in new_string]
           + ([0] * (32 - len(new_string))))

    with open(filename, 'r+b') as f:
        f.seek(37920)
        f.write(bytes(ids))


def read_all_strings(filename: str,
                     start: int = 0,
                     stop: int | None = None,
                     ) -> list[tuple[int, int, str]]:
    """finds all strings present in the file, from start to stop"""
    if stop is None:
        stop = len(file_bytes)

    with open(filename, 'r+b') as f:
        file_bytes = f.read()
    strings = []
    index = start
    while index < stop:
        byte = file_bytes[index]
        if byte not in TEXT_CHARACTERS:
            index += 1
            continue
        string = ''
        start = index
        while byte in TEXT_CHARACTERS:
            string += TEXT_CHARACTERS[byte]
            index += 1
            byte = file_bytes[index]
        if len(string) > 1:
            strings.append((start, start + len(string), string))
    return strings


def main() -> None:
    filenames = [f.path for f in scandir('saves')]
    padding = max(len(f) for f in filenames)

    with open('saves_names.txt') as saves_names_file:
        strings = saves_names_file.read().splitlines()

    for filename, string in zip(filenames, strings):
        old_name = read_all_strings(filename, 37920, 37920 + 32)[0][2]
        if old_name == string:
            print(f'{filename:{padding}} -> {old_name:32} -> (not renamed)')
            continue
        try:
            write_string(string, filename)
        except Exception as error:
            print(f'{filename:{padding}} -> {old_name:32} -> Error: {error}')
            continue
        new_name = read_all_strings(filename, 37920, 37920 + 32)[0][2]
        print(f'{filename:{padding}} -> {old_name:32} -> {new_name}')
    input('Press enter to exit...')


if __name__ == '__main__':
    main()
