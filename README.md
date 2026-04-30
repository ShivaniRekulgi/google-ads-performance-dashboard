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
<img width="2059" height="1161" alt="image" src="https://github.com/user-attachments/assets/159d9d4d-f577-4ba5-89e2-b0a43a5fbc71" />

## Conclusion
This dashboard analyzes Google Ads performance for November 2024 across three devices — Desktop, Mobile, and Tablet. All three devices show similar conversion rates (4.7–4.8%) and close CPA values (₹32.5–₹33.0), meaning no single device significantly outperforms the others. Mobile attracts the most clicks but does not convert better, suggesting that more traffic alone does not guarantee better results. Desktop shows the lowest CPA (₹32.6), making it the most cost-efficient device — shifting more budget towards Desktop could improve overall campaign efficiency. A longer dataset of 3–6 months would help identify patterns and guide smarter budget decisions.


