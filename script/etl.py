import pandas as pd

# Extract
with open('../data/sample_log.txt', 'r') as file:
    logs = file.readlines()

# Transform (ambil error aja)
error_logs = [log.strip() for log in logs if "ERROR" in log]

# Convert ke DataFrame
df = pd.DataFrame(error_logs, columns=["error_log"])

# Load (simpan ke CSV)
df.to_csv('../output/error_logs.csv', index=False)

print("ETL process selesai, data disimpan di output/error_logs.csv")