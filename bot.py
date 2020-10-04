
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class inicio :
    def __init__(self,username,password):
        self.username = username
        self.password = password 
        self.driver = webdriver.Firefox(executable_path=r"#VariavelDeAmbiente(EX:geckodriver.exe)")
    
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(6)
        user = driver.find_element_by_xpath("//input[@name='username' and @type='text']")
        user.clear()
        user.send_keys(self.username)
        password = driver.find_element_by_xpath("//input[@name='password' and @type='password']")
        password.clear()
        password.send_keys(self.password)
        time.sleep(random.randint(3,5))
        password.send_keys(Keys.RETURN)
        time.sleep(6)
        self.pesquisa("followforfollowback")
    
    @staticmethod
    def escrever(onde,comentarios):
        for letra in comentarios:
            onde.send_keys(letra)
            time.sleep(random.randint(1,5)/30)
        

    def pesquisa(self,tag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+tag+"/")
        for i in range(1,25):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randint(1,3))
        hrefs = driver.find_elements_by_tag_name("a")
        pic = [ft.get_attribute("href") for ft in hrefs]
        print(tag + " fotos: " + str(len(pic)))

        comentarios =["follow me","follow back","sdv","follow @newside_off"]
       
        for pic_href in pic:
            try:
                pic_href.index("https://www.instagram.com/p/")
            except ValueError as err:
                print("pulando link inválido")    
            driver.get(pic_href)
            driver.find_element_by_class_name("Ypffh").click()
            onde = driver.find_element_by_class_name("Ypffh")
            self.escrever(onde,random.choice(comentarios))
            time.sleep(random.randint(5,9))
           
            driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
            time.sleep(3)
            try:
                time.sleep(random.randint(19, 23))
            except Exception as e:
                print(e)
                time.sleep(5)

gigi = inicio("#email","#senha")
gigi.login()