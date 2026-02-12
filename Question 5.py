import pandas as pd
# 1. Load the dataset
df = pd.read_csv("student.csv")
# 2. Create a new categorical column called 'grade_band'
def assign_grade_band(grade):
    if grade <= 9:
        return "Low"
    elif grade <= 14:
        return "Medium"
    else:
        return "High"
df["grade_band"] = df["grade"].apply(assign_grade_band)
# 3. Create a grouped summary table by grade_band
summary = df.groupby("grade_band").agg(
    number_of_students=("grade", "count"),
    average_absences=("absences", "mean"),
    percent_with_internet=("internet", "mean"))
# Convert proportion to percentage
summary["percent_with_internet"] = summary["percent_with_internet"] * 100
# 4. Save the summary table to a CSV file
summary.to_csv("student_bands.csv")
# 5. Print the summary table
print(summary)
