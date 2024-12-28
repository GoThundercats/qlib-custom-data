# Qlib Custom Data Project

## Overview
Custom stock data analysis setup using Qlib, with support for CSV data conversion and visualization.

## Directory Structure
- `/data`: Location for CSV and converted bin files (not tracked in git)
- `/scripts`: Python scripts for data conversion and verification
- `/docker`: Docker-related files
- `/notebooks`: Jupyter notebooks for analysis

## Setup Instructions

### 1. Data Preparation
- Place your CSV file at: `/root/.qlib/csv_data/my_data/all_stock_data.csv`
- CSV must have columns: date, open, high, low, close, volume, factor

### 2. Convert Data
Run the conversion script in your Qlib container:
```bash
python scripts/dump_bin.py