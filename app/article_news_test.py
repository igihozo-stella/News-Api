import unittest
from models import article_news
News_Article=article_news.News_Article

class NewsArticleTest(unittest.TestCase):
    
    #Test the news article class
    
    def setUp(self):
        
        #Setup method that will run before every test
       
        self.new_article = News_Article('n','k','c','l','emg fgn dfbgn','www.ew.com/','www.ew.com/p.jpg','dae n')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,News_Article))

if __name__ == '__main__':
    unittest.main()