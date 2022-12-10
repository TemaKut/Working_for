import os


def get_upload_path(instance, filename):
    """ Динамический путь сохранения лого юзера. """
    path = f'users/logo/{instance.username}_logo.jpg'

    if os.path.exists('media/' + path):
        os.remove('media/' + path)

    return path
