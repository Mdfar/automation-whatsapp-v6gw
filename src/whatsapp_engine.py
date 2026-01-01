from selenium import webdriver from selenium.webdriver.common.by import By from selenium.webdriver.common.keys import Keys from selenium.webdriver.chrome.service import Service from webdriver_manager.chrome import ChromeDriverManager import os

class WhatsAppAutomator: def init(self): options = webdriver.ChromeOptions() # Persist session to avoid scanning QR every time options.add_argument(f"user-data-dir={os.getcwd()}/sessions") self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def open_whatsapp(self):
    self.driver.get("[https://web.whatsapp.com](https://web.whatsapp.com)")

def send_message(self, phone, message, media_path=None):
    # Direct URL Link for specific number
    url = f"[https://web.whatsapp.com/send?phone=](https://web.whatsapp.com/send?phone=){phone}&text={message}"
    self.driver.get(url)
    
    try:
        # Wait for send button and click
        send_btn = self.driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        
        if media_path and os.path.exists(media_path):
            self.attach_media(media_path)
        
        send_btn.click()
    except Exception as e:
        print(f"Failed to send to {phone}: {e}")

def attach_media(self, path):
    attachment_btn = self.driver.find_element(By.XPATH, '//div[@title="Attach"]')
    attachment_btn.click()
    image_input = self.driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_input.send_keys(os.path.abspath(path))

def export_chat_lists(self):
    # Logic to scrape the chat sidebar for contact names/numbers
    elements = self.driver.find_elements(By.XPATH, '//div[@id="pane-side"]//span[@title]')
    return [{"ContactName": el.get_attribute("title")} for el in elements]

def quit(self):
    self.driver.quit()