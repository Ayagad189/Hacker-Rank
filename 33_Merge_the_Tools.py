def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        t = ""
        for char in substring:
            if char not in t:
                t += char
        print(t)

if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)
