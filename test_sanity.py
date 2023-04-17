class TestSanity:

    def test_title(self, browser_setup):
        browser_setup.get("http://www.shai-adani.co.il/practiceForm.html")
        assert "שי עדני – ניהול פרוייקטים, אבטחת איכות, בדיקות תוכנה" in browser_setup.title

    def test_input_exists(self, browser_setup):
        browser_setup.get("http://www.shai-adani.co.il/practiceForm.html")
        input_element = browser_setup.find_element_by_name("fullname")
        assert input_element is not None
        input_element = browser_setup.find_element_by_name("email")
        assert input_element is not None

    def test_submit(self, browser_setup):
        browser_setup.get("http://www.shai-adani.co.il/practiceForm.html")
        submit_button = browser_setup.find_element("name","submit")
        assert submit_button is not None
        submit_button.click()
        success_message = browser_setup.find_element("id","Show SUM")
        assert success_message is not None