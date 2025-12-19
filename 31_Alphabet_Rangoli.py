def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lines = []
    width = 4 * size - 3

    for i in range(size):
        chars = '-'.join(alpha[size-1:i:-1] + alpha[i:size])
        lines.append(chars.center(width, '-'))

    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
