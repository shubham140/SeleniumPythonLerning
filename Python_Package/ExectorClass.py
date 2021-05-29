from Python_Package import DriverClass
from Python_Package import GenericFunctions
from Python_Package import  LocatorsClass
from time import sleep
from jproperties import Properties
config=Properties()
with open('D:\\pythonProject\\Python_Package\\Property.properties', 'rb') as config_file:
    config.load(config_file)
GenericFunctions.getURL(LocatorsClass.URL)
sleep(20)
GenericFunctions.findElement(LocatorsClass.LOGIN_NAME).send_keys(config.get("username"))
GenericFunctions.findElement(LocatorsClass.LOGIN_PASSWORD).send_keys(config.get("password"))
GenericFunctions.findElement(LocatorsClass.LOGIN_BUTTON).click()
sleep(10)
GenericFunctions.findElement(LocatorsClass.ADMIN_BUTTON).click()