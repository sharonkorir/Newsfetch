import unittest
from models import news_articles, news_sources
Source = news_sources.Source 
Article = news_articles.Article

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
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

  
class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_article = Article("bbc-news", "Ukraine's Zelensky asks citizens to resist and Europe to do more", "Ukraine's president tells Europe it has the \"strength to stop this aggression\" and calls for action.", "http://www.bbc.co.uk/news/world-europe-60527346", "https://ichef.bbci.co.uk/news/1024/branded_news/E1CA/production/_123420875_hi074132197.jpg", "2022-02-25T17:22:23.06428Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

    def test_init(self):
        '''
        test_init test case to test if the article object is initialized properly
        '''

        self.assertEqual(self.new_article.source_id, "bbc-news")
        self.assertEqual(self.new_article.title, "Ukraine's Zelensky asks citizens to resist and Europe to do more")
        self.assertEqual(self.new_article.description, "Ukraine's president tells Europe it has the \"strength to stop this aggression\" and calls for action.")
        self.assertEqual(self.new_article.artcle_url,"http://www.bbc.co.uk/news/world-europe-60527346")
        self.assertEqual(self.new_article.image,"https://ichef.bbci.co.uk/news/1024/branded_news/E1CA/production/_123420875_hi074132197.jpg")
        self.assertEqual(self.new_article.time, "2022-02-25T17:22:23.06428Z")

if __name__ == '__main__':
    unittest.main()