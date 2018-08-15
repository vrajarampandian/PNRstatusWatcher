from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def checkPNRstatus(pnrnum):
    driver = webdriver.Chrome()
    driver.get("http://www.trainspnrstatus.com")
    elem = driver.find_element_by_name("lccp_pnrno1")
    elem.clear()
    elem.send_keys(pnrnum)
    elem.send_keys(Keys.RETURN)
    driver.save_screenshot("pnrstatus.png")
    driver.quit()

def main():
    pnrno = open("input.txt").readline()
    if len(pnrno)==10 and pnrno.isdigit():
        checkPNRstatus(pnrno)
    else:
        print("Please check your PNR number")
if __name__ == '__main__':
    main()