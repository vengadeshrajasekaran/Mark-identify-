from sklearn.linear_model import LogisticRegression

# Training data
X = [[80], [50], [30], [90]]  # Marks
y = [1, 0, 0, 1]              # 1 = Pass, 0 = Fail

model = LogisticRegression()
model.fit(X, y)

# Test
mark = int(input("Enter your marks: "))
pred = model.predict([[mark]])
print("Result: Pass" if pred[0]==1 else "Fail")