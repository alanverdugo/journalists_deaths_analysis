#!/usr/bin/env python
'''
    I will use a dataset from the Committee to Protect Journalists with data 
    regarding worldwide assassinations of journalists since 1992.
    Since Mexico is one of the most dangerous countries when it comes to being 
    a journalists and it is famous for having corrupt leaders, I will research 
    if there is a correlation between the ruling political parties and the 
    number of journalist killed during each presidential term. I will also 
    create a similar analysis for the USA, for comparison purposes. This 
    research may point to the root cause of the problem and a possible solution 
    to ensure the safety and the free speech of the journalists.
'''
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv

# Open journalists deaths .csv file.
df_journalists = pd.read_csv('./cpj.csv', sep=',')

# Some cleaning: Only keep rows where the date is not "Unknown" and 
# not "Date unknown".
df_journalists = df_journalists[(df_journalists.Date != 'Unknown') & 
                    (df_journalists.Date != 'Date unknown')]

# Extract the year of the assassination and add it as another column.
df_journalists['Date'] = df_journalists['Date'].apply(lambda x: x.replace(')', ''))
df_journalists['Date'] = df_journalists['Date'].apply(lambda x: x.replace(',', ''))
df_journalists['Year'] = df_journalists.Date.apply(lambda x: x[len(x) - 4:])

# Cast the year column to Integer.
df_journalists.Year = df_journalists.Year.astype(int)

# More cleaning: Drop rows where year or country_killed are null.
df_journalists = df_journalists.dropna(subset=['Year', 'Country_killed'], axis=0, how='any')

# Save lowest and highest years (for the graph axis).
beginning_year = df_journalists['Year'].min()
ending_year = df_journalists['Year'].max()


def plot_usa():
    # Now let's analyze the USA data.

    # Select rows where Country_killed == "USA"
    df_usa = df_journalists[df_journalists.Country_killed == 'USA']

    df_rep1 = df_usa[(df_usa.Year >= 1989) & (df_usa.Year < 1993)]
    df_dem1 = df_usa[(df_usa.Year >= 1993) & (df_usa.Year < 2001)]
    df_rep2 = df_usa[(df_usa.Year >= 2001) & (df_usa.Year < 2009)]
    df_dem2 = df_usa[(df_usa.Year >= 2009) & (df_usa.Year < 2017)]
    df_rep3 = df_usa[(df_usa.Year >= 2017)]

    df_rep1_grouped_by_year = df_rep1.groupby('Year').size().reset_index()
    df_dem1_grouped_by_year = df_dem1.groupby('Year').size().reset_index()
    df_rep2_grouped_by_year = df_rep2.groupby('Year').size().reset_index()
    df_dem2_grouped_by_year = df_dem2.groupby('Year').size().reset_index()
    df_rep3_grouped_by_year = df_rep3.groupby('Year').size().reset_index()

    # Convert the DF to numeric values since we want to use the "fill_between" function
    df_rep1_grouped_by_year = df_rep1_grouped_by_year.apply(pd.to_numeric, errors='ignore')
    df_dem1_grouped_by_year = df_dem1_grouped_by_year.apply(pd.to_numeric, errors='ignore')
    df_rep2_grouped_by_year = df_rep2_grouped_by_year.apply(pd.to_numeric, errors='ignore')
    df_dem2_grouped_by_year = df_dem2_grouped_by_year.apply(pd.to_numeric, errors='ignore')
    df_rep3_grouped_by_year = df_rep3_grouped_by_year.apply(pd.to_numeric, errors='ignore')

    # Get data for the axis
    x_rep1 = df_rep1_grouped_by_year['Year']
    y_rep1 = df_rep1_grouped_by_year[0]
    x_dem1 = df_dem1_grouped_by_year['Year']
    y_dem1 = df_dem1_grouped_by_year[0]
    x_rep2 = df_rep2_grouped_by_year['Year']
    y_rep2 = df_rep2_grouped_by_year[0]
    x_dem2 = df_dem2_grouped_by_year['Year']
    y_dem2 = df_dem2_grouped_by_year[0]
    x_rep3 = df_rep3_grouped_by_year['Year']
    y_rep3 = df_rep3_grouped_by_year[0]

    # Set the style for the chart.
    plt.style.use('bmh')

    # Set the plot legends.
    plt.ylabel("Number of deaths")
    plt.xlabel("Year")
    plt.title("Number of journalists killed in USA")

    # Set the axis.
    plt.axis([beginning_year, ending_year, 0, 11])
    plt.grid(True)

    # Set ticks every year.
    plt.xticks(range(beginning_year, ending_year+1, 1))

    # Plot.
    # (Since the US has so few journalists deaths -thankfully-, we need to graph 
    # it as a bar chart in order for it to make some sense)
    plt.bar(x_rep1, y_rep1, color="orangered")
    plt.bar(x_dem1, y_dem1, color="deepskyblue")
    plt.bar(x_rep2, y_rep2, color="orangered")
    plt.bar(x_dem2, y_dem2, color="deepskyblue")
    plt.bar(x_rep3, y_rep3, color="orangered")

    # Add some legends.
    rep_patch = mpatches.Patch(color='orangered', 
        label='Republican is the ruling party.')
    dem_patch = mpatches.Patch(color='deepskyblue', 
        label='Democrat is the ruling party.')
    plt.legend(handles=[rep_patch, dem_patch], loc=2).get_frame().set_facecolor("white")

    # Show the plot.
    plt.show()
    plt.close()


def plot_mexico():
    # Select rows where Country_killed == "Mexico"
    df_mexico = df_journalists[df_journalists.Country_killed == 'Mexico']

    # PRI was in power since the dawn of time to 2001, then started again in 2013.
    # We will build two different datasets to make it easier.
    df_pri_1 = df_mexico[df_mexico.Year <= 2001]
    df_pri_2 = df_mexico[df_mexico.Year >= 2012]

    # PAN was in power between 2002 and 2012.
    df_pan = df_mexico[(df_mexico.Year >= 2001) & (df_mexico.Year <= 2012)]

    # Group deaths per year.
    df_pri_1_grouped_by_year = df_pri_1.groupby('Year').size().reset_index()
    df_pri_2_grouped_by_year = df_pri_2.groupby('Year').size().reset_index()
    df_pan_grouped_by_year = df_pan.groupby('Year').size().reset_index()

    # Convert the DF to numeric values since we want to use the "fill_between" function
    df_pri_1_grouped_by_year = df_pri_1_grouped_by_year.apply(pd.to_numeric, errors='ignore')
    df_pri_2_grouped_by_year = df_pri_2_grouped_by_year.apply(pd.to_numeric, errors='ignore')
    df_pan_grouped_by_year = df_pan_grouped_by_year.apply(pd.to_numeric, errors='ignore')

    # Get data for the axis
    x_pri_1 = df_pri_1_grouped_by_year['Year']
    y_pri_1 = df_pri_1_grouped_by_year[0]
    x_pri_2 = df_pri_2_grouped_by_year['Year']
    y_pri_2 = df_pri_2_grouped_by_year[0]
    x_pan = df_pan_grouped_by_year['Year']
    y_pan = df_pan_grouped_by_year[0]

    # Set the style for the chart.
    plt.style.use('bmh')

    # Set the plot legends.
    plt.ylabel("Number of deaths")
    plt.xlabel("Year")
    plt.title("Number of journalists killed in Mexico")

    # Set the axis.
    plt.axis([beginning_year, ending_year, 0, 11])
    plt.grid(True)

    # Set ticks every year.
    plt.xticks(range(beginning_year, ending_year+1, 1))

    # Plot.
    #plt.fill_between(x_pri_1, y_pri_1, 0, alpha=0.9, interpolate=True, color="indianred")
    #plt.fill_between(x_pan, y_pan, 0, alpha=0.9, interpolate=True, color="skyblue")
    #plt.fill_between(x_pri_2, y_pri_2, 0, alpha=0.9, interpolate=True, color="indianred")
    #plt.plot(x_pri_1, y_pri_1, color="orangered")
    #plt.plot(x_pan, y_pan, color="deepskyblue")
    #plt.plot(x_pri_2, y_pri_2, color="orangered")
    plt.bar(x_pri_1, y_pri_1, color="orangered")
    plt.bar(x_pan, y_pan, color="deepskyblue")
    plt.bar(x_pri_2, y_pri_2, color="orangered")

    # Add some legends.
    pri_patch = mpatches.Patch(color='orangered', 
        label='PRI is the ruling party.')
    pan_patch = mpatches.Patch(color='deepskyblue', 
        label='PAN is the ruling party.')
    plt.legend(handles=[pri_patch, pan_patch], loc=2).get_frame().set_facecolor("white")

    # Show the plot.
    plt.show()
    plt.close()

    # Lets further explore Mexico's data and create a pie char to analyze the 
    # reasons behind the deaths.

    # Data to plot
    df_mex_source_fire = df_mexico.groupby('Source_fire').size().reset_index()
    df_mex_source_fire = df_mex_source_fire.apply(pd.to_numeric, errors='ignore')
    labels = df_mex_source_fire['Source_fire']
    sizes = df_mex_source_fire[0]
     
    # Plot
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)     
    plt.axis('equal')
    plt.show()


plot_usa()

plot_mexico()
