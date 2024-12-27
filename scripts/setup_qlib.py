import qlib
from qlib.data import D

def init_qlib_environment():
    """Initialize Qlib with custom dataset"""
    qlib.init(
        provider_uri="/root/.qlib/qlib_data/my_data",
        expression_cache=None,
        dataset_cache=None
    )
    
def verify_data_access():
    """Verify we can access the data"""
    try:
        fields = ["$open", "$high", "$low", "$close", "$volume", "$factor"]
        df = D.features(
            instruments=["ALL_STOCK_DATA"],
            fields=fields,
            start_time='2020-01-02',
            end_time='2020-12-31',
            freq="day"
        )
        print("Data access successful!")
        print("\nSample data:")
        print(df.head())
        return True
    except Exception as e:
        print(f"Error accessing data: {e}")
        return False

if __name__ == "__main__":
    init_qlib_environment()
    verify_data_access()