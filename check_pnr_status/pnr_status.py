from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import configparser
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def get_path(file):
    project_path = os.path.abspath(os.path.join(os.curdir, os.pardir))
    return project_path + os.sep + file


config = configparser.ConfigParser()
config.read(get_path('conf') + os.sep + 'config.ini')


def get_pnr_out_file_name(pnr_num):
    return get_path('out') + os.sep + config['misc']['out_file_name_template'].format(no=pnr_num)


def check_pnr_status(pnr_num):
    os.environ['PATH'] += get_path('drivers')
    driver = webdriver.Chrome()
    site = config['site']['url']
    print('Loading {site} ...'.format(site=site))
    driver.get(site)
    elem = driver.find_element_by_name(config['site']['pnr_input_element'])
    elem.clear()
    elem.send_keys(pnr_num)
    elem.send_keys(Keys.RETURN)

    file_name = get_pnr_out_file_name(pnr_num)
    print('Saving output as: ' + file_name)
    driver.save_screenshot(file_name)
    driver.quit()
    print('Bye')


def send_email(pnr_num, email):
    print('Sending email to {email} for PNR no: {no} ...'.format(email=email, no=pnr_num))
    msg = MIMEMultipart()
    msg['Subject'] = 'PNR status of {pnr}'.format(pnr=pnr_num)
    msg['From'] = config['smtp']['username']
    msg['To'] = email

    msg_content = MIMEText('PFA PNR status image.')
    msg.attach(msg_content)

    # attaching the image
    image_file = get_pnr_out_file_name(pnr_num)
    with open(image_file, 'rb') as fp:
        image_data = MIMEImage(fp.read(), name=os.path.basename(image_file))
        msg.attach(image_data)

    server = smtplib.SMTP(config['smtp']['host'], config['smtp']['port'])
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(config['smtp']['username'], config['smtp']['password'])
    server.send_message(msg)
    server.quit()
    print('Email sent!')


def main():
    with open('input.txt') as fp:
        inputs = list(map(lambda x: x.strip(), fp.readlines()))
    pnr_num = inputs[0]
    email = inputs[1]
    if len(pnr_num) == 10 and pnr_num.isdigit():
        check_pnr_status(pnr_num)
        send_email(pnr_num, email)
    else:
        print('Please check your PNR number')


if __name__ == '__main__':
    main()
