from django.http import HttpRequest
from django.test import TestCase

from .utils import TestUser
from ..validators import is_superuser, is_staff, is_authenticated, is_anonymous, user_has_permission


class ValidatorsTestCase(TestCase):
    """
    Validators test
    """

    def setUp(self):
        """
        Setup the test.
        """
        self.request = HttpRequest()
        self.request.path = '/'

    def test_is_superuser(self):
        self.request.user = TestUser(authenticated=True, superuser=True)
        self.assertTrue(is_superuser(self.request))

    def test_is_staff(self):
        self.request.user = TestUser(authenticated=True, staff=True)
        self.assertTrue(is_staff(self.request))

    def test_is_authenticated(self):
        self.request.user = TestUser(authenticated=True)
        self.assertTrue(is_authenticated(self.request))

    def test_is_anonymous(self):
        self.request.user = TestUser()
        self.assertTrue(is_anonymous(self.request))

    def test_user_has_permission(self):
        self.request.user = TestUser(authenticated=True)
        self.request.user.add_perm("test_permission")
        self.assertTrue(user_has_permission(self.request, "test_permission"))
