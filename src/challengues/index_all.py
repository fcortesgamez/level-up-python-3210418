def index_all(search_list, item):
    indices = []
    for index, value in enumerate(search_list):
        if value == item:
            indices.append([index])
        elif isinstance(value, list):
            for i in index_all(value, item):
                indices.append([index] + i)
    return indices