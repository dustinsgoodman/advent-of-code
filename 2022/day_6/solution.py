"""Solution to Day 6"""

MARKER_LENGTH = 4
MESSAGE_LENGTH = 14


def are_char_distinct(sequence):
    """Check if a sequence is the marker"""
    return len(set(sequence)) == len(sequence)


def main():
    """Program main"""
    with open('input.txt', encoding="utf8") as file:
        datastream = file.readline().strip()

        for idx in range(0, len(datastream) - MARKER_LENGTH):
            if are_char_distinct(datastream[idx:idx + MARKER_LENGTH]):
                break

        print('MARKER AT', idx + MARKER_LENGTH)

        for idx in range(0, len(datastream) - MESSAGE_LENGTH):
            if are_char_distinct(datastream[idx:idx + MESSAGE_LENGTH]):
                break

        print('MESSAGE AT', idx + MESSAGE_LENGTH)


main()
