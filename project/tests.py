from django.test import TestCase

# Create your tests here.
class LoginViewTest(TestCase):    

    def test_login_password_not_correct(self):
        print('*****************test_login_password_not_correct()*********************')
        login_account_test_data = {'username': 'admin', 'password': 'qqqqqq'}
        response = self.client.post(path='', data=login_account_test_data)
        print('Response status code : ' + str(response.status_code))
        self.assertEqual(response.status_code, 200)
        # if the provided string exist in the response content html, then pass.
        self.assertIn('Invalid Credential', response.content)
        

    def test_login_success(self):
        print('*****************test_login_success()*********************')
        login_account_test_data = {'username': 'admin', 'password': 'admin'}
        response = self.client.post(path='', data=login_account_test_data)
        self.assertEqual(response.status_code, 200)
        print('Response status code : ' + str(response.status_code))


# class BookingTest(TestCase):

#      def test_booking_success(self):
#         print('*****************test_login_success()*********************')
#         login_account_test_data = {'firstname': 'bikram', 'lastname': 'acharya','address': 'kathmandu', 'room_type': 'delux', 'room_num': '30','checkin': '',}
#         response = self.client.post(path='/room_booked/', data=login_account_test_data)
#         self.assertEqual(response.status_code, 200)
#         print('Response status code : ' + str(response.status_code))
