import numpy as np
from pymongo import MongoClient
import disproportionaly_analysis
import timeit

# Start total runtime timer
start_time = timeit.default_timer()

# Connect to MongoDB and select collection
client = MongoClient("mongodb://localhost:27017/")
db = client["vaers"]
collection = db["combinations"]

# Define the query parameters
vaccine = "COVID19-2"
manufacturer = "MODERNA"
symptom = "Transfusion"

# Execute the MongoDB query
db_query_start_time = timeit.default_timer()
result = collection.find_one({"vaccine": vaccine, "manufacturer": manufacturer, "symptom": symptom})
db_query_elapsed_time = (timeit.default_timer() - db_query_start_time) * 1000  # Convert to milliseconds

# Extract values from the result
DE = result.get("DE")
dE = result.get("dE")
De = result.get("De")
de = result.get("de")

# Create the contingency table
contingency_table = [
    [DE, dE],
    [De, de]
]

# Define a function to time each query
def time_query(query_func):
    start_time = timeit.default_timer()
    result = query_func(contingency_table)
    elapsed_time = (timeit.default_timer() - start_time) * 1000  # Convert to milliseconds
    return result, elapsed_time

# Time each query
rrr, rrr_time = time_query(disproportionaly_analysis.relative_reporting_ratio)
ror, ror_time = time_query(disproportionaly_analysis.reporting_odds_ratio)
prr, prr_time = time_query(disproportionaly_analysis.proportional_reporting_ratio)
chi_square, chi_square_time = time_query(disproportionaly_analysis.chi_square_yates)
information_component, information_component_time = time_query(disproportionaly_analysis.information_component)

# Print results
print("DB Query time (ms):", db_query_elapsed_time)
print("rrr query:", rrr)
print("rrr query time (ms):", rrr_time)
print("ror query:", ror)
print("ror query time (ms):", ror_time)
print("prr query:", prr)
print("prr query time (ms):", prr_time)
print("chi-square-yates:", chi_square)
print("chi-square-yates time (ms):", chi_square_time)
print("information_component:", information_component)
print("information_component time (ms):", information_component_time)

# Total runtime
total_runtime = (timeit.default_timer() - start_time) * 1000  # Convert to milliseconds
print("Total runtime:", "{:.2f} ms".format(total_runtime))
