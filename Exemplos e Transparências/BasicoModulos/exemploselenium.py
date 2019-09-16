from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("https://sistemas.riopomba.ifsudestemg.edu.br/dacc/index.php/professores")
print driver.page_source.encode("utf-8")

driver.quit()
