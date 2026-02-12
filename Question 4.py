import pandas as pd
# Load the dataset into a DataFrame
df = pd.read_csv("student.csv")
# Filter the data based on the required conditions:
# studytime >= 3
# internet == 1 (student has internet access)
# absences <= 5
filtered_df = df[(df['studytime'] >= 3) & (df['internet'] == 1) & (df['absences'] <= 5)]
# Save the filtered results to a new CSV file
# index=False ensures row numbers are not added to the file
filtered_df.to_csv("high_engagement.csv", index = False)
# Compute the number of selected students and their average grade
num_students = len(filtered_df)              # Count how many rows remain after filtering
average_grade = filtered_df['grade'].mean()  # Compute mean grade
# Print the results in a clear format
print(f"Number of students saved: {num_students}")
print(f"Average grade: {average_grade:.2f}")
