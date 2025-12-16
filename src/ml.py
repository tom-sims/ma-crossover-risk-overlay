from sklearn.ensemble import RandomForestClassifier

def add_regime_label(df, lookahead, neg_tol):
    future_returns = df['Returns'].rolling(lookahead).sum().shift(-lookahead)
    df['Regime'] = (future_returns > neg_tol).astype(int)
    return df

def train_regime_model(df, feature_cols, train_split):
    df = df.dropna().copy()
    split = int(len(df) * train_split)

    train, test = df.iloc[:split], df.iloc[split:]
    X_train, y_train = train[feature_cols], train['Regime']
    X_test = test[feature_cols]

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=5,
        min_samples_leaf=50,
        random_state=42
    )

    model.fit(X_train, y_train)

    df.loc[test.index, 'ML_Prob'] = model.predict_proba(X_test)[:, 1]
    df['ML_Prob'] = df['ML_Prob'].fillna(0)

    return df, model