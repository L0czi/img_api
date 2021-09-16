from django.test import TestCase
from api.models import Account
from django.contrib.auth.models import User
# Create your tests here.
class AccountrModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user1 = User.objects.create(username='testuser1', password='testing321')
        self.user2 = User.objects.create(username='testuser2', password='testing321')

        self.account = Account.objects.create(user=self.user1)
        self.account2 = Account.objects.create(user=self.user2, tier='PREMIUM')
        
    def test_default_tier(self):
        account = Account.objects.get(id=1)
        default_value = account.tier
        self.assertEqual(default_value, 'BASIC')

    def test_premium_tier_assigment(self):
        account = Account.objects.get(id=2)
        default_value = account.tier
        self.assertEqual(default_value, 'PREMIUM')

    def test_retuned_name(self):
        account = Account.objects.get(id=1)
        expected_object_name = f"{account.user.username} Account"
        self.assertEqual(str(account), expected_object_name)
