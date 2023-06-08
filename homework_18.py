def bold(bolding):
    def wrapper(*args, **kwargs):
        result = bolding(*args, **kwargs)
        if isinstance(result, str):
            return "<b>" + result + "</b>"
        return result
    return wrapper
def get_result():
    return "Жирный шрифт"

result = get_result()
print(result)