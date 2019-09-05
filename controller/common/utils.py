def string_to_array(str_val, separator):
    if not str_val:
        return []
    str_val = str_val.strip()
    if len(str_val) == 0:
        return []
    res = str_val.split(separator)
    res[:] = [res_val.strip() for res_val in res]
    return res
