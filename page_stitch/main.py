# https://github.com/petersimeth/selenium-chrome-full-page-screenshot/blob/master/app.py

from selenium import webdriver
from PIL import Image
from io import BytesIO
import time

SERVER = "http://localhost:4444/wd/hub"

def fullpage_screenshot(driver, file, scroll_delay=0.3):
    device_pixel_ratio = driver.execute_script('return window.devicePixelRatio')

    total_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    viewport_height = driver.execute_script('return window.innerHeight')
    total_width = driver.execute_script('return document.body.offsetWidth')
    viewport_width = driver.execute_script("return document.body.clientWidth")

    assert(viewport_width == total_width)

    # scroll the page, take screenshots and save screenshots to slices
    offset = 0
    slices = {}
    while offset < total_height:
        if offset + viewport_height > total_height:
            offset = total_height - viewport_height

        driver.execute_script('window.scrollTo({0}, {1})'.format(0, offset))
        time.sleep(scroll_delay)

        img = Image.open(BytesIO(driver.get_screenshot_as_png()))
        slices[offset] = img

        offset = offset + viewport_height

    # combine image slices
    stitched_image = Image.new('RGB', (total_width * device_pixel_ratio, total_height * device_pixel_ratio))
    for offset, image in slices.items():
        stitched_image.paste(image, (0, offset * device_pixel_ratio))
    stitched_image.save(file)


def get_screenshot_from_url(URL, FILENAME):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080") # Change this for different viewing options
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    with webdriver.Remote(command_executor=SERVER, options=options) as driver:
        driver.get(URL)
        fullpage_screenshot(driver, FILENAME)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python app.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    filename = "page_stitch_screenshot.png"
    get_screenshot_from_url(url, filename)
    print(f"Screenshot saved to {filename}")
