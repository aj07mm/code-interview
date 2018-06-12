import os
import random
import string


def get_available_name(name, max_length=None):
    file_root, file_ext = os.path.splitext(name)

    while os.path.exists(name) or (max_length and len(name) > max_length):
        rs = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        name = '%s_%s%s' % (file_root, rs, file_ext)
        if max_length is None:
            continue
        truncation = len(name) - max_length
        if truncation > 0:
            file_root = file_root[:-truncation]
            name = '%s_%s%s' % (file_root, rs, file_ext)

return name
