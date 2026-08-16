# Simple Machine Learning Example

from sklearn.linear_model import LinearRegression

# Training data
X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make a prediction
prediction = model.predict([[5]])

print("Prediction for 5:", prediction[0])