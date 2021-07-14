def slice(data, count):
    prefix = data[:count]
    data = data[count:]
    return prefix, data
