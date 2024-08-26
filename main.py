from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

list_of_fiis = [
  'IRDM11', 
  'KNCR11', 
  'KNSC11', 
  'HGCR11', 
   
  'XPML11', 
  'HGBS11', 
  
  'HGLG11', 
  'BTLG11',
  'VILG11',
  
  'KNRI11', 
  'ALZR11', 
  'HGRU11',
  
  'VISC11',
  'HSML11',
  'HLOG11',
  'LVBI11',
  'HSLG11',
  'TRXF11'
]

print('TICKER\tDIV. YIELD\tP/VP\tVAR. 30 DIAS\tVAR. 12 MESES')

for fii in list_of_fiis:
  URL = 'https://fundamentus.com.br/detalhes.php?papel=%s' % fii

  page = driver.get(URL)

  # patrimonio = driver.find_element('xpath', '/html/body/div[1]/main/div[7]/div[2]/div[2]')

  # n_cotas = driver.find_element('xpath', '/html/body/div[1]/main/div[7]/div[2]/div[2]/div/div[1]/h3')

  div_yield = driver.find_element(
    'xpath', '/html/body/div[1]/div[2]/table[3]/tbody/tr[3]/td[4]/span')

  p_vp = driver.find_element(
    'xpath', '/html/body/div[1]/div[2]/table[3]/tbody/tr[4]/td[4]/span')

  trinta_dias = driver.find_element(
    'xpath', '/html/body/div[1]/div[2]/table[3]/tbody/tr[4]/td[2]/span/font')

  doze_meses = driver.find_element(
    'xpath', '/html/body/div[1]/div[2]/table[3]/tbody/tr[5]/td[2]/span/font')

  print('%s\t%s\t\t%s\t%s\t\t\t%s' %
        (fii, div_yield.text, p_vp.text, trinta_dias.text, doze_meses.text))

  driver.back()
'''
URL = "https://www.fundsexplorer.com.br/funds/irdm11"

page = requests.get(URL)

#print(page.text)

#f = write()
soup = BeautifulSoup(page.content, "html.parser")


with open('a.txt', 'w') as f:
    f.write(str(soup))
#results = soup.find(id="asset-price-range")
#print(results.prettify())


job_elements = soup.find_all('div', class_='carousel-cell')
for job_element in job_elements:
  if job_element.contents[1].contents[0] == 'Liquidez Diária':
    print('Liquidez Diária')
    print(job_element.contents[3].contents[0].strip())
  if job_element.contents[1].contents[0] == 'P/VP':
    print('P/VP')
    print(job_element.contents[3].contents[0].strip())


    
  
#<div class="info ">
#<h3 class="title m-0">P/VP</h3>
#<strong class="value">0,95</strong>
'''
