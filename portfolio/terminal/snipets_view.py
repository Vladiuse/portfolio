import os
import json

def drop_html_format(string):
    print(string, string.endswith('.html') and string.count('.') == 2)
    if string.endswith('.html') and string.count('.') == 2:
        string = string.split('.')[:-1]
        string = '.'.join(string)
    return string

def get_structure_of_templates(path, obj, relpath=''):
    objects_in_dir = os.listdir(path)
    objects_in_dir.sort()
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            file_size = os.path.getsize(item_path)
            file_path  = os.path.relpath(item_path, relpath)
            file_data = {
                'size': str(file_size) + ' bytes',
                'path': file_path,
            }
            item = drop_html_format(item)
            obj.update({item: file_data})
        else:
            item = item + '/'
            if not item in obj:
                obj.update({item: {}})
            get_structure_of_templates(item_path, obj[item], relpath)


def get_templates(to_json=True):
    ROOT = '/'
    DIR = {
        ROOT: {}
    }
    path = 'terminal/templates/terminal/files'
    relpath = 'terminal/templates/'
    get_structure_of_templates(path, DIR[ROOT], relpath=relpath)
    if to_json:
        return json.dumps(DIR)
    return DIR