from functools import reduce


def map_function(char):
    return ord(char)


def filter_function(number):
    if number > 5:
        return True
    return False


def reduce_function(x, y):
    return x * y


if __name__ == '__main__':
    # List comprehension
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    square_even = [x ** 2 for x in num if x % 2 == 0]
    square_of = [x ** 2 for x in [x ** 2 for x in num if x % 2 == 0]]
    print(square_even)
    print(square_of)

    # Dictionary comprehension
    data_dict = {"Maths": 180, "Physics": 170, "CS": 185, "Chemistry": 175}
    dict1 = {key for key in data_dict.keys()}
    print(dict1)
    dict2 = {value // 2 for value in {value for value in data_dict.values()}}
    print(dict2)
    dict3 = {key: value for key, value in data_dict.items() if value % 2 == 0 if value <= 170}
    print(dict3)

    # Map function
    alphabet = ["a", "b", "c", "d", "e"]
    result = map(map_function, alphabet)
    print(result)
    print(list(result))
    measurements = [{'length': 1, 'width': 2}, {'length': 3, 'width': 4}, {'length': 2, 'width': 1}]
    area = map(lambda x: x.get("length") * x.get("width"), measurements)
    print(list(area))

    # Filter function
    filter_result = filter(filter_function, num)
    print(filter_result)
    print(tuple(filter_result))
    filter_lambda = filter(lambda x: (x < 5), num)
    print(filter_lambda)
    print(list(filter_lambda))

    # Reduce function
    reduce_func = reduce(reduce_function, num)
    print(reduce_func)
    reduce_result = reduce(lambda x, y: (x + y), num)
    print(reduce_result)

    data = map(lambda x: (x + x), filter(lambda x: (x > 4), num))
    print(data)
    print(list(data))
    data1 = filter(lambda x: (x > 5), map(lambda y: (y + y), num))
    print(data1)
    print(list(data1))

    data3 = reduce(lambda x, y: x + y, map(lambda x: (x + x), filter(lambda x: (x > 4), num)))
    print(data3)

    # String manipulation
    word = "Elavarasu Appusamy"
    print(word.capitalize())
    print(word.casefold())
    print(word.count("a"))
    print(word.startswith("E"))
    print(word.endswith("u"))
    print(word.expandtabs())
    print(word.find("l"))
    print(word.index("v"))
    print(word.isalnum())
    print(word.isalpha())
    print(word.isascii())
    print(word.split())

    word_list = ["H", "e", "l", "l", "o"]
    print("".join(word_list))
