from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_start_list_and_retrieve_later(self):

        # Opens the homepage
        self.browser.get('http://localhost:8000')

        # The page title and header mention 'To-Do' list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        # Type 'Buy peacock feathers' into text box (for fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # Hit enter, the page updates and shows '1: Buy peacock feathers' as an
        #   item in a to-do list table
        inputbox.send_keys(Keys.ENTER)

        # Page updates, showing that one item in the list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # Add another item to the list: 'Use peacock feathers to make a fly'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # Page updates, showing both items in the list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly',
                      [row.text for row in rows])

        self.fail('Finished the test')

if __name__ == '__main__':

    unittest.main()
