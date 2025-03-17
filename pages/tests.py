from django.test import SimpleTestCase

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        # Test if the homepage URL returns a 200 status code
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
class AboutPageTests(SimpleTestCase):
    def test_about_page(self):
        # Test if the about page URL returns a 200 status code
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
