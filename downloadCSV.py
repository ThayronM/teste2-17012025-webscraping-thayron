# classe downloadCSV:
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class downloadCSV:
    def __init__(self, download_dir, wait):
        self.download_dir = download_dir
        self.wait = wait
        
    def download_csv(self):
        # Esperar e clicar no botão de download
        download_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="data"]/div[2]/div[1]/a[1]')))
        download_button.click()
        print('Download do arquivo CSV inciado para a pasta "downloads"')