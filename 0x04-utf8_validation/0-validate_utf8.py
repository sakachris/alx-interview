#!/usr/bin/python3
''' 0-validate_utf8.py '''


def validUTF8(data):
    def get_byte_count(first_byte):
        if first_byte & 0b11110000 == 0b11110000:
            return 4
        elif first_byte & 0b11100000 == 0b11100000:
            return 3
        elif first_byte & 0b11100000 == 0b11000000:
            return 2
        else:
            return 1

    i = 0
    n = len(data)

    while i < n:
        current_byte = data[i]

        # Number of bytes in the current UTF-8 character
        span = get_byte_count(current_byte)

        if span == 1:
            # Single-byte character
            if current_byte > 0x7F:
                return False
        else:
            # Multi-byte character
            if n - i < span:
                return False

            for j in range(i + 1, i + span):
                if not (0x80 <= data[j] <= 0xBF):
                    return False

            i += span - 1

        i += 1

    return True
