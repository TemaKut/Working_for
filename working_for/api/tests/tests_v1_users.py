from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from users.models import User
from .source import create_all_role_users


class UsersTest(APITestCase):
    """ Тестирование эндпоинта api/v1/users/ """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        create_all_role_users()

        cls.admin = APIClient()
        cls.employer = APIClient()
        cls.applicant = APIClient()

        cls.admin.force_authenticate(
            user=User.objects.get(username='admin'),
            )
        cls.employer.force_authenticate(
            user=User.objects.get(username='employer'),
            )
        cls.applicant.force_authenticate(
            user=User.objects.get(username='applicant'),
            )

        cls.admin_user_id = User.objects.get(username='admin').id
        cls.employer_user_id = User.objects.get(username='employer').id
        cls.applicant_user_id = User.objects.get(username='applicant').id

    def test_200_for_all_users_and_anonym_get_users_list(self):
        """ Анонимный пользователь и админ получают список пользователей. """
        request = self.admin.get(reverse('api_v1:users-list'))
        self.assertEqual(
            request.status_code,
            status.HTTP_200_OK,
            'У админа должен быть статус 200',
        )

        request = self.employer.get(reverse('api_v1:users-list'))
        self.assertEqual(
            request.status_code,
            status.HTTP_200_OK,
            'У работодателя должен быть статус 200',
        )

        request = self.applicant.get(reverse('api_v1:users-list'))
        self.assertEqual(
            request.status_code,
            status.HTTP_200_OK,
            'У соискателя должен быть статус 200',
        )

        request = self.client.get(reverse('api_v1:users-list'))
        self.assertEqual(
            request.status_code,
            status.HTTP_200_OK,
            'У анонима должен быть статус 200',
        )

    def test_admin_can_chenge_self_data(self):
        """ Админ может менять свои данные. """
        admin_name = User.objects.get(username='admin').first_name
        self.assertEqual(admin_name, '')

        response = self.admin.patch(
            reverse(
                'api_v1:users-detail',
                kwargs={'pk': str(self.admin_user_id)}
            ),
            data={'first_name': 'chenged_name'},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        admin_name = User.objects.get(username='admin').first_name
        self.assertEqual(admin_name, 'chenged_name')

    def test_employer_can_chenge_self_data(self):
        """ Работодатель может менять свои данные. """
        employer_name = User.objects.get(username='employer').first_name
        self.assertEqual(employer_name, '')

        response = self.employer.patch(
            reverse(
                'api_v1:users-detail',
                kwargs={'pk': str(self.employer_user_id)}
            ),
            data={'first_name': 'chenged_name'},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        employer_name = User.objects.get(username='employer').first_name
        self.assertEqual(employer_name, 'chenged_name')

    def test_applicant_can_chenge_self_data(self):
        """ Соискатель может менять свои данные. """
        applicant_name = User.objects.get(username='applicant').first_name
        self.assertEqual(applicant_name, '')

        response = self.applicant.patch(
            reverse(
                'api_v1:users-detail',
                kwargs={'pk': str(self.applicant_user_id)}
            ),
            data={'first_name': 'chenged_name'},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        applicant_name = User.objects.get(username='applicant').first_name
        self.assertEqual(applicant_name, 'chenged_name')

    def test_admin_can_chenge_data_of_any_users(self):
        """ Администратор может менять информацию о любых пользователях. """
        employer_name = User.objects.get(username='employer').first_name
        self.assertEqual(employer_name, '')

        response = self.admin.patch(
            reverse(
                'api_v1:users-detail',
                args=(str(self.employer_user_id))
            ),
            data={'first_name': 'chenged_FN'},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('first_name'), 'chenged_FN')

        applicant_name = User.objects.get(username='applicant').first_name
        self.assertEqual(applicant_name, '')

        response = self.admin.patch(
            reverse(
                'api_v1:users-detail',
                args=(str(self.applicant_user_id))
            ),
            data={'first_name': 'chenged_FN'},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('first_name'), 'chenged_FN')

    def test_applicant_not_can_chenge_data_of_another_users(self):
        """ Соискатель не может менять информацию о других юзерах. """
        response = self.applicant.patch(
            reverse('api_v1:users-detail', args=(str(self.employer_user_id))),
            data={'first_name': 'chenged_FN'},
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.applicant.patch(
            reverse('api_v1:users-detail', args=(str(self.admin_user_id))),
            data={'first_name': 'chenged_FN'},
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_employer_not_can_chenge_data_of_another_users(self):
        """ Соискатель не может менять информацию о других юзерах. """
        response = self.employer.patch(
            reverse('api_v1:users-detail', args=(str(self.applicant_user_id))),
            data={'first_name': 'chenged_FN'},
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.employer.patch(
            reverse('api_v1:users-detail', args=(str(self.admin_user_id))),
            data={'first_name': 'chenged_FN'},
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_paginations(self):
        """ Работа паджинации. """
        for i in range(30):
            User.objects.create(
                username=f'test_user_{i}',
                password='12345678',
                email=f'test_user_{i}@mail.ru',
            ),

        response = self.applicant.get(
            reverse('api_v1:users-list') + '?offset=0'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 15)

        response = self.applicant.get(
            reverse('api_v1:users-list') + '?offset=30'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 3)
