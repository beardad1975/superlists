from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


#test from a visitor 's point of view

class NewVisitorTest(unittest.TestCase):

    
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('待辦事項',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('待辦事項', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '請輸入一個待辦事項'
        )
        
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('買孔雀羽毛')
        
        
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)

        import time
        #time.sleep(10)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text ==  '1: 買孔雀羽毛' for row in rows),
            "新的待辦事項沒有出現在表上 -- row.text是 :\n%s" % table.text,
        )
        
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('用孔雀羽毛來飛')
        inputbox.send_keys(Keys.ENTER)
             
        # The page updates again, and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn( '1: 買孔雀羽毛' , [row.text for row in rows])
        self.assertIn(
            '2: 用孔雀羽毛來飛',
            [row.text for row in rows]
        )
        
        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail('Finish the test!')

        # She visits that URL - her to-do list is still there.
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')








