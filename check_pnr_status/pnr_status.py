from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


SITE = "http://www.trainspnrstatus.com"
EL_PNR = "lccp_pnrno1"
OUT_DIR = "out"
TEMPLATE_OUTPUT_FILE_NAME = "pnr_status_{no}.png"


def check_pnr_status(pnr_num):
    project_path = os.path.abspath(os.path.join(os.curdir, os.pardir))
    os.environ['PATH'] += project_path + os.sep + "drivers"
    driver = webdriver.Chrome()

    print("Loading {site} ...".format(site=SITE))
    driver.get(SITE)
    elem = driver.find_element_by_name(EL_PNR)
    elem.clear()
    elem.send_keys(pnr_num)
    elem.send_keys(Keys.RETURN)
    file_name = project_path + os.sep + OUT_DIR + os.sep + TEMPLATE_OUTPUT_FILE_NAME.format(no=pnr_num)
    print("Saving output as: " + file_name)
    driver.save_screenshot(file_name)
    driver.quit()
    print("Bye")


def main():
    pnr_no = open("input.txt").readline()
    if len(pnr_no) == 10 and pnr_no.isdigit():
        check_pnr_status(pnr_no)
    else:
        print("Please check your PNR number")


if __name__ == '__main__':
    main()
