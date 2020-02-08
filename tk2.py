'''
TKinter gui with which 'backup1' is going to run:

1. Two buttons are displayed:
		Single_country_button - Button to print the graph of gdp vs an attribute(to be accepted later) for one country over the years.
		Many_countries_button - Button to print graphs for the given no.of countries  for each year.
	SINGLE_COUNTRY_BUTTON:
	Country code is asked from the user.
	Six buttons are displayed:
		Each of the buttons call the function draw_three_dimensionl with choice_option and country_code as parameters.

	MANY_COUNTRIES_BUTTON:
	No. of countries is accepted from the user.'
	Six buttons are displayed:
		Each of the buttons call the function 'draw_graph_for_stats' with choice_code and country_count as parameters.


'''



from tkinter import *
from backup1 import draw_three_dimensional
from backup1 import draw_graph_for_stats

root = Tk()


import matplotlib.pyplot as py
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg, FigureCanvasTkAgg
from matplotlib.figure import Figure


myFrame = Frame(root)
myFrame.pack()

'''photo = PhotoImage(file = "/home/karunyav/Downloads/Documents/sem2/package/python/checking/world.jpg")
w = Label(root, image = photo)
w.pack()'''



#Retrieved the entry given to the textbox which is the required country code.
#def retrieve_household():
	

#show_list_single function: Accepts the country code and Displays 6 buttons with the 6 differents attributes with which gdp can be compared.
def show_list_single():
	country_code = Label(myFrame, text = "Enter the country code: ")
	country_code.pack()
	entry = Text(myFrame, height = 1, width = 20)
	entry.pack()

	button_household= Button(myFrame, text="GDP vs Household consumption " ,bg = "sky blue", fg = "brown4", command = lambda:draw_three_dimensional("HC", entry.get("1.0", "end-1c")))
	button_capital_stock= Button(myFrame, text="GDP vs capital stock " ,bg = "sky blue", fg = "brown4", command = lambda:draw_three_dimensional("CS", entry.get("1.0", "end-1c")))
	button_merchandise_exports = Button(myFrame, text="GDP vs Merchandise Exports " ,bg = "sky blue", fg = "brown4", command = lambda:draw_three_dimensional("ME", entry.get("1.0", "end-1c")))
	button_merchandise_imports = Button(myFrame, text="GDP vs Merchandise Imports " ,bg = "sky blue", fg = "brown4", command = lambda:draw_three_dimensional("MI", entry.get("1.0", "end-1c")))
	button_human_capital= Button(myFrame, text="GDP vs Human Capital " ,bg = "sky blue", fg = "brown4", command = lambda:draw_three_dimensional("HU", entry.get("1.0", "end-1c")))
	button_population= Button(myFrame, text="GDP vs Population" ,bg = "sky blue", fg = "brown4", command = lambda:draw_three_dimensional("PO", entry.get("1.0", "end-1c")))
	
	button_household.pack()
	button_capital_stock.pack()
	button_merchandise_exports.pack()
	button_merchandise_imports.pack()
	button_human_capital.pack()
	button_population.pack()

#show_list_many function: Accepts the number of countries and displays 6 buttons with the 6 differents attributes with which gdp can be compared.
def show_list_many():
	no_of_countries = Label(myFrame, text = "Enter the number of countries: ")
	no_of_countries.pack()
	entry = Text(myFrame, height = 1, width = 20)
	entry.pack()

	button_household= Button(myFrame, text="GDP vs Household consumption " ,bg = "sky blue", fg = "brown4", command = lambda:draw_graph_for_stats("HC", entry.get("1.0", "end-1c")))
	button_capital_stock= Button(myFrame, text="GDP vs capital stock " ,bg = "sky blue", fg = "brown4", command = lambda:draw_graph_for_stats("CS", entry.get("1.0", "end-1c")))
	button_merchandise_exports = Button(myFrame, text="GDP vs Merchandise Exports " ,bg = "sky blue", fg = "brown4", command = lambda:draw_graph_for_stats("ME", entry.get("1.0", "end-1c")))
	button_merchandise_imports = Button(myFrame, text="GDP vs Merchandise Imports " ,bg = "sky blue", fg = "brown4", command = lambda:draw_graph_for_stats("MI", entry.get("1.0", "end-1c")))
	button_human_capital= Button(myFrame, text="GDP vs Human Capital " ,bg = "sky blue", fg = "brown4", command = lambda:draw_graph_for_stats("HU", entry.get("1.0", "end-1c")))
	button_population= Button(myFrame, text="GDP vs Population" ,bg = "sky blue", fg = "brown4", command = lambda:draw_graph_for_stats("PO", entry.get("1.0", "end-1c")))
	
	button_household.pack()
	button_capital_stock.pack()
	button_merchandise_exports.pack()
	button_merchandise_imports.pack()
	button_human_capital.pack()
	button_population.pack()


#Shows the two main buttons
single_country_button = Button(myFrame, text=" See trend of one country " ,bg = "sky blue", fg = "brown4", command = lambda:show_list_single())
many_countries_button = Button(myFrame, text=" See graphs with trend of many contries " ,bg = "sky blue", fg = "brown4", command = lambda:show_list_many())
single_country_button.pack()
many_countries_button.pack() 
'''def graph_draw(input):

	list1=[1,2,3,4,5]
	list2=[6,7,8,9,10]
	# py.scatter(list1,list2)
	# py.show()
	fig = Figure(figsize=(5, 5), dpi=100)
	a = fig.add_subplot(111)
	a.scatter(list1,list2)
	a.set_xlabel(input)

	canvas = FigureCanvasTkAgg(fig,master=myFrame)
	canvas.get_tk_widget().pack()
	#binst.destroy()
#Prints text

label= Label(myFrame, text = "COMPARISON OF GDP WITH VARIOUS ATTRIBUTES")
label.pack()


country_name = Label(myFrame, text= "Enter the number of countries: ", fg="purple4")
country_input = Entry(myFrame)
country_name.pack()
country_input.pack()


button1 = Button(myFrame, text="Household Consumption vs GDP " ,bg = "sky blue", fg = "brown4", command = graph_draw(country_input.get()))
#button1['command'] = lambda idx=1 , binst=button1: draw_graph(idx, binst)   , command = lambda:graph_draw(country_input.get()

button2 = Button(myFrame, text="Capital Stock vs GDP " , bg = "sky blue",fg = "brown4")
button3 = Button(myFrame, text="Merchandise Exports vs GDP " , bg = "sky blue",fg = "brown4")
button4 = Button(myFrame, text="Merchandise Imports vs GDP " ,bg = "sky blue", fg = "brown4")
button5 = Button(myFrame, text="Human Capital vs GDP " , bg = "sky blue",fg = "brown4")
button6 = Button(myFrame, text="Population vs GDP " , bg = "sky blue",fg = "brown4")

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()



textBox = Text(height = 1, width = 20)

def retrieve():
	return textBox.get("1.0", "end-1c")

textBox.pack()

button1 = Button(myFrame, text="Household Consumption vs GDP " ,bg = "sky blue", fg = "brown4", command = lambda:graph_draw(retrieve()))
button1.pack()''' 

root.mainloop()
