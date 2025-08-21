import pandas as pd

data = {
    "Transaction_ID": [1001, 1002, 1003, 1004, 1005, 1006],
    "Customer_Name": ["Ahmed Ali", "Sara Omar", "Ali Saleh", 
                      "Nada Hassan", "Omar Khalid", "Ahmed Ali"],
    "Age": [28, None, 35, 42, None, 28],
    "Email": ["ahmed@mail.com", "sara@mail.com", None, 
              "nada@mail.com", "omar@mail.com", "ahmed@mail.com"],
    "Join_Date": ["2025-01-10", "2025-02-15", "2025-03-20", 
                  None, "2025-05-05", "2025-01-10"],
    "Total_Purchase": [250, 300, 150, 400, 200, 250]
}

df = pd.DataFrame(data)

# (1) تحويل عمود Join_Date إلى تاريخ
df["Join_Date"] = pd.to_datetime(df["Join_Date"])


# (2) تحديد الصفوف التي تحتوي على أكثر من قيمة فارغة
rows_with_many_nulls = df[df.isnull().sum(axis=1) > 1]


# (3) التحقق من عدد الصفوف والأعمدة
print(df.shape)


# (4) التحقق من أسماء الأعمدة ونوع البيانات وعدد القيم المفقودة في كل عمود
print(df.info())
print(df.isnull().sum())


# (5) استخراج الصفوف التي العمر فيها أقل من 30
rows_age_less_30 = df[df["Age"] < 30]


# (6) حذف الصفوف التي تحتوي على قيم فارغة
df_no_nulls = df.dropna()


# (7) استبدال القيم الفارغة في عمود Age بمتوسط العمر
df["Age"].fillna(df["Age"].mean(), inplace=True)


# (8) استبدال القيم الفارغة في عمود Total_Purchase بالرقم 0
df["Total_Purchase"].fillna(0, inplace=True)


# (9) إزالة الصفوف المكررة
df_no_duplicates = df.drop_duplicates()
duplicates = df[df.duplicated()]