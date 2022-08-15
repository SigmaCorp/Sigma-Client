def retrieve_data(data, field):
    result = data.get(field, "Not found")
    if type(result) is dict:
        return "Not found"
    return str(result)
