# repo_util.py

def convert_to_string(obj_list, format_string):
    return '\n'.join([format_string.format(*obj) for obj in obj_list])

def convert_from_string(content, split_char, obj_type):
    obj_data = [line.split(split_char) for line in content.split('\n')]
    return [obj_type(*data) for data in obj_data if data]

def get_by_id(obj_list, obj_id):
    for obj in obj_list:
        if obj.id == obj_id:
            return obj
    return None
