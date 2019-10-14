import unittest
from models import Articles,Sources


class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Articles(1,'tumaa','Kenyan Man breaks world record','Kipchoge breaks the world record on 2 hour marathon','https://techtoday.com','https://marathons.com/images','2019-010-21T14:50:05Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.author,'tumaa')
        self.assertEquals(self.new_article.title,'Kenyan Man breaks world record')
        self.assertEquals(self.new_article.description,'Kipchoge breaks the world record on 2 hour marathon')
        self.assertEquals(self.new_article.url,'https://techtoday.com')
        self.assertEquals(self.new_article.urlToImage,'https://marathons.com/images')
        self.assertEquals(self.new_article.publishedAt,'2019-010-21T14:50:05Z')
if __name__ == '__main__':
    unittest.main()
