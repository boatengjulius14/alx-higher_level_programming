def remove_char_at(str, index):
    if index < 0:
        return str
    return str[:index] + str[index + 1:]
