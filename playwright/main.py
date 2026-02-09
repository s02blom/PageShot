#!/usr/bin/env python3
import sys
from playwright.sync_api import sync_playwright

def screenshot(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path="playwright_screenshot.png", full_page=True)
        browser.close()
    return "playwright_screenshot.png"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
        sys.exit(1)
    
    result = screenshot(sys.argv[1])
    print(f"Screenshot saved to {result}")
