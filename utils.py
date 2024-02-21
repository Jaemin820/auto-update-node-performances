import time
import logging
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

logging.info('Config selenuim chrom options')
# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # Headless 모드 활성화
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 크롬드라이버 실행
driver = webdriver.Chrome(options=chrome_options)

def get_drive_values(url, times, *class_name):
    logging.info('Getting nodes performance information')
    try:
        driver.get(url)
        time.sleep(times)
        if len(class_name) > 1:
            list_value = {}
            for name in class_name:
                value = driver.find_elements(By.CLASS_NAME, name)
                value_list = [i.text for i in value]
                list_value[name] = value_list
            return list_value
        value = driver.find_elements(By.CLASS_NAME, class_name[0])
        value_list = [i.text for i in value]
        logging.info('Nodes performance information successfully geted.')
        return value_list
    except Exception as e:
        logging.error(f'Error getting nodes performance information: {e}')
        sys.exit(1)
