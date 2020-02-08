'''Program to display the trend in various statistics as a scatter graph.
Project work done by V.Karunya and G.S.Nikkitha as part of 2nd Semester studies.
Program components
------------------
1. Data file prepartion program 
        - This reads the datafiles available in the public domain from the URL https://fred.stlouisfed.org/categories/33402/downloaddata
        - the prepared data are stored in the subfolder datasets_final under the folder where this program resides.
          The structure of the datafiles will be
                     <attribute>_file.csv - year, countrycode, gdp (in millions), 
2. Main program 
        Will offer two options :
            1.See the trend of one country for a particular attribute and gdp over the years.
            2.See the trend of mutiple countries for a particular attribute and gdp over a period of years.

       1. Will offer the choice of which statistics is to be viewed and the number of entries to be studied to the user through a menu
        Based on user choice, calls a function "draw_graph_for_stats" with the code for the statistics to be displayed, 
          and the number of entries to be studied in a given year
        --Function "draw_graph_for_stats"
            Based on the code passed in, set the below variables
                The title of the Graph
                The datafile with path
                The Y axis name
                The starting year for which data is available
                The ending year for which data is available
            Loop for the years starting from the first year till the last year call the function 'plot_for_an_year'
            Logic in plot_for_an_year is as below.  
                    Arrive at the top n countries for the given statistics in the given year. This is done in the function maxElements. 
                        This creates the list l_top_countries_in_the_year.
                    Check if any new country in the list as compared to the list 'l_countries_to_plot'. If yes add these countries to the list
                             l_countries_to_plot.
                    Load the data of population in the list l_population
                    Arrive the data of the size of the bubble based on population and store it in the list l_bubble_size
                    Load the data of GDP in the list l_gdp
                    Load the data of the attribute to be studied in the list l_data_to_plot
            Plot the scatter graph. (Do the necessary hacking for clearing/redrawing the content without changing the graph frame)
                    The colours of the countries are given from list_colour and the size from l_bubble_size(taken from l_population). 
                    The country code is shown as a label when mouse pointer is placed on its bubble.

       2. Will offer the choice of which statistics is to be viewed and the number of entries to be studied to the user through a menu
          Asks the user for the country code.
          Calls function 'draw_three_dimensional' which has the code to draw the 3D scatter graph
        --Function "draw_three_dimensional"
            Based on the choice of statistics, set the below variables: 
                The title of the Graph
                The datafile with path
                The y axis name
            Loop through the file to get the list of years (l_year) for which data is available for the given country code.
            For each of the year in l_year, loop through the file to find the corrsponding gdp and the data to be plotted(i.e, the attribute value)
            and append it in the l_gdp and l_data_to_plot lists respectively.
            Plot the 3D scatter graph with:
                x axis - gdp
                y axis - attribute
                z axis - year'''



'''1. Data file prepartion program 
        - This reads the datafiles available in the public domain from the URL https://fred.stlouisfed.org/categories/33402/downloaddata
        - the prepared data are stored in the subfolder datasets_final under the folder where this program resides.
          The structure of the datafiles will be
                     <attribute>_file.csv - year, countrycode, gdp (in millions), 

The above is done in the program <> '''




import random
import numpy as np
import matplotlib.pyplot as plt
import mpld3
from mpl_toolkits.mplot3d import Axes3D




'''3. Function "draw_graph_for_stats"
    Based on the code passed in, set the below variables
        The title of the Graph
                The datafile with path
                The Y axis name
                The starting year for which data is available
                The ending year for which data is available
        Loop for the years starting from the first year till the last year call the function 'plot_for_an_year
        Arrive at the top n countries for the given statistics in the given year. This is done in the function maxElements. 
                    This creates the list l_top_countries_in_the_year.
        Check if any new country in the list as compared to the list 'l_countries_to_plot'. If yes add these countries to the list
                         l_countries_to_plot.'''

def find_min(HC_year_list):
    """Function to find the starting year.
        Returns the starting year"""

    min_year = 2018
    for i in range(len(HC_year_list)):
        check_year = int(HC_year_list[i])
        if(check_year < min_year):
            min_year = check_year
    return min_year

def find_max(HC_year_list):
    """Function to find the ending year.
        Returns the ending year"""

    max_year = 0
    for i in range(len(HC_year_list)):
        check_year = int(HC_year_list[i])
        if(check_year > max_year):
            max_year = check_year
    return max_year
  

def plot_for_a_year(year,datafile_path,title_of_the_graph, y_axis_name, country_count, l_countries_to_plot, datafile_path_prefix):
        """Function to plot the scatter graph for the given year"""
        plt.ion()
        list_color=['#001f3f','#7FDBFF','#3D9970','#2ECC40','#FFDC00','#FF4136','#85144b','#F012BE','#111111','#AAAAAA']
        l_top_countries_in_the_year = []
        data_file = open(datafile_path)
        population_data_file_path = datafile_path_prefix+"PO"+".csv"
        population_data_file = open(population_data_file_path)

        def maxElements(attr_val_list, attr_country_list):
            """Function to find the top n countries for the given attribute for the given year"""

            for i in range(0,int(country_count)):
                max_n = 0.0
                for j in range(len(attr_val_list)):
                    check_val = float(attr_val_list[j])
                    if(check_val > max_n):
                        max_c = attr_country_list[j]
                        max_n = float(attr_val_list[j])
                        pos = j
                attr_val_list.remove(attr_val_list[pos])
                l_top_countries_in_the_year.append(max_c)



        attr_val_list=[]        #For the given year, list of all the values of the chosen attribute
        attr_country_list=[]    #For the given year, list of all the country codes of the chosen attribute
        for line in data_file:
            
            check_year=line.split(',')[0]
            attr_val=line.split(',')[3]
            attr_country=line.split(',')[1]
            if check_year==str(year):
                attr_val_list.append(attr_val)
                attr_country_list.append(attr_country)

        maxElements(attr_val_list,attr_country_list) 
        

        #For each of the elements in the newly formed l_top_countries_in_the_world, if it is not there in l_countries_to_plot, add it.
        for i in l_top_countries_in_the_year:
            if i not in l_countries_to_plot:
                l_countries_to_plot.append(i)
        #print(l_countries_to_plot)


        '''Load the data of population in the list l_population
           Arrive the data of the size of the bubble based on population and store it in the list l_bubble_size
           Load the data of GDP in the list l_gdp
           Load the data of the attribute to be studied in the list l_data_to_plot'''

        l_population=[]
        l_bubble_size=[]
        l_gdp=[]
        l_data_to_plot=[]

        for country in l_countries_to_plot:
            
            #Load the data of population in the list l_population
            population_data_file.seek(0)
            for line in population_data_file:
                check_year = line.split(',')[0]
                check_country = line.split(',')[1]
                if check_year == str(year) and check_country == country:
                    check_attr = line.split(',')[3]
                    check_attr = check_attr[:-1]

                    #Arrive the data of the size of the bubble based on population and store it in the list l_bubble_size
                    bubble_size = float(check_attr) * 20
                    l_population.append(check_attr)
                    l_bubble_size.append(bubble_size)      
  
            #Load the data of GDP in the list l_gdp
            data_file.seek(0)
            for line in data_file:
                check_year = line.split(',')[0]
                check_country = line.split(',')[1]
                if check_year == str(year) and check_country == country:
                    check_attr = line.split(',')[2]
                    check_attr = check_attr[:-1]
                    l_gdp.append(check_attr)

            #Load the data of the attribute to be studied in the list l_data_to_plot
            data_file.seek(0)
            for line in data_file:
                check_year = line.split(',')[0]
                check_country = line.split(',')[1]
                if check_year == str(year) and check_country == country:
                    check_attr = line.split(',')[3]
                    check_attr = check_attr[:-1]
                    l_data_to_plot.append(check_attr)

        '''Plot the scatter graph. (Do the necessary hacking for clearing/redrawing the content without changing the graph frame)
                The colours of the countries are given from list_colour and the size from l_bubble_size(taken from l_population). 
                The country code is shown as a label when mouse pointer is placed on its bubble.''' 

        '''fig,ax = plt.subplots()
        annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                           bbox=dict(boxstyle="round", fc="w"),
                           arrowprops=dict(arrowstyle="->"))'''
        
        plt.scatter(l_gdp,l_data_to_plot,c=list_color,s=l_bubble_size, label=country, alpha=0.5)
        plt.grid(color='black', linestyle='solid')
        plt.ylabel(y_axis_name)
        plt.xlabel('GDP')
        plt.title(title_of_the_graph+"-"+str(year))

        '''tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=l_countries_to_plot)
        mpld3.plugins.connect(fig, tooltip)

        mpld3.show()'''
        plt.draw()
        plt.show()
        plt.clf()
        

  
def draw_graph_for_stats(choice_code, country_count):
    datafile_path_prefix = "/home/karunyav/Downloads/Documents/sem2/package/python/datasets_final/"

    '''Based on the code passed in, set the below variables
        The title of the Graph
                The datafile with path
                The Y axis name
                The starting year for which data is available
                The ending year for which data is available'''

    if(choice_code == 'HC'):
        title_of_the_graph = "GDP vs Household Consumption"
        datafile_path = datafile_path_prefix + choice_code + ".csv"
        y_axis_name = "Household Consumption"
        
        HC_year_list = [] #List of all years availble in HC_file 
        data_file = open(datafile_path)
        for line in data_file:
            HC_year = line.split(',')[0]
            HC_year_list.append(HC_year)

        starting_year = find_min(HC_year_list)
        ending_year = find_max(HC_year_list)
        
    
    if(choice_code=='CS'):
        title_of_the_graph="GDP vs Capital Stock"
        datafile_path=datafile_path_prefix + choice_code + ".csv"
        y_axis_name="Capital Stock"
        
        CS_year_list=[] #List of all years availble in CS_file 
        data_file=open(datafile_path)
        for line in data_file:
            CS_year=line.split(',')[0]
            CS_year_list.append(CS_year)

        starting_year=find_min(CS_year_list)
        ending_year=find_max(CS_year_list)  
        
    

    if(choice_code=='ME'):
        title_of_the_graph="GDP vs Merchandise Exports"
        datafile_path=datafile_path_prefix + choice_code + ".csv"
        y_axis_name="Merchandise Exports"
        
        ME_year_list=[] #List of all years availble in ME_file 
        data_file=open(datafile_path)
        for line in data_file:
            ME_year=line.split(',')[0]
            ME_year_list.append(ME_year)

        starting_year=find_min(ME_year_list)
        ending_year=find_max(ME_year_list)
        
    
        
    if(choice_code=='MI'):
        title_of_the_graph="GDP vs Merchndise Imports"
        datafile_path=datafile_path_prefix + choice_code + ".csv"
        y_axis_name="Merchandise Imports"
        
        MI_year_list=[] #List of all years availble in MI_file 
        data_file=open(datafile_path)
        for line in data_file:
            MI_year=line.split(',')[0]
            MI_year_list.append(MI_year)

        starting_year=find_min(MI_year_list)
        ending_year=find_max(MI_year_list)
     

    if(choice_code=='HU'):
        title_of_the_graph="GDP vs Human Capital"
        datafile_path=datafile_path_prefix + choice_code + ".csv"
        y_axis_name="Human Capital"
        
        HU_year_list=[] #List of all years availble in HU_file 
        data_file=open(datafile_path)
        for line in data_file:
            HU_year=line.split(',')[0]
            HU_year_list.append(HU_year)

        starting_year=find_min(HU_year_list)
        ending_year=find_max(HU_year_list)
    

    if(choice_code=='PO'):
        title_of_the_graph = "GDP vs Population"
        datafile_path = datafile_path_prefix + choice_code + ".csv"
        y_axis_name="Population"
        
        PO_year_list=[] #List of all years availble in PO_file 
        data_file=open(datafile_path)
        for line in data_file:
            PO_year=line.split(',')[0]
            PO_year_list.append(PO_year)

        starting_year=find_min(PO_year_list)
        ending_year=find_max(PO_year_list)
    
    l_countries_to_plot = []    #The main list of countries to be plotted. As each year is plotted, if there is a new country, it is added to this list.

    '''Loop for the years starting from the first year till the last year call the function 'plot_for_a_year'''   
    for year in range(starting_year , ending_year):
        title = "xxxx" + "-" + str(year)
        plot_for_a_year(year,datafile_path,title_of_the_graph, y_axis_name, country_count, l_countries_to_plot, datafile_path_prefix)
    




'''
--Function "draw_three_dimensional"
            Based on the choice of statistics, set the below variables: 
                The title of the Graph
                The datafile with path
                The y axis name
            Loop through the file to get the list of years (l_year) for which data is available for the given country code.
            For each of the year in l_year, loop through the file to find the corrsponding gdp and the data to be plotted(i.e, the attribute value)
            and append it in the l_gdp and l_data_to_plot lists respectively.
            Plot the 3D scatter graph with:
                x axis - gdp
                y axis - attribute
                z axis - year'''

def draw_three_dimensional(choice_code, country_code):
    datafile_path_prefix = "/home/karunyav/Downloads/Documents/sem2/package/python/datasets_final/"


    if(choice_code == 'HC'):
        title_of_the_graph = "GDP vs Household Consumption"
        datafile_path = datafile_path_prefix + choice_code + ".csv"
        y_axis_name = "Household Consumption"
        
        HC_year_list = [] #List of all years availble in HC_file 
        data_file = open(datafile_path)
        for line in data_file:
            HC_year = line.split(',')[0]
            HC_year_list.append(HC_year)
        
    
    if(choice_code=='CS'):
        title_of_the_graph="GDP vs Capital Stock"
        datafile_path=datafile_path_prefix + choice_code + ".csv"
        y_axis_name="Capital Stock"
        
        CS_year_list=[] #List of all years availble in CS_file 
        data_file=open(datafile_path)
        for line in data_file:
            CS_year=line.split(',')[0]
            CS_year_list.append(CS_year)
        
    

    if(choice_code=='ME'):
        title_of_the_graph="GDP vs Merchandise Exports"
        datafile_path=datafile_path_prefix + choice_code + ".csv"
        y_axis_name="Merchandise Exports"
        
        ME_year_list=[] #List of all years availble in ME_file 
        data_file=open(datafile_path)
        for line in data_file:
            ME_year=line.split(',')[0]
            ME_year_list.append(ME_year)

        
        
    if(choice_code=='MI'):
        title_of_the_graph="GDP vs Merchndise Imports"
        datafile_path=datafile_path_prefix + choice_code + ".csv"
        y_axis_name="Merchandise Imports"
        
        MI_year_list=[] #List of all years availble in MI_file 
        data_file=open(datafile_path)
        for line in data_file:
            MI_year=line.split(',')[0]
            MI_year_list.append(MI_year)

        

    if(choice_code=='HU'):
        title_of_the_graph="GDP vs Human Capital"
        datafile_path=datafile_path_prefix + choice_code + ".csv"
        y_axis_name="Human Capital"
        
        HU_year_list=[] #List of all years availble in HU_file 
        data_file=open(datafile_path)
        for line in data_file:
            HU_year=line.split(',')[0]
            HU_year_list.append(HU_year)

        

    if(choice_code=='PO'):
        title_of_the_graph = "GDP vs Population"
        datafile_path = datafile_path_prefix + choice_code + ".csv"
        y_axis_name="Population"
        
        PO_year_list=[] #List of all years availble in PO_file 
        data_file=open(datafile_path)
        for line in data_file:
            PO_year=line.split(',')[0]
            PO_year_list.append(PO_year)

        
    data_file = open(datafile_path)
    population_data_file_path = datafile_path_prefix+"PO"+".csv"
    population_data_file = open(population_data_file_path)

    l_year = []
    l_data_to_plot = []
    l_gdp = []
    
    data_file.seek(0)
    for line in data_file:
        check_country = line.split(',')[1]
        if check_country == country_code:
            check_attr = line.split(',')[0]
            l_year.append(check_attr)

    for year in l_year:

        data_file.seek(0)
        for line in data_file:
            check_year = line.split(',')[0]
            check_country = line.split(',')[1]
            if check_year == str(year) and check_country == country_code:
                check_attr = line.split(',')[3]
                check_attr = check_attr[:-1]
                l_data_to_plot.append(check_attr)

        data_file.seek(0)
        for line in data_file:
            check_year = line.split(',')[0]
            check_country = line.split(',')[1]
            if check_year == str(year) and check_country == country_code:
                check_attr = line.split(',')[2]
                check_attr = check_attr[:-1]
                l_gdp.append(check_attr)

    l_year = list(map(int,l_year))
    l_data_to_plot = list(map(float,l_data_to_plot))
    l_gdp = list(map(float,l_gdp))
   
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    
    ax.scatter(l_gdp, l_data_to_plot, l_year , c='r', s=40)
    ax.set_xlabel('GDP')
    ax.set_ylabel(y_axis_name)
    ax.set_zlabel('YEAR')

    plt.show()




'''2. Main program 
        Will offer two options :
            1.See the trend of one country for a particular attribute and gdp over the years.
            2.See the trend of mutiple countries for a particular attribute and gdp over a period of years.


    CODES:
    1.HC- household consumption
    2.CS- capital stock
    3.ME- merchandise exports
    4.MI- merchandise imports
    5.HU- human capital
    6.PO- population '''


'''
def choose_attr(choice, option):
    if(choice==1):    

        if(option==1):
            country_count=input("Enter the number of countries for which comparison has to be made: ")
            draw_graph_for_stats("HC",country_count)
        elif(option==2):
            country_code=input("Enter the country code: ")
            draw_three_dimensional("HC",country_code)

    elif(choice==2): 

        if(option==1):
            country_count=input("Enter the number of countries for which comparison has to be made: ")
            draw_graph_for_stats("CS",country_count)
        elif(option==2):
            country_code=input("Enter the country code: ")
            draw_three_dimensional("CS",country_code)    

    elif(choice==3):
        if(option==1):
            country_count=input("Enter the number of countries for which comparison has to be made: ")
            draw_graph_for_stats("ME",country_count)
        elif(option==2):
            country_code=input("Enter the country code: ")
            draw_three_dimensional("CS",country_code)    

    elif(choice==4):
        if(option==1):
            country_count=input("Enter the number of countries for which comparison has to be made: ")
            draw_graph_for_stats("MI",country_count)
        elif(option==2):
            country_code=input("Enter the country code: ")
            draw_three_dimensional("CS",country_code)       

    elif(choice==5):

        if(option==1): 
            country_count=input("Enter the number of countries for which comparison has to be made: ")
            draw_graph_for_stats("HU",country_count)
        elif(option==2):
            country_code=input("Enter the country code: ")
            draw_three_dimensional("CS",country_code)    

    elif(choice==6):

        if(option==1):
            country_count=input("Enter the number of countries for which comparison has to be made: ")
            draw_graph_for_stats("PO",country_count)
        elif(option==2):
            country_code=input("Enter the country code: ")
            draw_three_dimensional("CS",country_code)    
    else:
        print("Invalid input")

def  main():
    option=int(input("Do you want to see the trend of multiple countries or of one country? (Enter 1 for the former and 2 for the latter: "))
    choice=int(input("1. Household consumption vs gdp\n2. Capital Stock vs gdp\n3. Merchandise Exports vs gdp\n4. Merchandise Imports vs gdp\n5. Human Capital vs gdp\n6. Population vs  gdp\nEnter your option:"))
    choose_attr(choice, option)


main()
'''