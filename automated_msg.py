from selenium import webdriver


def sendwhatsapp(phone, msg):
    try:
        msg_box = driver.find_element_by_class_name('_1Plpp')
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()

    except Exception as e:
        print("web address not valid.so not send to ", phone, '\n', e)


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
phone = input("enter phone number or empty for selecting on screen:")
if phone != '':
    driver.get("https://web.whatsapp.com/send?phone=91" + phone)
try:
    msg = input("enter message:")
    no = int(input("enter no of times:"))
    for i in range(0, no):
        sendwhatsapp(phone, msg)
        print(i)


except Exception as e:
    print("Error due to selenium driver", e)
finally:
    driver.close()
