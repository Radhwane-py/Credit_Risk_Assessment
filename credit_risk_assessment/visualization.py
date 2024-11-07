import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import auc, roc_curve
import pandas as pd

# Plot distributions.
def plot_distributions(df):
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(df['credit_score'], bins=10, kde=True)
    plt.title('Distribution of Credit Scores')
    plt.subplot(1, 2, 2)
    sns.histplot(df['loan_amount'], bins=10, kde=True)
    plt.title('Distribution of Loan Amounts')
    plt.savefig('Distribution of Loan Amounts.png')
    plt.show()

# Plot correlation matrix.
def plot_correlation_matrix(df):
    plt.figure(figsize=(10, 8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.savefig('Correlation Matrix.png')
    plt.show()

# Plot feature importances if Random Forest is the best model.
def plot_feature_importances(model, X_train):
    feature_importances = pd.Series(model.feature_importances_, index=X_train.columns)
    feature_importances.sort_values(ascending=False).plot(kind='bar')
    plt.title('Feature Importances')
    plt.savefig('Feature Importances.png')
    plt.show()

# Plot Receiver Operating Characteristic (ROC) curve.
def plot_roc_curve(y_test, y_pred):
    fpr, tpr, _ = roc_curve(y_test, y_pred)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC)')
    plt.legend(loc='lower right')
    plt.savefig('Receiver Operating Characteristic.png')
    plt.show()
