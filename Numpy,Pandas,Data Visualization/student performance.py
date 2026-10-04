import pandas as pd

# Student data
data = {
    "Name": ["Arun", "Bala", "Divya", "Kavi", "Nisha", "Ravi", "Siva", "Priya"],
    "Department": ["CSE", "ECE", "CSE", "IT", "ECE", "CSE", "IT", "CSE"],
    "Marks": [85, 72, 91, 68, 78, 88, 55, 95],
    "Attendance": [90, 75, 85, 92, 78, 88, 70, 95]
}

df = pd.DataFrame(data)

# Display first 5 students
print("First 5 Students:")
print(df.head())

# Average marks
print("\nAverage Marks:", df["Marks"].import pandas as pd

# Product data
data = {
    "Product Name": ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"],
    "Price": [50000, 20000, 15000, 2000, 1500],
    "Quantity Sold": [10, 60, 30, 80, 55]
}

df = pd.DataFrame(data)

# Calculate total sales
df["Total Sales"] = df["Price"] * df["Quantity Sold"]

print("Product Sales Data:")
print(df)

# Product with highest sales
highest_sales = df.loc[df["Total Sales"].idxmax()]

print("\nProduct with Highest Sales:")
print(highest_sales)

# Average product price
print("\nAverage Product Price:", df["Price"].mean())

# Products where quantity sold is greater than 50
print("\nProducts with Quantity Sold greater than 50:")
print(df[df["Quantity Sold"] > 50])

# Sort products based on total sales
print("\nProducts sorted by Total Sales:")
print(df.sort_values("Total Sales", ascending=False))mean())

# Students who scored more than 75
print("\nStudents with marks greater than 75:")
print(df[df["Marks"] > 75])

# Students whose attendance is below 80%
print("\nStudents with attendance below 80%:")
print(df[df["Attendance"] < 80])

# Sort students based on marks
print("\nStudents sorted by marks:")
print(df.sort_values("Marks"))
