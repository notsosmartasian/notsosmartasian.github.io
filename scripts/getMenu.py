import xml.etree.cElementTree as ET
from selenium import webdriver
from time import localtime, strftime

#cafe: 1920-commons; kings-court-english-house; new-college-house; houston-market
#meals: 1 = first meal of the day, 2 = second meal of the day, 3 = third meal of the day

cafes = ["1920-commons", "kings-court-english-house", "new-college-house", "falk-dining-commons", "mcclelland", "houston-market"]
meals = [1, 2, 3]

def getMenu(cafe, meal): 
	driver = webdriver.PhantomJS()
	driver.get('http://university-of-pennsylvania.cafebonappetit.com/cafe/'+cafe+'/')
	content = driver.find_elements_by_css_selector('section#panel-daypart-menu-'+str(meal)+' .bg.dotted-leader-content')
	return content

root = ET.Element("menus")
timeElement = ET.SubElement(root, "timerun").text = strftime("%Y-%m-%d %H:%M:%S", localtime())

for cafe in cafes:
	cafeElement = ET.SubElement(root, "cafe", name=cafe)
	for meal in meals:
		print "* * * getting " + cafe + " menu " + str(meal) + " * * *\n"
		mealElement = ET.SubElement(cafeElement, "meal", name="meal" + str(meal))	
		menu = getMenu(cafe, meal)
		for item in menu:
			print item.text
			ET.SubElement(mealElement, "item").text = item.text

tree = ET.ElementTree(root)
tree.write("/home/makarios/Documents/DineTrack/data/meals.xml")
