import re
from collections import OrderedDict


def get_words_stdin():
    try:
        n = int(input())
    except UnicodeDecodeError:
        print("Utf-8 encoding required")
    except ValueError:
        print("No number in first line as expected")
    else:
        for _ in range(n):
            yield input()


def file_output(data):
    with open("result.txt", 'w', encoding='utf-8') as f:
        for _, value in data.items():
            if len(value) > 1:
                print(*value, file=f)


def formatted_output(data):
    for _, value in data.items():
        if len(value) > 1:
            print(*value)


def get_anagramms(result_dict):
    for item in get_words_stdin():
        word = re.findall(r'[а-яёa-z-]+', item.lower())
        if len(word) == 2:
            raise Exception("No valid word: {}".format(item))
        key = "".join(sorted(*word))
        if key not in result_dict:
            result_dict[key] = word
        else:
            result_dict[key].append(*word)


def main():
    result = OrderedDict()
    get_anagramms(result)
    file_output(result)


if __name__ == '__main__':
    main()
