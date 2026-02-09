#!/usr/bin/env python3
import sys
from selenium import webdriver

SERVER = "http://localhost:4444/wd/hub"

def screenshot(url, filename):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    with webdriver.Remote(command_executor=SERVER, options=options) as driver:
        driver.get(url)
        driver.save_screenshot(filename)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    filename = "selenium_screenshot.png"
    screenshot(url, filename)
    print(f"Screenshot saved to {filename}")
