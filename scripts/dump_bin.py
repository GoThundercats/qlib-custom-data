import os
import sys
import pandas as pd
from datetime import datetime

def dump_bin_csv():
    """
    Convert CSV to Qlib binary format
    CSV should have columns: date, open, high, low, close, volume, factor
    """
    source_dir = "/root/.qlib/csv_data/my_data"
    target_dir = "/root/.qlib/qlib_data/my_data"
    
    # Read CSV file
    csv_path = os.path.join(source_dir, "all_stock_data.csv")
    df = pd.read_csv(csv_path)
    
    # Ensure date is in correct format
    df['date'] = pd.to_datetime(df['date'])
    
    # Create necessary directories
    os.makedirs(os.path.join(target_dir, "calendars"), exist_ok=True)
    os.makedirs(os.path.join(target_dir, "instruments"), exist_ok=True)
    os.makedirs(os.path.join(target_dir, "features", "all_stock_data"), exist_ok=True)
    
    # Create calendar file
    calendar = sorted(df['date'].unique())
    with open(os.path.join(target_dir, "calendars", "day.txt"), "w") as f:
        for date in calendar:
            f.write(date.strftime("%Y-%m-%d") + "\n")
    
    # Create instruments file
    with open(os.path.join(target_dir, "instruments", "all.txt"), "w") as f:
        f.write(f"ALL_STOCK_DATA\t{calendar[0].strftime('%Y-%m-%d')}\t{calendar[-1].strftime('%Y-%m-%d')}")

    print("Created calendar and instruments files")
    
    # Convert data to binary format
    for col in ['open', 'high', 'low', 'close', 'volume', 'factor']:
        print(f"Converting {col} data...")
        data = df[['date', col]].copy()
        data.columns = ['date', 'value']
        data.to_csv(os.path.join(target_dir, "features", "all_stock_data", f"{col}.day.bin"), 
                   index=False, header=None, sep="\t")
    
    print("Data conversion complete!")

if __name__ == "__main__":
    dump_bin_csv()