# Creation of the WACC and CAPM Function

#  WACC = Weighted Average Cost of Capital
#  CAPM = Capital Asset Pricing Model = Cost of Equity

def WACC_CAPM(Total_Assets, Debt, Interest_on_Debt, Tax, Beta, Market_Premium, Risk_Free_Rate):
    equity = Total_Assets - Debt
    re = Risk_Free_Rate
    ke = re + Beta * (Market_Premium - re)
    Debt_ratio = Debt / Total_Assets
    Equity_ratio = equity / Total_Assets
    WACC = (Interest_on_Debt * (1 - Tax) * Debt_ratio) + (ke * Equity_ratio)
    WACC_percent = WACC * 100
    ke_percent = ke * 100
    return "WACC: {:.2f}%".format(WACC_percent), "CAPM: {:.2f}%".format(ke_percent)


# Sample Input

Total_Assets = 100  # Total assets of the company
Debt = 30  # Total debt outstanding of the company
Interest_on_Debt = 0.09  # Interest rate on debt
Tax = 0.35  # Corporate Tax Rate
Beta = 1.5  # Beta of the asset (Beta of 1 == S&P 500)
Market_Premium = 0.10  # Market risk premium
Risk_Free_Rate = 0.03   # Risk-free rate (For example, a 6-month US Treasury Bill annualized)

print(WACC_CAPM(Total_Assets, Debt, Interest_on_Debt, Tax, Beta, Market_Premium, Risk_Free_Rate))

# Output:
# WACC: 11.21%
# CAPM: 13.50%
