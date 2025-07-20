# 🚗 Car Stock Dashboard

This project is a **Streamlit**-based interactive dashboard for visualizing and analyzing car stock data. The dashboard allows users to filter and explore car prices, manufacturers, and key statistics in a visually appealing and intuitive interface using **Plotly** visualizations.

## 📁 Project Structure

```
📦 Car Stock Dashboard
 ┣ 📄 first Dashboard.py
 ┣ 📄 cars.csv (not included)
 ┗ 📄 README.md
```

## 🚀 Features

- Interactive sidebar filters:
  - **Manufacturer**
  - **Automation Type**
  - **Foreign/Local Used**
- Key Performance Indicators (KPIs):
  - Average price (in USD)
  - Total number of cars
  - Earliest make year
  - Min/Max/Median price
- Visualizations:
  - Bar chart of **Price per Color**
  - Bar chart of **Price per Manufacturer**
  - Pie chart of **Seat Make Distribution**
  - Histogram of **Make Year Distribution**

## 🧠 Technologies Used

- **Python 3**
- **Streamlit** - UI and dashboard rendering
- **Plotly Express** - Interactive visualizations
- **Pandas & NumPy** - Data handling and transformation

## 📝 Setup Instructions

1. **Clone the Repository** or copy the `.py` script.
2. Ensure you have the required libraries:
   ```bash
   pip install streamlit pandas numpy plotly
   ```
3. Make sure the `cars.csv` file is located at the correct path:
   ```
   C:/Users/acer/Downloads/cars.csv
   ```
   Or update the file path in the script accordingly.

4. **Run the dashboard**:
   ```bash
   streamlit run "first Dashboard.py"
   ```

## 📌 Notes

- Prices are displayed in **USD** (converted from local currency assuming 1 USD = ₹80).
- Default theme and background have been customized.
- Created by: **Subhash Tiwari**
