from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import scipy.interpolate as si

# Curve base:
points = [[0, 0], [0, 2], [2, 3], [4, 0], [6, 3], [8, 2], [8, 0], [8, 4], [8, 8], [16, 8], [18, 2]];
points = np.array(points)

x = points[:,0]
y = points[:,1]


t = range(len(points))
ipl_t = np.linspace(0.0, len(points) - 1, 100)

x_tup = si.splrep(t, x, k=3)
y_tup = si.splrep(t, y, k=3)

x_list = list(x_tup)
xl = x.tolist()
x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

y_list = list(y_tup)
yl = y.tolist()
y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

x_i = si.splev(ipl_t, x_list) # x interpolate values
y_i = si.splev(ipl_t, y_list) # y interpolate values

url = "https://codepen.io/falldowngoboone/pen/PwzPYv"
driver = webdriver.Firefox(executable_path="/root/Utilities/webDrivers/geckodriver")
driver.get(url)

action =  ActionChains(driver)

startElement = driver.find_element_by_id('drawer')

# First, go to your start point or Element:
action.move_to_element(startElement);
action.perform();

for mouse_x, mouse_y in zip(x_i, y_i):
    action.move_by_offset(mouse_x,mouse_y);
    action.perform();
    print(mouse_x, mouse_y)