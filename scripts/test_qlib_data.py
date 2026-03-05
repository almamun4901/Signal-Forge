import os
os.environ['JOBLIB_MMAP_MODE'] = 'r'  # Fix multiprocessing issues

import qlib
from qlib.config import REG_CN
from qlib.data import D

if __name__ == "__main__":
    print("Starting Qlib test")

    print("Import successful, now initializing...")

    qlib.init(provider_uri="~/.qlib/qlib_data/cn_data", region=REG_CN)

    print("Qlib initialized successfully")

    print("Getting instruments...")

    # Get list of available instruments
    instruments = D.instruments(market="csi500")  # Try with a smaller market instead of "all"

    print(f"Instruments type: {type(instruments)}")
    print(f"Instruments: {instruments}")

    # Convert to list if needed
    if hasattr(instruments, '__iter__') and not isinstance(instruments, (str, dict)):
        instruments_list = list(instruments)[:10]
        print(f"Using first 10 instruments: {instruments_list}")
    else:
        instruments_list = instruments

    print("Loading features...")

    df = D.features(
        instruments=instruments_list,
        fields=["$close", "$volume"],
        start_time="2020-01-01",
        end_time="2020-01-10",
    )

    print("Data loaded:")
    print(df.head())

    print("Test completed successfully")