import unittest
from models import news_articles, news_sources
Source = news_sources.Source 

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before evry test
        '''
        self.new_source = Source("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "https://abcnews.go.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

    def test_init(self):
        '''
        test_init test case to test if the source object is initialized properly
        '''

        self.assertEqual(self.new_source.id, "abc-news")
        self.assertEqual(self.new_source.name, "ABC News")
        self.assertEqual(self.new_source.description,"Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")
        self.assertEqual(self.new_source.url,"https://abcnews.go.com")
  


if __name__ == '__main__':
    unittest.main()