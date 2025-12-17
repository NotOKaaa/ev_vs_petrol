# EV vs Petrol Car Total Cost of Ownership (TCO) Calculator
Exploratory cost simulation

A simple Python script that compares the total cost of ownership over a defined period (default: 6 years) between an electric vehicle (EV) and a petrol car, including:

- Purchase price difference
- Energy/fuel costs over time
- Fuel price inflation
- Resale value at the end
- Opportunity cost: what would happen if you invested the extra upfront cost of the EV (or the money saved by buying the cheaper petrol car) at a given annual return rate

The script also generates three simple plots for visualization.

## Why this calculator is useful
Buying an EV usually means a higher upfront cost, but lower running costs. This tool helps answer the question:  
**Over X years, which option is cheaper when accounting for fuel/electricity prices, inflation, resale, and the opportunity cost of money tied up in the more expensive car?**

The unique twist: the price difference is treated as an "investment" that grows at a specified return rate, while petrol fuel costs are subtracted from it each year (simulating the cash flow advantage of lower running costs).

## Requirements
- Python 3
- matplotlib (`pip install matplotlib`)

## How to use

1. Clone or download the repository
2. Run the script:

```bash
python ev_vs_petrol.py 
