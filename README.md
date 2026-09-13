# Basic Analysis of Simulated Water-Quality Data from Former Tin-Mining Pits

## Author
Aliefia Noor

## Background
Former tin-mining pits, locally known as *kolong*, are important environmental features in Bangka Belitung, Indonesia. This beginner project was created to practice Python-based environmental data analysis using a simulated dataset.

## Objective
This project demonstrates a basic computational workflow for:
1. Importing a CSV dataset.
2. Checking data structure and missing values.
3. Producing descriptive statistics.
4. Identifying the lowest pH and highest iron concentration.
5. Exploring correlations among selected water-quality variables.
6. Creating scientific visualizations.
7. Saving analysis output as a new CSV file.

## Tools
- Python
- Pandas
- Matplotlib
- Visual Studio Code
- Python virtual environment (venv)

## Dataset
The simulated dataset contains 12 former tin-mining pits and includes:
- Pit age in years
- pH
- Dissolved oxygen
- Turbidity
- Total dissolved solids
- Iron concentration
- Manganese concentration

## Important note
This dataset is simulated for learning purposes only. It does not represent actual field measurements from Bangka Belitung and must not be used to make environmental claims about specific locations.

## Main results from the simulated dataset
- Kolong_01 had the lowest pH value of 3.82.
- Kolong_01 had the highest iron concentration of 5.80 mg/L.
- The pH versus iron plot showed an inverse pattern in the simulated data.
- The pit-age versus pH plot showed that pH increased with pit age in the simulated data.

## Files
- `analysis.py`: Python script for the data analysis.
- `water_data.csv`: Simulated input dataset.
- `water_quality_summary.csv`: Descriptive-statistics output.
- `ph_vs_iron.png`: Scatter plot of pH versus iron concentration.
- `pit_age_vs_ph.png`: Scatter plot of pit age versus pH.

## Learning outcome
This project helped me begin learning independent Python-based environmental data analysis. I practiced reading CSV files, inspecting datasets, calculating descriptive statistics, identifying minimum and maximum values, calculating correlations, generating scatter plots, and saving results.

## Next steps
- Learn Git and GitHub for version control.
- Learn basic Linux command-line operations.
- Add geographic coordinates and create a simple map of pit locations.
- Learn introductory remote-sensing workflows for environmental monitoring.