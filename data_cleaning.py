import pandas as pd
import re
#loading data
df = pd.read_excel("C:/Users/rs38129/Desktop/BI/Google Ads/GoogleAds_DataAnalytics_Sales_Uncleaned.xlsx")
print(df.head())
df.info()
df.describe()
df.isnull().sum()
#cleaning the Cost column to remove unwanted symbols and convert the data type to numeric
df['Cost']=df['Cost'].astype(str)
df['Cost']=df['Cost'].str.replace('₹','',regex=False)
df['Cost']=df['Cost'].str.replace('$','',regex=False)
df['Cost']=df['Cost'].str.replace(',','',regex=False)
df['Cost']=pd.to_numeric(df['Cost'],errors='coerce')
#covert date column to datetime type
df['Ad_Date']=pd.to_datetime(df['Ad_Date'], errors='coerce')
#stripping extra spaces and making the text more readable  
df['Device']=df['Device'].str.strip().str.title()
df['Location']=df['Location'].str.strip().str.title()
df['Location']=df['Location'].str.replace({'Hyderbad':'Hyderabad','Hydrebad':'Hyderabad'})
#replacing null or missing values with 0
df['Cost']=df['Cost'].fillna(0)
df['Clicks']=df['Clicks'].fillna(0)
df['Conversions']=df['Conversions'].fillna(0)
df['Campaign_Name']=df['Campaign_Name'].str.strip()
df['Campaign_Name'] = df['Campaign_Name'].apply(
    lambda x: re.sub(r'([a-z])([A-Z])', r'\1 \2', x)
)
df['CTR']=df['Clicks']/df['Impressions'].replace(0, None)
df['Conversion_Rate_Calc']=df['Conversions']/df['Clicks']
df['Cost']=pd.to_numeric(df['Cost'], errors='coerce')
df['Clicks']=pd.to_numeric(df['Clicks'], errors='coerce')
df['Impressions']=pd.to_numeric(df['Impressions'], errors='coerce')
df['Cost']=pd.to_numeric(df['Cost'], errors='coerce')
df['Leads']=pd.to_numeric(df['Leads'], errors='coerce')
df['Conversions']=pd.to_numeric(df['Conversions'], errors='coerce')
df['Sale_Amount'] = pd.to_numeric(df['Sale_Amount'], errors='coerce')
df['Sale_Amount'] = df['Conversions'] * 500
df['CTR'] = pd.to_numeric(df['CTR'], errors='coerce')
df['Conversion_Rate_Calc'] = pd.to_numeric(df['Conversion_Rate_Calc'], errors='coerce')
df['CPC'] = df['Cost'] / df['Clicks']
df['CPC'] = pd.to_numeric(df['CPC'], errors='coerce')
df['Cost_Per_Conversion'] = df['Cost'] / df['Conversions']
df['Cost_Per_Conversion'] = pd.to_numeric(df['Cost_Per_Conversion'], errors='coerce')
df['ROI'] = (df['Sale_Amount'] - df['Cost']) / df['Cost']
df['ROI'] = pd.to_numeric(df['ROI'], errors='coerce')
#exporting dataframe to excel
df.to_excel("C:/Users/rs38129/Desktop/BI/Google Ads/Cleaned_ads_data.xlsx", index=False)
