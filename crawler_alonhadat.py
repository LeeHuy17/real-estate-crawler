from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from datetime import datetime
import os

def run_crawler():
    print("Bắt đầu thu thập dữ liệu lúc", datetime.now().strftime("%H:%M:%S"))
    all_data = []

    driver = webdriver.Chrome()
    driver.get("https://alonhadat.com.vn/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    city_dropdown = Select(wait.until(EC.presence_of_element_located((By.CLASS_NAME, "province"))))
    city_dropdown.select_by_visible_text("Đà Nẵng")

    type_dropdown = Select(wait.until(EC.presence_of_element_located((By.CLASS_NAME, "demand"))))
    type_dropdown.select_by_visible_text("Cho thuê")

    search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btnsearch")))
    search_button.click()
    time.sleep(3)

    def extract_data():
        titles = driver.find_elements(By.CSS_SELECTOR, ".ct_title a")
        descriptions = driver.find_elements(By.CSS_SELECTOR, ".content .content_description")
        areas = driver.find_elements(By.CSS_SELECTOR, ".ct_dt span")
        prices = driver.find_elements(By.CSS_SELECTOR, ".price")
        addresses = driver.find_elements(By.CSS_SELECTOR, ".address")
        images = driver.find_elements(By.CSS_SELECTOR, ".thumb img")

        for i in range(len(titles)):
            try:
                data = {
                    "Tiêu đề": titles[i].text,
                    "Mô tả": descriptions[i].text if i < len(descriptions) else "",
                    "Diện tích": areas[i].text if i < len(areas) else "",
                    "Giá": prices[i].text if i < len(prices) else "",
                    "Địa chỉ": addresses[i].text if i < len(addresses) else "",
                    "Hình ảnh": images[i].get_attribute("src") if i < len(images) else "",
                    "Link chi tiết": titles[i].get_attribute("href")
                }
                all_data.append(data)
            except Exception as e:
                print(f"Lỗi khi lấy dữ liệu tin số {i}: {e}")

    extract_data()

    while True:
        try:
            next_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, ">>")))
            if "disabled" in next_button.get_attribute("class") or not next_button.is_enabled():
                break
            next_button.click()
            time.sleep(3)
            extract_data()
        except Exception as e:
            print("Kết thúc or lỗi:", e)
            break

    date_str = datetime.now().strftime("%Y-%m-%d")
    file_path = f"D:\\TDH_quytrinh\\real-estate-crawler\\data\\real_estate_data_{date_str}.xlsx"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df = pd.DataFrame(all_data)
    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Đã lưu {len(all_data)} dòng dữ liệu vào {file_path}")

    # Đóng 
    driver.quit()


#Chờ đúng 06:00 để chạy
if __name__ == "__main__":
    print("Đang chờ đến 06:00 để chạy crawler...")

    while True:
        now = datetime.now()
        if now.hour == 23 and now.minute == 18:
            run_crawler()
            time.sleep(70)  
        else:
            time.sleep(30) 
