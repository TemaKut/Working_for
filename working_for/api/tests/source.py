from users.models import User


def create_all_role_users():
    """ Создать в БД пользователей с разными ролями. (Только для тестов.) """
    User.objects.create(
            username='admin',
            password='admin',
            email='admin@mail.ru',
            role='admin',
    ),
    User.objects.create(
        username='employer',
        password='employer',
        email='employer@mail.ru',
        role='employer',
    ),
    User.objects.create(
        username='applicant',
        password='applicant',
        email='applicant@mail.ru',
        role='applicant',
    ),
