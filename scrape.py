from time import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os
import pandas as pd
from selenium.webdriver.common.by import By




from selenium.webdriver.chrome.service import Service


service_gecko = Service(executable_path=r'C:\Users\Shiva Chandan Reddy\Videos\chromedriver.exe')


driver = webdriver.Chrome(service=service_gecko)


irr_date=[]
Evapotranspiration=[]
acc_Evapotranspiration=[]
rainfall=[]
acc_rainfall=[]
water_bal=[]
url = 'https://www.mesonet.org/node/971/webform/confirmation?ref=324&token=M8Miwjb5v8D7rrZ0nNzRZTs4Jhfs_PitRpCQECmcbrI'
driver.get(url)
driver.maximize_window()
sleep (5)
irr_date_sel=driver.find_elements(By.CSS_SELECTOR,'div#webform-confirmation__table>table>tbody>tr>th')
Evapotranspiration_sel=driver.find_elements(By.CSS_SELECTOR,'div#webform-confirmation__table>table>tbody>tr>td:nth-of-type(1)')
Acc_Evapotranspiration_sel=driver.find_elements(By.CSS_SELECTOR,'div#webform-confirmation__table>table>tbody>tr>td:nth-of-type(2)')
rainfall_sel=driver.find_elements(By.CSS_SELECTOR,'div#webform-confirmation__table>table>tbody>tr>td:nth-of-type(3)')
acc_rainfall_sel=driver.find_elements(By.CSS_SELECTOR,'div#webform-confirmation__table>table>tbody>tr>td:nth-of-type(4)')
water_bal_sel=driver.find_elements(By.CSS_SELECTOR,'div#webform-confirmation__table>table>tbody>tr>td:nth-of-type(5)')




for a in irr_date_sel:
    irr_date.append(a.text)
for a in Evapotranspiration_sel:
    Evapotranspiration.append(a.text)
for a in Acc_Evapotranspiration_sel:
    acc_Evapotranspiration.append(a.text)
for a in rainfall_sel:
    rainfall.append(a.text)
for a in acc_rainfall_sel:
    acc_rainfall.append(a.text)
for a in water_bal_sel:
    water_bal.append(a.text)




start_date = pd.to_datetime('2023-10-01')
end_date = start_date + pd.DateOffset(days=138)




df=pd.DataFrame()
df['Last Irrigation Date']=pd.to_datetime(pd.Series(irr_date))
#df['Last Irrigation Date'] = pd.to_datetime(df['Last Irrigation'])
df['Evapotranspiration (in.)']=pd.Series(Evapotranspiration)
#df['Accumulated Evapotranspiration (in.)']=pd.Series(acc_Evapotranspiration)
df['Rainfall (in.)']=pd.Series(rainfall)
#df['Accumulated Rainfall (in.)']=pd.Series(acc_rainfall)
#df['Water Balance (in.)']=pd.Series(water_bal)




filtered_df = df[(df['Last Irrigation Date'] >= start_date) & (df['Last Irrigation Date'] <= end_date)]




filtered_df.to_csv(r"C:\Users\Shiva Chandan Reddy\Documents\Desktop\RA WORK\Irrigation Planner results\STILLWATER\WHEAT\StillwaterWheat.csv",index=False)


print(filtered_df)


driver.quit()