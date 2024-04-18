import geopandas as gpd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shapely.wkt import loads
import warnings
warnings.filterwarnings("ignore")
import pickle
import folium
import seaborn as sns
from scipy import stats
from scipy.optimize import curve_fit
from scipy.stats import gamma


def aggregate_community_level_TIF(DemographicsDataframe_info,metric,Blockgroup_boundary_info,column_name_info):
  """
  INPUT :
  DemographicsDataframe_info - Ratio/Relationship between CBG, TIF, and community
  metric                     - e.g) income, housing price, owner, ...
  Blockgroup_boundary_info   - Blockgroup boundary
  column_name_info           - the column name of metric e.g) ['Community', 'Less than $10,000', '$10,000 - $14,999', ... ]

  OUTPUT : metric data in TIF at the community level.
  -----------------------------------------------------------------------------------------------------------------------------------------
  test code
  test_incomeDistribution = pd.DataFrame({'geoid':['a','b','c','d','e'],
                      'Less than $10,000':[[10,2,40],[2,4,8],[20,30,70],[40,10,20],[90,80,70]],
                      '$10,000 to $14,999':[[30,40,50],[4,6,10],[50,60,100],[86,40,32],[10,20,30]]})

  test_demogrpahicsDataFrame = pd.DataFrame(columns=['Community','CBG in Community','TIF in Community','CBG in TIF','CBG-Community-TIF Overlap','Non-TIF Ratio of CBG'])
  test_demogrpahicsDataFrame['Community'] = [0,0]
  test_demogrpahicsDataFrame=test_demogrpahicsDataFrame.drop(1)
  test_demogrpahicsDataFrame['Community'].iloc[0] = 'DOUGLAS'
  test_demogrpahicsDataFrame['CBG in Community'].iloc[0] = ['a', 'b', 'c', 'd','e']
  test_demogrpahicsDataFrame['TIF in Community'].iloc[0] = ['x', 'y', 'z']
  test_demogrpahicsDataFrame['CBG in TIF'].iloc[0] = [['a', 'b'], ['a', 'c', 'e'], ['e', 'd']]
  test_demogrpahicsDataFrame['CBG-Community-TIF Overlap'].iloc[0] = [[0.1, 0.2], [0.1, 0.5, 0.2], [0.1, 0.2]]
  test_demogrpahicsDataFrame['Non-TIF Ratio of CBG'].iloc[0] = [0.1, 0.5, 0.1, 0.2,0.3]
  column_name = ['Community','Less than $10,000','$10,000 to $14,999']
  aggregate_community_level_TIF(test_demogrpahicsDataFrame,test_incomeDistribution,Blockgroup_boundary,column_name)


  result
  Community	Less than $10,000	$10,000 to $14,999
	DOUGLAS	[47.4, 42.2, 69.6]	[52.0, 53.2, 77.4]

  -----------------------------------------------------------------------------------------------------------------------------------------
  """

  GEOID = metric.columns[0]  # name of geoid e.g) 'geoid', 'GEO_ID', 'geo_id', 'GEOID'
  community_names = DemographicsDataframe_info['Community']
  no_data_of_geoid = []
  column_number = len(column_name_info)-1 # reason for -1 : 'Community'
  aggregated_TIF = []
  for com_number, com_name in enumerate(community_names):
    lst = np.zeros((column_number,3))
    for range_name_index, range_name in enumerate(column_name_info[1:]):
      CBG_in_TIF_Community = [item for sublist in DemographicsDataframe_info['CBG in TIF'].iloc[com_number] for item in sublist]
      CBG_in_TIF_Community_index = [index for index, sublist in enumerate(DemographicsDataframe_info['CBG in TIF'].iloc[com_number]) for _ in range(len(sublist))]
      for CBG_index,(index, GEOID_TIF) in enumerate(zip(CBG_in_TIF_Community_index,CBG_in_TIF_Community)):
        if len(metric[metric[GEOID]==GEOID_TIF][range_name])==0:
          no_data_of_geoid.append(GEOID_TIF)
        else:
          Overlap_list = [item for sublist in DemographicsDataframe_info['CBG-Community-TIF Overlap'].iloc[com_number] for item in sublist]
          ratio = Overlap_list[CBG_index]
          lst[range_name_index] += np.array(metric[metric[GEOID]==GEOID_TIF][range_name].iloc[0])*ratio
    aggregated_TIF.append(np.array([[com_name]+list(lst)],dtype=object)[0])
  aggregated_TIF_df = pd.DataFrame(aggregated_TIF, columns = column_name_info)
  return aggregated_TIF_df


def aggregate_community_level_Non_TIF(DemographicsDataframe_info,metric,Blockgroup_boundary_info,column_name_info):
  """
  INPUT :
  DemographicsDataframe_info - Ratio/Relationship between CBG, TIF, and community
  metric                     - e.g) income, housing price, owner, ...
  Blockgroup_boundary_info   - Blockgroup boundary
  column_name_info           - the column name of metric e.g) ['Community', 'Less than $10,000', '$10,000 - $14,999', ... ]

  OUTPUT : metric data in Non TIF at the community level.
  -----------------------------------------------------------------------------------------------------------------------------------------
  test code
  test_incomeDistribution = pd.DataFrame({'geoid':['1500000US170313501001','1500000US170313501002','1500000US170313504001'],
                      'Less than $10,000':[[10,2,40],[2,4,8],[20,30,70]],
                      '$10,000 to $14,999':[[30,40,50],[4,6,10],[50,60,100]]})


  test_demogrpahicsDataFrame = pd.DataFrame({'Community':'DOUGLAS',
                                            'CBG in Community':[['1500000US170313501001','1500000US170313501002','1500000US170313504001']],
                                            'Non-TIF Ratio of CBG':[[0.1,0.5,0.1]]})
  column_name = ['Community','Less than $10,000','$10,000 to $14,999']
  aggregate_community_level_Non_TIF(test_demogrpahicsDataFrame,test_incomeDistribution,Blockgroup_boundary,column_name)

  result

  Community	Less than $10,000	$10,000 to $14,999
  DOUGLAS	[4.0, 5.2, 15.0]	[10.0, 13.0, 20.0]
  -----------------------------------------------------------------------------------------------------------------------------------------
  """
  GEOID = metric.columns[0]  # name of geoid e.g) 'geoid', 'GEO_ID', 'geo_id', 'GEOID'
  community_names = DemographicsDataframe_info['Community']
  no_data_of_geoid = []
  column_number = len(column_name_info)-1 # reason for -1 : 'Community'
  aggregated_Non_TIF = []
  for com_number, com_name in enumerate(community_names):
    lst = np.zeros((column_number,3))
    for range_name_index, range_name in enumerate(column_name_info[1:]):
      for GEOID_in_Community_index,GEOID_in_Community in enumerate(DemographicsDataframe_info['CBG in Community'].iloc[com_number]):
        if len(metric[metric[GEOID]==GEOID_in_Community][range_name])==0:
          no_data_of_geoid.append(GEOID_in_Community)
        else:
          ratio = DemographicsDataframe_info['Non-TIF Ratio of CBG'].iloc[com_number][GEOID_in_Community_index]
          lst[range_name_index] += np.array(metric[metric[GEOID]==GEOID_in_Community][range_name].iloc[0])*ratio

    aggregated_Non_TIF.append(np.array([[com_name]+list(lst)],dtype=object)[0])


  aggregated_Non_TIF_df = pd.DataFrame(aggregated_Non_TIF, columns = column_name_info)
  return aggregated_Non_TIF_df

def Calculate_Median_Income_from_Distribution(data):

  # Now, iterate for every race, every communities.

  communities = np.array(data['Community'])
  col_names = list(data.columns)
  col_names.pop(0)

  def cumulative_gamma_dist(x, shape, scale):
      return gamma.cdf(x, shape, scale=scale)

  def Coef_of_Determination(y_data, y_pred):

      y_mean = np.mean(y_data)

      # Calculate the total sum of squares (TSS)
      TSS = np.sum((y_data - y_mean) ** 2)

      # Calculate the residual sum of squares (RSS)
      RSS = np.sum((y_data - y_pred) ** 2)

      # Calculate the coefficient of determination (R^2)
      R_squared = 1 - (RSS / TSS)

      return R_squared

  median_incomes_list = []
  CoD_list = []

  ranges = [10000, 14999, 19999, 24999, 29999, 34999, 39999, 44999, 49999, 59999, 74999, 99999, 124999, 149999, 199999, np.inf]
  cf_ranges = (np.array(ranges[:-1]) - ranges[0]) / (ranges[-2] - ranges[0])


  for community in communities:
      comm_income = data[data['Community'] == community]


      # obtain percentage of population under the income in list 'ranges'
      W_list = []; B_list = []; L_list = []

      for col in col_names:
          W_list.append(comm_income[col].iloc[0][0])
          B_list.append(comm_income[col].iloc[0][1])
          L_list.append(comm_income[col].iloc[0][2])

      W_list = np.array(W_list); B_list = np.array(B_list); L_list = np.array(L_list)

      temp_CoD_list = []
      temp_median_income_list = []


      # there are communities with certain racial population = 0
      if np.sum(W_list) != 0:
          W_percentage = W_list/np.sum(W_list)
          W_cumulative_percentage = np.array([np.sum(W_percentage[:i+1]) for i in range(len(W_percentage))])

          pars, _ = curve_fit(f = cumulative_gamma_dist, xdata = cf_ranges, ydata = W_cumulative_percentage[:-1], bounds = (-np.inf, np.inf))

          temp_CoD_list.append(Coef_of_Determination(W_cumulative_percentage[:-1], cumulative_gamma_dist(cf_ranges, pars[0], pars[1])))
          temp_median_income_list.append(gamma.median(pars[0], scale=pars[1])*(ranges[-2] - ranges[0]) + ranges[0])
      else:
          temp_CoD_list.append(0)
          temp_median_income_list.append(0)

      if np.sum(B_list) != 0:
          B_percentage = B_list/np.sum(B_list)
          B_cumulative_percentage = np.array([np.sum(B_percentage[:i+1]) for i in range(len(B_percentage))])

          pars, _ = curve_fit(f = cumulative_gamma_dist, xdata = cf_ranges, ydata = B_cumulative_percentage[:-1], bounds = (-np.inf, np.inf))

          temp_CoD_list.append(Coef_of_Determination(B_cumulative_percentage[:-1], cumulative_gamma_dist(cf_ranges, pars[0], pars[1])))
          temp_median_income_list.append(gamma.median(pars[0], scale=pars[1])*(ranges[-2] - ranges[0]) + ranges[0])
      else:
          temp_CoD_list.append(0)
          temp_median_income_list.append(0)

      if np.sum(L_list) != 0:
          L_percentage = L_list/np.sum(L_list)
          L_cumulative_percentage = np.array([np.sum(L_percentage[:i+1]) for i in range(len(L_percentage))])

          pars, _ = curve_fit(f = cumulative_gamma_dist, xdata = cf_ranges, ydata = L_cumulative_percentage[:-1], bounds = (-np.inf, np.inf))

          temp_CoD_list.append(Coef_of_Determination(L_cumulative_percentage[:-1], cumulative_gamma_dist(cf_ranges, pars[0], pars[1])))
          temp_median_income_list.append(gamma.median(pars[0], scale=pars[1])*(ranges[-2] - ranges[0]) + ranges[0])
      else:
          temp_CoD_list.append(0)
          temp_median_income_list.append(0)

      median_incomes_list.append(temp_median_income_list)
      CoD_list.append(temp_CoD_list)

  # Mdeian Income Dataframe
  MI_df = pd.DataFrame(columns = ['Community', 'Median Income'])

  for idx, community in enumerate(communities):
      MI_df.loc[idx] = np.array([community, median_incomes_list[idx]], dtype = object)

  return MI_df

def seperate(aggregated_data_community):
  """
  aggregated_data_community : data is like [[10,20,30]]
  """
  total_number_of_community = len(aggregated_data_community)
  # print(aggregated_data_community.columns)
  metrics = aggregated_data_community.columns[-1]
  column_name = ['Community',f'{metrics} of White',f'{metrics} of Black',f'{metrics} of Latin']

  seperate_race_community_area_Median_income = pd.DataFrame(columns=column_name)
  arr = np.array(['name','White','Black','Latin'])

  for community_number in range(total_number_of_community):
    seperate_race_community_area_Median_income.loc[community_number] = np.array(arr)

  seperate_race_community_area_Median_income['Community'] = aggregated_data_community['Community']

  for community_number, community_name in enumerate(aggregated_data_community['Community']):
    for race_index, race in enumerate([f"{metrics} of White",f"{metrics} of Black",f"{metrics} of Latin"]):
        seperate_race_community_area_Median_income[race].iloc[community_number] = aggregated_data_community[metrics].iloc[community_number][race_index]

  return seperate_race_community_area_Median_income

def aggregate_MI_df_list(df_list):

    list_median_income = []
    one_df = df_list[0]
    White_name = one_df.columns[1]
    Black_name = one_df.columns[2]
    Latin_name = one_df.columns[3]

    # print(one_df.columns)
    community_names = np.array(df_list[0]['Community'])
    columns = df_list[0].columns

    for name in community_names:
        W = [];B = [];L = []
        for df in df_list:
            W.append(df[df['Community'] == name][White_name].iloc[0])
            B.append(df[df['Community'] == name][Black_name].iloc[0])
            L.append(df[df['Community'] == name][Latin_name].iloc[0])

        list_median_income.append(np.array([name, W, B, L], dtype = object))


    return pd.DataFrame(list_median_income, columns = columns)

def Make_matric_with_many_metrics(df_list):

    White = []
    Black = []
    Latin = []
    community_names = np.array(df_list[0]['Community'])
    columns_list = ['Community']
    count =0
    for metric_number in range(len(df_list)):
      metric_name = df_list[metric_number].columns[1]
      metric_name = metric_name.replace(' of ','')
      metric_name = metric_name.replace('White','')
      metric_name = metric_name.replace('Black','')
      metric_name = metric_name.replace('Latin','')
      columns_list.append(metric_name)
    # print(columns_list)

    for name in community_names:
      W = []
      B = []
      L = []
      for column_name_of_df, df in zip(columns_list[1:],df_list):
        W.append(df[df['Community'] == name][column_name_of_df+f' of White'].iloc[0])
        B.append(df[df['Community'] == name][column_name_of_df+f' of Black'].iloc[0])
        L.append(df[df['Community'] == name][column_name_of_df+f' of Latin'].iloc[0])
      White.append(np.array([[name]+W],dtype=object)[0])
      Black.append(np.array([[name]+B],dtype=object)[0])
      Latin.append(np.array([[name]+L],dtype=object)[0])

    aggregated_W = pd.DataFrame(White, columns = columns_list)
    aggregated_B = pd.DataFrame(Black, columns = columns_list)
    aggregated_L = pd.DataFrame(Latin, columns = columns_list)

    return aggregated_W,aggregated_B,aggregated_L


