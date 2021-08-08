from PyQt5 import QtWidgets
from PyQt5 import QtTest
from main import MainWindow
class statecode(MainWindow):
    def searching_start(self):        
        from selenium import webdriver
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        from selenium.common.exceptions import TimeoutException
        from selenium.webdriver.support.ui import Select
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.chrome.options import Options
        import webbrowser
        import time
        import re
        import datetime
        global driver
        
        start_time = datetime.datetime.now()
        
        opt = Options()
        # opt.add_argument("--headless")
        opt.add_argument('--disable-blink-features=AutomationControlled')
        opt.add_argument("--disable-infobars")
        opt.add_argument("--disable-notifications")
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")
        opt.add_argument("--in-process-gpu")
        opt.add_argument("--log-level=OFF")
        opt.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        driver = webdriver.Chrome(options=opt, executable_path=('./driver/chromedriver.exe'))
        driver.get("https://www.cowin.gov.in/home")
        
        
        WebDriverWait(driver,200).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))
        def dist_clicker():
            try:
                WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'mat-tab-label-0-1'))).click()
                return True
            except:
                return False
        
        while not dist_clicker():
            driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
            dist_clicker()
    
        def clicker_state(self):
            WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'mat-select-0'))).click()
            try:
                for i in range(500):
                    x = f'mat-option-{i}'
                    option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, x)))
    #                 print(option.text)
                    if option.text == self.ui.statename_line.text():
                        option.click()
    #                     print("done")
                        return True
            except:
                print("except block running")
                return False
        
        
        def clicker_city(self):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'mat-select-value-3'))).click()
            try:
                for i in range(500):
                    try:
                        x = f'mat-option-{i}'
                        option1 = driver.find_element_by_id(x)
    #                     print(option1.text)
                        if option1.text == self.ui.cityname_line.text():
                            option1.click()
    #                         print("done")
                            search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'searchBtn'))).click()
                            return True
                    except:
                        pass
            except:
                return False
    
        #----------------------------------------------------------------------------------------------------------------------
        def titlefinder():
            try:
                QtTest.QTest.qWait(5000)
                walkin = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'search-with-walkin')))
                for i in walkin:
                    result = (i.text)
    
                if re.search('\d', result):
                    len_checker = re.findall('\d', result)
                    # print(len_checker)
    
                    if type(len_checker) == list:
                        total = int(len_checker[0])
                        print(f'{total} Vaccination center are available in your area')
                        self.ui.pin_error.setText(f'{total} Vaccination center are available in your area')
    
                        if total >= 1:
                            print("Registration process is continue in your area")
                            self.ui.pin_error.setText(f'Registration process is continue in your area')
                            return True
                        elif total == 0:
                            print("Walkin Process is working on your area")
                            self.ui.pin_error.setText(f'Walkin Process is working on your area')
                            return False
    
                    elif type(len_checker) == str:
                        total = int(len_checker)
                        print(total)
                        if total >= 1:
                            print("Registration process is working on your area")
                            self.ui.pin_error.setText(f'Registration process is continue in your area')
                            return True
                        elif total == 0:
                            print("Walkin Process is working on your area")
                            self.ui.pin_error.setText(f'Walkin Process is working on your area')
                            return False
                    else:
                        print("Something Wrong happen at area's total vaccination center counting")
                        self.ui.pin_error.setText(f"Something Wrong happen at area's total vaccination center counting")
    
                else:
                    print("else part return false")
                    self.ui.pin_error.setText(f"else part return false")
                    return False
            except:
                print("except part return false")
                self.ui.pin_error.setText(f"except part return false")
                return False
    
        #----------------------------------------------------------------------------------------------------------------------
        def young_click(enable):
            if enable == True:
                younger = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Search-Vaccination-Center"]/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[3]/ul/li[1]/div/div[1]/label'))).click()
                return True
            else:
                return False
            
        def miiddle(enable):
            if enable == True:
                middle = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Search-Vaccination-Center"]/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[3]/ul/li[1]/div/div[2]/label'))).click()
                return True
            else:
                return False
        
        def golden(enable):
            if enable == True:
                golden = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Search-Vaccination-Center"]/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[3]/ul/li[1]/div/div[3]/label'))).click()
                return True
            else:
                return False
    
        def paid(enable):
            if enable == True:
                paid = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Search-Vaccination-Center"]/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[3]/ul/li[2]/div/div[1]/label'))).click()
                return True
            else:
                return False
        
        def free(enable):
            if enable == True:
                free = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Search-Vaccination-Center"]/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[3]/ul/li[2]/div/div[2]/label'))).click()
                return True
            else:
                return False
    
        def covishield_click(enable):
            if enable == True:
                covishield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Search-Vaccination-Center"]/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[3]/ul/li[3]/div/div[1]/label'))).click()
                return True
            else:
                return False
            
        def covaxin_click(enable):
            if enable == True:
                covaxin = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Search-Vaccination-Center"]/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[3]/ul/li[3]/div/div[2]/label'))).click()
                return True
            else:
                return False
        #----------------------------------------------------------------------------------------------------------------------
        
        def slot_grabber():
            global ans
            try:
                slotq = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'center-box')))
                ans = slotq.text
                ans = list(ans.split("\n"))
                print(ans)
    
                if len(ans) > 1:
                    return True
                elif len(ans) == 1:
                    print(ans[0])
                    return False
                else:
                    return False
            except:
                return False
            return ans
        
        #----------------------------------------------------------------------------------------------------------------------
        def d1finder(self):
            try:
                self.ui.tableWidget.setColumnWidth(0, 250)
                self.ui.tableWidget.setColumnWidth(1, 300)
                self.ui.tableWidget.setColumnWidth(2, 100)
                
                stylesheet = "::section{color:rgb(0,0,0);}"
                self.ui.tableWidget.verticalHeader().setStyleSheet(stylesheet)
                
                stylesheet = "::section{color:rgb(0,0,0);}"
                self.ui.tableWidget.horizontalHeader().setStyleSheet(stylesheet)
                
                _basestr = []
                for i in range(len(ans)):
                    k = 0
                    if ans[i] == "D1":
                        if re.search('\d[1-9]|\d\d|\d\d\d', ans[i+1]):
                            print(f'1st\t\t\t\t{i}')
                            k = i
                            for z in range(0,i):
                                print(f'2nd\t\t\t\t{i}')
                                if re.search('\d{6}', ans[k]):
                                    main = [ans[k-1], ans[k], ans[i+1]]
                                    _basestr.append(main)
                                    print(f"main\t\t\t\t{ans[k-1], ans[k], ans[i+1]}")
                                    break
                                k -= 1
                            pass
                        else:
                            print('slots are fulled')
                            pass
                if len(_basestr) >= 1:
                    tablerow=0
                    # webbrowser.open("E:\music\Fallin for You - Shrey Singhal.mp3")
                    print(len(_basestr))
                    print(f"\nit's main str:- {_basestr}\n")
                    for i in range(len(_basestr)):
                        k = _basestr[i]
                        for _temp in range(0,1):
                            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(k[0]))
                            self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(k[1]))
                            self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(k[2]))
                            self.ui.tableWidget.setRowHeight(tablerow, 100)
                            tablerow += 1
                    return False
                return True
            except IndexError as E:
                print(E)
                return True
            except Exception as E:
                print(E)
                return False
    
        def d2finder(self):
            try:
                self.ui.tableWidget.setColumnWidth(0, 250)
                self.ui.tableWidget.setColumnWidth(1, 300)
                self.ui.tableWidget.setColumnWidth(2, 100)
                
                stylesheet = "::section{color:rgb(0,0,0);}"
                self.ui.tableWidget.verticalHeader().setStyleSheet(stylesheet)
                
                stylesheet = "::section{color:rgb(0,0,0);}"
                self.ui.tableWidget.horizontalHeader().setStyleSheet(stylesheet)
                
                _basestr = []
                for i in range(len(ans)):
                    k = 0
                    if ans[i] == "D2":
                        if re.search('\d[1-9]|\d\d|\d\d\d', ans[i+1]):
                            print(f'1st\t\t\t\t{i}')
                            k = i
                            for z in range(0,i):
                                print(f'2nd\t\t\t\t{i}')
                                if re.search('\d{6}', ans[k]):
                                    main = [ans[k-1], ans[k], ans[i+1]]
                                    _basestr.append(main)
                                    print(f"main\t\t\t\t{ans[k-1], ans[k], ans[i+1]}")
                                    break
                                k -= 1
                            pass
                        else:
                            print('slots are fulled')
                            pass
                if len(_basestr) >= 1:
                    tablerow=0
                    # webbrowser.open("E:\music\Fallin for You - Shrey Singhal.mp3")
                    print(len(_basestr))
                    print(f"\nit's main str:- {_basestr}\n")
                    for i in range(len(_basestr)):
                        k = _basestr[i]
                        for _temp in range(0,1):
                            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(k[0]))
                            self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(k[1]))
                            self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(k[2]))
                            self.ui.tableWidget.setRowHeight(tablerow, 100)
                            tablerow += 1
                    return False
                return True
            except IndexError as E:
                print(E)
                return True
            except Exception as E:
                print(E)
                return False
        #----------------------------------------------------------------------------------------------------------------------

        def main_funcation(self):
            while True:
                QtTest.QTest.qWait(10000)
                if clicker_state(self) == True:
                    pass
                else:
                    print('clicker_state return False')
                    self.ui.pin_error.setText(f'Statename must be written in Capitlize form. Kindly prefer placeholder Format.')
                    driver.close()
                    break
                
                QtTest.QTest.qWait(10000)
                if clicker_city(self) == True:
                    pass
                else:
                    print('clicker_city return False')
                    self.ui.pin_error.setText(f'Cityname must be written in Capitlize form. Kindly prefer placeholder Format')
                    driver.close()
                    break
            
                if (self.ui.agetype_box.currentText()) == '18&Above':
                    if young_click(True) == True:
                        pass
                    else:
                        print('titlefiner return False')
                        driver.close()
                        break
                elif (self.ui.agetype_box.currentText()) == '18 to 45':
                    if miiddle(True) == True:
                        pass
                    else:
                        print('titlefiner return False')
                        driver.close()
                        break
                else:
                    if golden(True) == True:
                        pass
                    else:
                        print('titlefiner return False')
                        driver.close()
                        break
                    
                if (self.ui.vaccinetype_box.currentText()) == 'Covishield':
                    if covishield_click(True) == True:
                        pass
                    else:
                        print('covishield_click return False')
                        driver.close()
                        break
                else :
                    if covaxin_click(True) == True:
                        pass
                    else:
                        print('covishield_click return False')
                        driver.close()
                        break

                if (self.ui.paidtype_box.currentText()) == 'Free':
                    if free(True) == True:
                        pass
                    else:
                        print('titlefiner return False')
                        driver.close()
                        break
                else:
                    if paid(True) == True:
                        pass
                    else:
                        print('titlefiner return False')
                        driver.close()
                        break
                QtTest.QTest.qWait(5000)
                if titlefinder() == True:
                    pass
                else:
                    print('titlefiner return False')
                    driver.close()
                    break
                
                if slot_grabber() == True:
                    pass
                else:
                    print('slot_grabber return False')
                    driver.close()
                    break
                if  self.ui.deos_no.text() == '1':
                    if d1finder(self) == True:
                        pass
                    else:
                        print(f'\nit take {datetime.datetime.now() - start_time} seconds to find the free vaccination center')
                        driver.close()
                        break
                else:
                    if d2finder(self) == True:
                        pass
                    else:
                        print(f'\nit take {datetime.datetime.now() - start_time} seconds to find the free vaccination center')
                        self.ui.pin_error.setText(f'\nit take {datetime.datetime.now() - start_time} seconds to find the free vaccination center')
                        driver.close()
                        break
                    break
                return True
                                
        
                        
        main_funcation(self)    
