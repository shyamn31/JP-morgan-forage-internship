import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    pass

def exercise_1(df):
    pass

def exercise_2(df, k):
    pass

def exercise_3(df, k):
    pass

def exercise_4(df):
    pass

def exercise_5(df):
    pass

def exercise_6(df):
    pass

def exercise_7(df):
    pass

def visual_1(df):
    pass

def visual_2(df):
    pass

def exercise_custom(df):
    pass
    
def visual_custom(df):
    pass
df = exercise_0('/content/input/transactions.csv')
def exercise_0(file):
    
    df = pd.read_csv(file)
    return df
def visual_1(df):
    def transaction_counts(df):
        return df['type'].value_counts()

    def transaction_counts_split_by_fraud(df):
        return df.groupby(['type', 'isFraud'])['type'].count().unstack()

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction Types')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Count')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction Type Split by Fraud')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Count')
    fig.suptitle('Transaction Analysis')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return 

visual_1(df)
def visual_2(df):
    def visual_custom(df):
  
      cash_out_df = df[df['type'] == 'CASH_OUT']

  
      plt.scatter(cash_out_df['oldbalanceOrg'] - cash_out_df['newbalanceOrig'], 
              cash_out_df['oldbalanceDest'] - cash_out_df['newbalanceDest'],
              alpha=0.5)  

      plt.xlabel('Origin Account Balance Delta')
      plt.ylabel('Destination Account Balance Delta')
      plt.title('Cash Out Transactions: Origin vs Destination Balance Delta')
      plt.grid(True)
      plt.show()

    visual_custom(df)
    return 

visual_2(df)
