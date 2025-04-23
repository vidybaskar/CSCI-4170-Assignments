
#GEOMAGNETIC DATA
"""
import pandas as pd

# Define input and output file paths
input_file = 'Geomagnetic and Solar Indicies.txt'  # Change this to your actual filename
output_file = 'data.csv'

# Read the file using whitespace as delimiter (handles multiple spaces)
df = pd.read_csv(input_file, delim_whitespace=True, header=None)

# Optionally, assign column names (if known). Here’s an example structure:
columns = [
    'Year', 'Month', 'Day', 'JulianDayStart', 'JulianDayEnd', 'StationID', 'DayOfYear',
    'Val1', 'Val2', 'Val3', 'Val4', 'Val5', 'Val6', 'Val7', 'Val8',
    'Count1', 'Count2', 'Count3', 'Count4', 'Count5', 'Count6', 'Count7', 'Count8',
    'Sum1', 'Sum2', 'TempMax', 'TempMin', 'Flag'
]
df.columns = columns

# Save to CSV
df.to_csv(output_file, index=False)

print(f"Data successfully written to {output_file}")
"""
#SOLAR FLARE DATA
"""
import csv

# Define the fixed columns for the flare dataset.
fixed_columns = [
    "Flare", "Start_Date", "Start_Time", "Peak_Time", "End_Time",
    "Duration", "Peak_Cps", "Total_Counts", "Energy_Range",
    "X_Pos", "Y_Pos", "Radial", "AR"
]

# Define the flag codes (all uppercase).
flag_codes = [
    "A0", "A1", "A2", "A3", "DF", "DR", "ED", "EE", "ES",
    "FE", "FR", "FS", "GD", "GE", "GS", "MR", "NS", "PE", "PS",
    "PN", "QN", "SD", "SE", "SS"
]

# All CSV columns: fixed fields + one column per flag code.
csv_columns = fixed_columns + flag_codes

# Input and output file paths.
input_file = "solarflare.txt"
output_file = "hessi_flare_list.csv"

# Function to parse a single line.
def parse_flare_line(line):
    # Split by whitespace. This assumes fields are separated by one or more spaces.
    tokens = line.strip().split()
    
    # Ensure there are at least 13 tokens for the fixed columns.
    if len(tokens) < 13:
        return None  # or raise an error
    
    # Extract the fixed fields.
    fixed_data = {
        "Flare": tokens[0],
        "Start_Date": tokens[1],
        "Start_Time": tokens[2],
        "Peak_Time": tokens[3],
        "End_Time": tokens[4],
        "Duration": tokens[5],
        "Peak_Cps": tokens[6],
        "Total_Counts": tokens[7],
        "Energy_Range": tokens[8],
        "X_Pos": tokens[9],
        "Y_Pos": tokens[10],
        "Radial": tokens[11],
        "AR": tokens[12]
    }
    
    # Initialize flag columns to 0.
    flags_data = {flag: 0 for flag in flag_codes}
    
    # All remaining tokens (if any) are flag tokens.
    flag_tokens = tokens[13:]
    
    for token in flag_tokens:
        token_upper = token.upper()
        
        # Check for exact matches for flag codes that are two or more letters.
        if token_upper in flag_codes:
            flags_data[token_upper] = 1
        else:
            # For flags like P1 or Q1, map them to PN or QN.
            if token_upper.startswith("P") and len(token_upper) == 2 and token_upper[1].isdigit():
                flags_data["PN"] = 1
            elif token_upper.startswith("Q") and len(token_upper) == 2 and token_upper[1].isdigit():
                flags_data["QN"] = 1
            # You can add additional pattern matching here if needed.
    
    # Merge fixed data and flag data.
    combined = {**fixed_data, **flags_data}
    return combined

# Read the input file, parse each line, and write out to CSV.
parsed_rows = []
with open(input_file, "r") as f:
    for line in f:
        # Skip blank lines.
        if not line.strip():
            continue
        parsed = parse_flare_line(line)
        if parsed:
            parsed_rows.append(parsed)

# Write to CSV.
with open(output_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for row in parsed_rows:
        writer.writerow(row)

print(f"CSV file '{output_file}' has been created with {len(parsed_rows)} rows.")
"""
#SOLAR WIND DATA
"""
import csv

# Define column names for the solar wind dataset.
csv_columns = [
    "YYYY", "DOY", "HR", "MN",
    "Field_Magnitude_nT",
    "BZ_GSM_nT",
    "Speed_km_s",
    "Proton_Density_ncc",
    "Flow_Pressure_nPa",
    "Electric_Field_mVm"
]

# List of known fill/missing value markers.
missing_values = {"99999.9", "999.99", "99.99", "999.9", "9999.9"}

# Input and output file paths.
input_file = "Solar_Wind_Data.txt"    # Replace with your actual file name
output_file = "solarwind_data.csv"

# Function to parse a single line of the solar wind data.
def parse_solarwind_line(line):
    tokens = line.strip().split()
    
    # Pad the row if it's too short (e.g. missing final fields).
    if len(tokens) < 10:
        tokens += [None] * (10 - len(tokens))
    
    # Convert tokens and replace known bad values with None (to become NaN in CSV).
    parsed = {}
    for col, token in zip(csv_columns, tokens):
        if token in missing_values or token is None:
            parsed[col] = None
        else:
            try:
                parsed[col] = float(token) if '.' in token or 'e' in token.lower() else int(token)
            except ValueError:
                parsed[col] = None  # Fallback if parsing fails

    return parsed

# Read input, parse lines, and write to CSV.
parsed_rows = []

with open(input_file, "r") as f:
    for line in f:
        if not line.strip():
            continue  # Skip empty lines
        parsed = parse_solarwind_line(line)
        parsed_rows.append(parsed)

# Write to CSV file.
with open(output_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for row in parsed_rows:
        writer.writerow(row)

print(f"CSV file '{output_file}' has been created with {len(parsed_rows)} rows.")
    """
import pandas as pd

# Path to your CSV file
csv_path = "Data/hessi_flare_list.csv"

# Step 1: Read the CSV
hessi = pd.read_csv(csv_path)

# Step 2: Parse 'Start_Date' and combine with time columns to form datetimes
hessi["Start_Date"] = pd.to_datetime(hessi["Start_Date"], errors="coerce")
for col in ["Start_Time", "Peak_Time", "End_Time"]:
    hessi[col] = pd.to_datetime(hessi["Start_Date"].dt.date.astype(str) + " " + hessi[col], errors="coerce")

# Step 3: Convert numeric columns
numeric_cols = [
    "Duration", "Peak_Cps", "Total_Counts", "X_Pos", "Y_Pos", "Radial", "AR",
    "A0", "A1", "A2", "A3", "DF", "DR", "ED", "EE", "ES", "FE", "FR", "FS",
    "GD", "GE", "GS", "MR", "NS", "PE", "PS", "PN", "QN", "SD", "SE", "SS"
]

for col in numeric_cols:
    if col in hessi.columns:
        hessi[col] = pd.to_numeric(hessi[col], errors="coerce")

# Step 4: Replace 'Energy_Range' with 'Energy_Min' and 'Energy_Max'
if "Energy_Range" in hessi.columns:
    energy_split = hessi["Energy_Range"].str.extract(r"(?P<Energy_Min>\d+)-(?P<Energy_Max>\d+)")
    energy_split = energy_split.astype(float)
    insert_loc = hessi.columns.get_loc("Energy_Range")
    hessi = hessi.drop(columns=["Energy_Range"])
    for i, col_name in enumerate(["Energy_Min", "Energy_Max"]):
        hessi.insert(insert_loc + i, col_name, energy_split[col_name])

# Step 5: Save back to the same file
hessi.to_csv(csv_path, index=False)

# Step 6: Print final column types
print("✅ CSV cleaned and saved.\n\n🧪 Final column data types:\n")
print(hessi.dtypes)