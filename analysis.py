# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv(r"C:\Users\Divya\Downloads\student_analysis\student_dataset_cleaned.csv")

print("First 5 Records")
print(df.head())

# 2. Dataset information and summary statistics
print("\nDataset Information")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

# 3. Find missing values and handle them
print("\nMissing Values")
print(df.isnull().sum())

# Fill missing numerical values with mean
numeric_cols = ['Attendance (%)', 'Internal Marks', 'External Marks', 'Assignment Marks']

for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# Fill missing categorical values with mode
categorical_cols = ['Gender', 'Department', 'Final Grade']

for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# 4. Remove duplicate records
df.drop_duplicates(inplace=True)

print("\nDuplicate Records Removed")

# 5. Create Total Marks column
df["Total Marks"] = (
    df["Internal Marks"] +
    df["External Marks"] +
    df["Assignment Marks"]
)

# 6. Create Result column
df["Result"] = df["Total Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("\nUpdated Dataset")
print(df.head())

# 7. Top 10 students based on Total Marks
print("\nTop 10 Students")
top10 = df.sort_values(by="Total Marks", ascending=False).head(10)
print(top10[["Student_ID", "Name", "Total Marks"]])

# 8. Department-wise average marks
print("\nDepartment-wise Average Marks")
dept_avg = df.groupby("Department")["Total Marks"].mean()
print(dept_avg)

# 9. Students with attendance below 75%
print("\nStudents with Attendance Below 75%")
low_attendance = df[df["Attendance (%)"] < 75]
print(low_attendance[["Student_ID", "Name", "Attendance (%)"]])

# 10. Count students in each grade
print("\nGrade Count")
grade_count = df["Final Grade"].value_counts()
print(grade_count)

# =======================
# Graph 1: Bar Chart (Blue)
# =======================
plt.figure(figsize=(8,5))
dept_avg.plot(kind="bar", color="blue")
plt.title("Department-wise Average Marks")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.grid(axis="y")
plt.show()

# =======================
# Graph 2: Pie Chart (Default Colors)
# =======================
plt.figure(figsize=(6,6))
grade_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Grade Distribution")
plt.ylabel("")
plt.show()

# =======================
# Graph 3: Histogram (Green)
# =======================
plt.figure(figsize=(8,5))
plt.hist(df["Total Marks"], bins=10, color="green")
plt.title("Total Marks Distribution")
plt.xlabel("Total Marks")
plt.ylabel("Number of Students")
plt.grid()
plt.show()

# =======================
# Graph 4: Scatter Plot (Red)
# =======================
plt.figure(figsize=(8,5))
plt.scatter(df["Attendance (%)"], df["Total Marks"], color="red")
plt.title("Attendance vs Total Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Total Marks")
plt.grid()
plt.show()

# =======================
# Graph 5: Line Chart (Purple)
# =======================
semester_avg = df.groupby("Semester")["Total Marks"].mean()

plt.figure(figsize=(8,5))
plt.plot(
    semester_avg.index,
    semester_avg.values,
    marker="o",
    color="purple",
    linewidth=2
)
plt.title("Average Marks by Semester")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.grid()
plt.show()

# Save cleaned dataset
df.to_csv("student_dataset_cleaned.csv", index=False)

print("\nAnalysis Completed Successfully!")