import pandas as pd from src.whatsapp_engine import WhatsAppAutomator from src.data_handler import load_contact_data import time

def run_outreach(): # 1. Load Data from Excel # Expected columns: 'Number', 'Name', 'Tailored_Text', 'Media_Path' df = load_contact_data('contacts.xlsx') generic_msg = "Happy Birthday to"

# 2. Initialize Automator
driver = WhatsAppAutomator()
driver.open_whatsapp()

print("Please scan QR code if not logged in...")
time.sleep(15) # Buffer for login

# 3. Process Broadcast
for index, row in df.iterrows():
    personalized_msg = f"{generic_msg} {row['Name']}! {row['Tailored_Text']}"
    full_number = str(row['Number'])
    
    # Navigate and Send
    driver.send_message(full_number, personalized_msg, row.get('Media_Path'))
    print(f"Sent to: {row['Name']}")
    time.sleep(2) # Anti-ban jitter

# 4. Export Current Lists (Bonus Feature)
contacts = driver.export_chat_lists()
pd.DataFrame(contacts).to_excel('exported_whatsapp_lists.xlsx')

driver.quit()


if name == "main": run_outreach()