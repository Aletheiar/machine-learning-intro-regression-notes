
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

rng = np.random.default_rng(42)
area = rng.uniform(45, 140, size=120)
age = rng.uniform(0, 25, size=120)
distance = rng.uniform(1, 15, size=120)
X = np.column_stack([area, age, distance])
noise = rng.normal(0, 12, size=120)
y = 30 + 2.8 * area - 1.5 * age - 4.0 * distance + noise

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
models = {
    "mean": None,
    "linear": LinearRegression(),
    "ridge": make_pipeline(StandardScaler(), Ridge(alpha=10.0)),
    "knn": make_pipeline(StandardScaler(), KNeighborsRegressor(n_neighbors=5)),
}
for name, model in models.items():
    if model is None:
        pred = np.full(len(y_test), y_train.mean())
    else:
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, pred)
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    r2 = r2_score(y_test, pred)
    print(name, "MAE", round(mae, 2), "RMSE", round(rmse, 2), "R2", round(r2, 3))

# Only train folds are used during parameter selection.
search = GridSearchCV(
    make_pipeline(StandardScaler(), KNeighborsRegressor()),
    {"kneighborsregressor__n_neighbors": [3, 5, 9, 15]},
    scoring="neg_mean_absolute_error", cv=5
)
search.fit(X_train, y_train)
print("selected K:", search.best_params_)
print("test MAE:", mean_absolute_error(y_test, search.predict(X_test)))
