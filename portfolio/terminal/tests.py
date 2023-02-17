from django.test import TestCase

# Create your tests here.


# import os
# from pprint import pprint
# path = 'portfolio/terminal/templates/terminal/files'
# ROOT = '/'
# DIR  = {
#     ROOT: {}
# }

# def create(path, obj):
#     objects_in_dir = os.listdir(path)
#     objects_in_dir.sort()
#     for item in os.listdir(path):
#         item_path = os.path.join(path, item)
#         if os.path.isfile(item_path):
#             file_size = os.path.getsize(item_path)
#             file_data = {
#                 'size': file_size,
#                 'path': item_path,
#             }
#             obj.update({item:file_data})
#         else:
#             item = item + '/'
#             if not item in obj:
#                 obj.update({item:{}})
#             create(item_path, obj[item])

# create(path, DIR[ROOT])
# pprint(DIR)

