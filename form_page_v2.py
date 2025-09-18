from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class FormPageV2:
    URL = "https://practice-automation.com/form-fields/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def fill_form(self, data):
        self.wait.until(EC.visibility_of_element_located((By.ID, "name-input"))).send_keys(data["name"])
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))).send_keys(data["password"])
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"input[name='fav_drink'][value='{data['drink']}']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"input[name='fav_color'][value='{data['color']}']"))).click()
        
        automation_select = self.wait.until(EC.visibility_of_element_located((By.ID, "automation")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", automation_select)
        
        # Используем JavaScript для установки значения выпадающего списка
        self.driver.execute_script(f"arguments[0].value = '{data['automation']}';", automation_select)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", automation_select)
        
        self.wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(data["email"])
        self.wait.until(EC.visibility_of_element_located((By.ID, "message"))).send_keys(data["message"])

    def submit(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        # Используем JavaScript для клика, чтобы избежать перекрытия элементов
        self.driver.execute_script("arguments[0].click();", btn)

    def is_success_alert_present(self):
        try:
            self.wait.until(EC.alert_is_present())
            return True
        except Exception:
            return False

    def close_alert(self):
        self.driver.switch_to.alert.accept()