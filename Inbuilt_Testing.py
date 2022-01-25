import unittest
from app import app

class BasicTestCase(unittest.TestCase):
    def test_root(self):
            tester = app.test_client(self)
            response = tester.get('/', content_type='html/text')
            self.assertEqual(response.status_code, 200)
    def test_metadata(self):
            tester = app.test_client(self)
            response = tester.get('/metadata', content_type='html/text')
            self.assertEqual(response.status_code, 200)
    def test_health(self):
            tester = app.test_client(self)
            response = tester.get('/health', content_type='html/text')
            self.assertEqual(response.status_code, 200)            

if __name__ == '__main__':
    unittest.main()