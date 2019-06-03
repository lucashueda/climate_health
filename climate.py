#
# climate - Lib that has functions to study some extreme climate events like heatwaves, coldwaves, humidex etc
#
# Author: Lucas Hideki Ueda
# Coyright 2019
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def get_hcolors(df, var_temp,mean,pct90):
    
    colors = []
    
    aux_df = df.copy()
    
    for tmp in aux_df[var_temp]:
        
        if(tmp < mean):
            color = (1,0.8,0)
        elif(tmp > pct90):
            color = (0,0,0)
        else:
            color = (1,0.1,0)
            
        colors.append(color)

    
    return colors, aux_df

def plot_heatwave(df, FLAG_HEATWAVE,var_temperature = 'MAX_N_AIRTMP_MED10'):
    # Draw horizontal lines
    fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
    ax.hlines(y=np.arange(df.YEAR.nunique()), xmin=0, xmax=3000, color='gray', alpha=0.5, linewidth=.5, linestyles='dashdot')

    
    #getting pct of all temperature
    mean = df[df[FLAG_HEATWAVE] != 0][var_temperature].mean()
    pct90 = df[df[FLAG_HEATWAVE] != 0][var_temperature].quantile(.9)
    
     # Draw the Dots
    for i, make in enumerate(df.YEAR.unique()):
        df_make = df.loc[(df.YEAR==make) & (df[FLAG_HEATWAVE] != 0), :]

        colors, aux_df = get_hcolors(df_make, var_temperature, mean, pct90)

        ax.scatter(y=np.repeat(i, df_make.shape[0]), x='NEW_DAY', data=df_make, s=75, edgecolors=colors , c=colors , alpha=0.7)



    # Decorations

    # Vertical Lines to indicate Stations according to https://www.calendario-365.com.br/epocas-estacoes-do-ano.html
    ax.vlines(x= 360 , ymin=-1, ymax=21, color='black', alpha=1, linewidth=1, linestyles='dotted')
    ax.vlines(x= 90 , ymin=-1, ymax=21, color='black', alpha=1, linewidth=1, linestyles='dotted')
    ax.vlines(x= 180, ymin=-1, ymax=21, color='black', alpha=1, linewidth=1, linestyles='dotted')
    ax.vlines(x= 270 , ymin=-1, ymax=21, color='black', alpha=1, linewidth=1, linestyles='dotted')

    #Annotates
    ax.text(45, 22, " Winter ", fontdict={'size':20}, color='indigo')
    ax.text(125, 22, " Spring ", fontdict={'size':20}, color='indigo')
    ax.text(215, 22, " Summer ", fontdict={'size':20}, color='indigo')
    ax.text(300, 22, " Fall ", fontdict={'size':20}, color='indigo')


    #Corpse
    # ax.set_title('Monthly heatwaves distribution by years', fontdict={'size':22})
    ax.set_xlabel('Days', alpha=0.7, fontdict={'size':12})
    ax.set_yticks(np.arange(df.YEAR.nunique()))
    ax.set_yticklabels(df.YEAR.unique(), fontdict={'horizontalalignment': 'right'}, alpha=0.7)
    ax.set_xlim(0, 370)
    plt.xticks(alpha=0.7)
    plt.gca().spines["top"].set_visible(False)    
    plt.gca().spines["bottom"].set_visible(False)    
    plt.gca().spines["right"].set_visible(False)    
    plt.gca().spines["left"].set_visible(False)   
    plt.grid(axis='both', alpha=.4, linewidth=.1)
    plt.show()
    
    
    
# Plot  coldwaves

def get_ccolors(df, var_temp,mean,pct10):
    
    colors = []
    
    aux_df = df.copy()
    
    for tmp in aux_df[var_temp]:
        
        if(tmp > mean):
            color = (0,0.8,1)
        elif(tmp < pct10):
            color = (0,0,0)
        else:
            color = (0,0.1,1)
            
        colors.append(color)

    
    return colors, aux_df

def plot_coldwave(df, FLAG_COLDWAVE,var_temperature = 'MIN_N_AIRTMP_MED10'):
    # Draw horizontal lines
    fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
    ax.hlines(y=np.arange(df.YEAR.nunique()), xmin=0, xmax=3000, color='gray', alpha=0.5, linewidth=.5, linestyles='dashdot')

    
    #getting pct of all temperature
    mean = df[df[FLAG_COLDWAVE] != 0][var_temperature].mean()
    pct10 = df[df[FLAG_COLDWAVE] != 0][var_temperature].quantile(.1)
    
     # Draw the Dots
    for i, make in enumerate(df.YEAR.unique()):
        df_make = df.loc[(df.YEAR==make) & (df[FLAG_COLDWAVE] != 0), :]

        colors, aux_df = get_ccolors(df_make, var_temperature, mean, pct10)

        ax.scatter(y=np.repeat(i, df_make.shape[0]), x='NEW_DAY', data=df_make, s=75, edgecolors=colors , c=colors , alpha=0.7)



    # Decorations

    # Vertical Lines to indicate Stations according to https://www.calendario-365.com.br/epocas-estacoes-do-ano.html
    ax.vlines(x= 360 , ymin=-1, ymax=21, color='black', alpha=1, linewidth=1, linestyles='dotted')
    ax.vlines(x= 90 , ymin=-1, ymax=21, color='black', alpha=1, linewidth=1, linestyles='dotted')
    ax.vlines(x= 180, ymin=-1, ymax=21, color='black', alpha=1, linewidth=1, linestyles='dotted')
    ax.vlines(x= 270 , ymin=-1, ymax=21, color='black', alpha=1, linewidth=1, linestyles='dotted')

    #Annotates
    ax.text(45, 22, " Winter ", fontdict={'size':20}, color='indigo')
    ax.text(125, 22, " Spring ", fontdict={'size':20}, color='indigo')
    ax.text(215, 22, " Summer ", fontdict={'size':20}, color='indigo')
    ax.text(300, 22, " Fall ", fontdict={'size':20}, color='indigo')


    #Corpse
    # ax.set_title('Monthly heatwaves distribution by years', fontdict={'size':22})
    ax.set_xlabel('Days', alpha=0.7, fontdict={'size':12})
    ax.set_yticks(np.arange(df.YEAR.nunique()))
    ax.set_yticklabels(df.YEAR.unique(), fontdict={'horizontalalignment': 'right'}, alpha=0.7)
    ax.set_xlim(0, 370)
    plt.xticks(alpha=0.7)
    plt.gca().spines["top"].set_visible(False)    
    plt.gca().spines["bottom"].set_visible(False)    
    plt.gca().spines["right"].set_visible(False)    
    plt.gca().spines["left"].set_visible(False)   
    plt.grid(axis='both', alpha=.4, linewidth=.1)
    plt.show()
    
    
# function to check the shape of a dataframe, if shape[0] == 0 then there is no information in this df
def check_shape(data, day, day_name = 'DAY365'):
    
    # Here we explicit variable "DAY365" because of our specific application in this project
    if(data[data[day_name] == day].shape[0] == 0):
        return False
    else:
        return True


# auxiliary function to check if theres is at least 2 consecutive days with air temperature above the p90th in the past
def check_2days(data, day):
    # Data is dataframe
    # Day is the value of day to analyse past 2 days
    
    # If there is information in df in the day in question and 2 back also, the return True, else there is no way to there is a heatwave
    if((check_shape(data,day)) & (check_shape(data,day-1)) & (check_shape(data,day-2)) ):
        return True
    else:
        return False
    
# Function that if "check_2days" is True we check if in these 2 days the definition of heatwave is satisfied
def init_hw(data,day,index = 'CTX90pct',min_tmp_name = 'MIN_N_AIRTMP_MED10', max_tmp_name = 'MAX_N_AIRTMP_MED10', min_p90 = 25, max_p90 = 35):
    # data is the dtaaframe
    # day is the value of the day
    # min_air_var_name is the name (String) of the min_air temperature
    # max_air_var_name is the name (String) of the max_air temperature
    # min_air_p90 is the value of p90 min tmp
    # max_air_p90 is the value of p90 max tmp
    
    # Variables that is in our interest
    var_names = [min_tmp_name,max_tmp_name,'DAY365']
    
    actual_df = data[data['DAY365'] == day][var_names]
    
    if(check_2days(data,day)):
        
        #Creating auxiliar df's for 1 day and 2 day back 
        df1_back = data[data['DAY365'] == day - 1][var_names]
        df2_back = data[data['DAY365'] == day - 2][var_names]

        df1_forward = data[data['DAY365'] == day + 1][var_names]
        df2_forward = data[data['DAY365'] == day + 2][var_names]

#         print(df1.shape)
#         print(df2.shape)
        
        # Defining conditions so that there is or not a heatwave
        if(index == 'CTN90pct'):
            c1_b = df1_back[min_tmp_name].values >= min_p90
            c2_b = df2_back[min_tmp_name].values >= min_p90
            c1_f = df1_forward[min_tmp_name].values >= min_p90
            c2_f = df2_forward[min_tmp_name].values >= min_p90
            c3 = actual_df[min_tmp_name].values >= min_p90
        elif(index == 'CTX90pct'):
            c1_b = df1_back[max_tmp_name].values >= max_p90
            c2_b = df2_back[max_tmp_name].values >= max_p90
            c1_f = df1_forward[max_tmp_name].values >= max_p90
            c2_f = df2_forward[max_tmp_name].values >= max_p90
            c3 = actual_df[max_tmp_name].values >= max_p90
        else:
            print('A valid index name is required.')
            return False
        
#         if((c1_min)&(c2_min)&(c3_min)&(c1_max)&(c2_max)&(c3_max)):
        #Condition if there is 2 days before now that the temperature exceeds the pth
        c_b = c1_b & c2_b
        
        #Condition if there is 2 days AFTER now that the temperature exceeds the pth
        c_f = c1_f & c2_f
        
        if(c3&(c_b | c_f)):
            return True
        else:
            return False
    else:
        return False
    
# Function to actually get heatwaves
def get_heatwave(data, flag, hw_name='none', index = 'CTX90pct',percentile = 0.9, day_name = 'DAY365', year_name = 'YEAR',min_tmp_name = 'MIN_N_AIRTMP_MED10', max_tmp_name = 'MAX_N_AIRTMP_MED10'):
    #The only difference is that flag is an unique flag of heatwave (0,1)
    #and hw_name is a name_flag, for each unique heatwave it will have an unique integer flag (0,1,2,3,...) 
    
    # Define a df that is out mutable dataframe
    df = data.copy()
    
    # here we define the flag variable names
    flag_heat = flag
    flag_unique_heat = hw_name

    # Defining variable that flags heat waves with zeros
    df[flag_heat] = 0
    df[flag_unique_heat] = 0

    # Variable that describe unique heataves, each one of hetawaves will have an unique integer number
    which_heat_wave = 1
    new_hw = False
    
    for y in df[year_name].unique():
        df_year = df[df[year_name] == y]



        itera = iter(df_year[day_name].unique())

        for d in itera:
            # For each day we will have a different pct
            df_pct = df[(df[day_name] >= d-15) & (df[day_name] <= d + 15)]

            pth_max = df_pct[max_tmp_name].quantile(percentile)
            pth_min = df_pct[min_tmp_name].quantile(percentile)
#             print(df_pct.shape,pth_max,pth_min)
            if(init_hw(df_year,d,index = index,max_p90=pth_max,min_p90=pth_min,max_tmp_name = max_tmp_name, min_tmp_name = min_tmp_name)):
                new_hw = True
                df.loc[(df[year_name] == y) & (df[day_name] == d) , flag_heat] = 1
                df.loc[(data[year_name] == y) & (data[day_name] == d) , flag_unique_heat] = which_heat_wave
            else:
                if(new_hw == True):
                    which_heat_wave = which_heat_wave + 1
                    new_hw = False
                pass
    return df



# Function that if "check_2days" is True we check if in these 2 days the definition of coldwave is satisfied
def init_cw(data,day,index = 'CTN90pct',min_tmp_name = 'MIN_N_AIRTMP_MED10', max_tmp_name = 'MAX_N_AIRTMP_MED10', min_p90 = 25, max_p90 = 35):
    # data is the dtaaframe
    # day is the value of the day
    # min_air_var_name is the name (String) of the min_air temperature
    # max_air_var_name is the name (String) of the max_air temperature
    # min_air_p90 is the value of p90 min tmp
    # max_air_p90 is the value of p90 max tmp
    
    # Variables that is in our interest
    var_names = [min_tmp_name,max_tmp_name,'DAY365']
    
    actual_df = data[data['DAY365'] == day][var_names]
    
    if(check_2days(data,day)):
        
        #Creating auxiliar df's for 1 day and 2 day back 
        df1_back = data[data['DAY365'] == day - 1][var_names]
        df2_back = data[data['DAY365'] == day - 2][var_names]

        df1_forward = data[data['DAY365'] == day + 1][var_names]
        df2_forward = data[data['DAY365'] == day + 2][var_names]

#         print(df1.shape)
#         print(df2.shape)
        
        # Defining conditions so that there is or not a heatwave
        if(index == 'CTN90pct'):
            c1_b = df1_back[min_tmp_name].values <= min_p90
            c2_b = df2_back[min_tmp_name].values <= min_p90
            c1_f = df1_forward[min_tmp_name].values <= min_p90
            c2_f = df2_forward[min_tmp_name].values <= min_p90
            c3 = actual_df[min_tmp_name].values <= min_p90
        elif(index == 'CTX90pct'):
            c1_b = df1_back[max_tmp_name].values <= max_p90
            c2_b = df2_back[max_tmp_name].values <= max_p90
            c1_f = df1_forward[max_tmp_name].values <= max_p90
            c2_f = df2_forward[max_tmp_name].values <= max_p90
            c3 = actual_df[max_tmp_name].values <= max_p90
        else:
            print('A valid index name is required.')
            return False
        
#         if((c1_min)&(c2_min)&(c3_min)&(c1_max)&(c2_max)&(c3_max)):
        #Condition if there is 2 days before now that the temperature exceeds the pth
        c_b = c1_b & c2_b
        
        #Condition if there is 2 days AFTER now that the temperature exceeds the pth
        c_f = c1_f & c2_f
        
        if(c3&(c_b | c_f)):
            return True
        else:
            return False
    else:
        return False

# Function to actually get coldwaves
def get_coldwave(data, flag, cw_name='none', index = 'CTN90pct',percentile = 0.1, day_name = 'DAY365', year_name = 'YEAR',min_tmp_name = 'MIN_N_AIRTMP_MED10', max_tmp_name = 'MAX_N_AIRTMP_MED10'):
    #The only difference is that flag is an unique flag of heatwave (0,1)
    #and hw_name is a name_flag, for each unique heatwave it will have an unique integer flag (0,1,2,3,...) 
    
    # Define a df that is out mutable dataframe
    df = data.copy()
    
    # here we define the flag variable names
    flag_cold = flag
    flag_unique_cold = cw_name

    # Defining variable that flags heat waves with zeros
    df[flag_cold] = 0
    df[flag_unique_cold] = 0

    # Variable that describe unique heataves, each one of hetawaves will have an unique integer number
    which_cold_wave = 1
    new_cw = False
    
    for y in df[year_name].unique():
        df_year = df[df[year_name] == y]



        itera = iter(df_year[day_name].unique())

        for d in itera:
            # For each day we will have a different pct
            df_pct = df[(df[day_name] >= d-15) & (df[day_name] <= d+15 )]

            pth_max = df_pct[max_tmp_name].quantile(percentile)
            pth_min = df_pct[min_tmp_name].quantile(percentile)
#             print(df_pct.shape,pth_max,pth_min)
            if(init_cw(df_year,d,index = index,max_p90=pth_max,min_p90=pth_min,max_tmp_name = max_tmp_name, min_tmp_name = min_tmp_name)):
                new_cw = True
                df.loc[(df[year_name] == y) & (df[day_name] == d) , flag_cold] = 1
                df.loc[(data[year_name] == y) & (data[day_name] == d) , flag_unique_cold] = which_cold_wave
            else:
                if(new_cw == True):
                    which_cold_wave = which_cold_wave + 1
                    new_cw = False
                pass
    return df


# Function get thermal amplitude waves
def get_thermamp(data, flag, ta_name='none', index = 'CTN90pct',percentile = 0.1, day_name = 'DAY365', year_name = 'YEAR',min_tmp_name = 'MIN_N_AIRTMP_MED10', max_tmp_name = 'MAX_N_AIRTMP_MED10'):
    #The only difference is that flag is an unique flag of heatwave (0,1)
    #and hw_name is a name_flag, for each unique heatwave it will have an unique integer flag (0,1,2,3,...) 
    
    # Define a df that is out mutable dataframe
    df = data.copy()
    
    # here we define the flag variable names
    flag_cold = flag
    flag_unique_cold = ta_name

    # Defining variable that flags heat waves with zeros
    df[flag_cold] = 0
    df[flag_unique_cold] = 0

    # Variable that describe unique heataves, each one of hetawaves will have an unique integer number
    which_cold_wave = 1
    new_cw = False
    
    for y in df[year_name].unique():
        df_year = df[df[year_name] == y]



        itera = iter(df_year[day_name].unique())

        for d in itera:
            # For each day we will have a different pct
            df_pct = df[(df[day_name] >= d-7) & (df[day_name] <= d +7 )]

            pth_max = df_pct[max_tmp_name].quantile(percentile)
            pth_min = df_pct[min_tmp_name].quantile(percentile)
#             print(df_pct.shape,pth_max,pth_min)
            if(init_cw(df_year,d,index = index,max_p90=pth_max,min_p90=pth_min)):
                new_cw = True
                df.loc[(df[year_name] == y) & (df[day_name] == d) , flag_cold] = 1
                df.loc[(data[year_name] == y) & (data[day_name] == d) , flag_unique_cold] = which_cold_wave
            else:
                if(new_cw == True):
                    which_cold_wave = which_cold_wave + 1
                    new_cw = False
                pass
    return df