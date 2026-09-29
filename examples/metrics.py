
y_true = [3, 5, 2]
y_pred = [2, 5, 4]
n = len(y_true)
errors = [a - b for a, b in zip(y_true, y_pred)]
mae = sum(abs(e) for e in errors) / n
mse = sum(e * e for e in errors) / n
rmse = mse ** 0.5
y_mean = sum(y_true) / n
tss = sum((y - y_mean) ** 2 for y in y_true)
r2 = 1 - sum(e * e for e in errors) / tss
print(mae, mse, rmse, r2)
# Expected: 1.0, 1.666..., 1.29099..., -0.071428...
