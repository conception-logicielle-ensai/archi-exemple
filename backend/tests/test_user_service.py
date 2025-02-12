from unittest import TestCase
from unittest.mock import MagicMock

from backend.business_object.user import User
from backend.dao.user_dao import UserDAO
from backend.services.user_service import UserService


class TestUserService(TestCase):
    def setUp(self):
        self.user_dao = UserDAO(MagicMock())
        self.user_service = UserService(user_dao=self.user_dao)

    def test_user_valide(self):
        user_valide = User(id=None, username="admin", roles=["admin"])
        self.user_dao.get_user_by_username = MagicMock(return_value=user_valide)
        user = self.user_dao.get_user_by_username()
        self.assertTrue(self.user_service.peut_se_connecter(user=user))

    def test_user_invalide(self):
        user_valide = User(id=None, username="admin", roles=["pas_admin"])
        self.user_dao.get_user_by_username = MagicMock(return_value=user_valide)
        user = self.user_dao.get_user_by_username()
        self.assertFalse(self.user_service.peut_se_connecter(user=user))
