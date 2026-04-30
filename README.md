# Google Ads Performance Dashboard
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![DAX](https://img.shields.io/badge/DAX-003366?style=for-the-badge)
![Data Visualization](https://img.shields.io/badge/Data%20Visualization-4CAF50?style=for-the-badge)
![Analytics](https://img.shields.io/badge/Analytics-FF6F00?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
## Project Overview
This project analyzes Google Ads performance across different devices (Mobile, Desktop, Tablet) with a focus on **conversion efficiency and cost optimization**.

The dashboard is built in Power BI using DAX measures and interactive visuals to help stakeholders identify performance differences and optimization opportunities.

## Project Demo
Power BI (.pbix) file is included in this repository.  
You can download it and open using Power BI Desktop to interact with the dashboard.

## Business Objective
To evaluate:
- Which device drives the most traffic
- Which device converts most efficiently
- Where advertising spend can be optimized

## Key Metrics
- Total Clicks
- Total Conversions
- Conversion Rate (%)
- Cost per Conversion (CPA)

## DAX Measures
### Conversion Rate %
```dax
Conversion Rate % = DIVIDE(
    [Total Conversions],
    [Total Clicks])
```
### Cost Per Conversion (CPA)
```dax
Cost per Conversion (₹) = 
DIVIDE(
    [Total Cost (₹)],
    [Total Conversions])
```
### Dynamic Dashboard Title
```dax
Dynamic Title = "Google Ads Performance | Device: " & 
IF(
    HASONEVALUE('Ads'[Device]),
    VALUES('Ads'[Device]),
    "All Devices")
```

## Key Insights
- Mobile generates the highest traffic but does not significantly outperform in conversions, indicating lower efficiency.
- Desktop shows slightly better performance with higher conversion rate and lower CPA.
- Tablet underperforms across all metrics and may require optimization or budget reallocation.
- Overall differences across devices are minimal, which indicates relatively stable campaign performance.

## Data Limitations
- Revenue was not available in the dataset and was simulated for demonstration purposes.
- Due to this, profitability metrics like ROAS were not used for decision-making.
- Dataset covers a single month of Google Ads data, limiting long-term trend analysis. Monthly comparisons are not possible with this dataset.

## Tools Used
- Power BI
- DAX
- Python (Data Cleaning) — see `data_cleaning.py`

## Dashboard Features
- Daily trend analysis (Clicks, Conversions, CPA over 30-day period)
- Interactive slicers for Device
- Dynamic dashboard title reflecting selected Device
- Scatter plot for analyzing volume vs efficiency
- Custom tooltip for detailed device-level insights
- Consistent color-coded metrics for better readability

## Dashboard Preview
<img width="1803" height="1021" alt="Dashboard" src="https://github.com/user-attachments/assets/f9bcfbc7-e7bd-4656-9191-5d1d2030aedf" />

## Conclusion
This dashboard provides a structured view of ad performance, highlighting that while volume differs across devices, efficiency remains relatively consistent. Since performance differences are small, optimization efforts should focus on improving cost efficiency and conversions rather than making big changes. Extending this dashboard to 3–6 months of data would enable seasonality analysis and more confident budget reallocation decisions.

