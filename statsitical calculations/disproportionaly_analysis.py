import math

def reporting_ratio(contingency_table):
    DE = contingency_table[0][0]
    De = contingency_table[1][0]
    D = De + DE
    reporting_rate = DE / D
    return reporting_rate
def relative_reporting_ratio(contingency_table):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    D = De + DE
    E = dE + DE
    N = de + DE + De + dE
    rrr = (DE * N) / (D * E)
    return rrr

def proportional_reporting_ratio(contingency_table):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    D = De + DE
    d = dE + de
    prr = (DE / D) / (dE / d)
    return prr

def reporting_odds_ratio(contingency_table):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    ror = (DE / De) / (dE / de)
    return ror
def chi_square_yates(contingency_table):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    D = De + DE
    E = dE + DE
    N = de + DE + De + dE
    d = dE + de
    e = De + de
    chi_square_yates = (N * (abs(DE * de - dE * De) - N / 2) ** 2) / (D * d * E * e)
    return chi_square_yates

def sd_rrr(contingency_table):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    D = De + DE
    E = dE + DE
    N = de + DE + De + dE
    e = De + de

    sd_rrr = math.sqrt(De / (DE * D) + e / (E * N))
    return sd_rrr

def sd_prr(contingency_table):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    D = De + DE
    d = dE + de
    sd_prr = math.sqrt(De / (DE * D) + de / (dE * d))
    return sd_prr

def sd_ror(contingency_table):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    sd_ror = math.sqrt(1/DE + 1/De + 1/dE + 1/de)
    return sd_ror

def confidence_interval(FM , sd_FM):
    ln_FM = math.log(FM)
    ci_lower = math.exp(ln_FM - 1.96 * sd_FM)
    ci_upper = math.exp(ln_FM + 1.96 * sd_FM)
    return ci_lower, ci_upper

def information_component(contingency_table):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    D = De + DE
    E = dE + DE
    N = de + DE + De + dE
    rrr = (DE * N) / (D * E)
    IC = math.log2(rrr)
    return IC

def confidence_interval_information_component(contingency_table, IC):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    D = De + DE
    E = dE + DE
    N = de + DE + De + dE
    gamma = 1 / (E/N) * (D/N)
    var = ((1 / math.log(2)) ** 2) * (((N - DE + gamma - 1) / ((DE + 1) * (1 + N + gamma))) + ((N - E + 1)/((E + 1)*(N+ 3 ))) + ((N - D + 1) / ((D + 1) * (N + 3))))
    #var = (1 / math.log2((N - DE + gamma - 1) / ((DE + 1) * (1 + N + gamma))) + (1 / math.log2((N - E + 1)/((E + 1)*(N + 3)))) + (1 / math.log2((N - D + 1) / ((D + 1) * (N + 3)))))
    ci_lower = IC - var
    ci_upper = IC + var
    return ci_lower, ci_upper

#Uncomment for test runs with specific values
'''def main():
    # Given contingency table
    contingency_table = [
        [9, 938],
        [16946, 2547122] # De, de
    ]
    print("Reporting Rate:", reporting_ratio(contingency_table))
    print("Relative Reporting Rate:", relative_reporting_ratio(contingency_table))
    print("Proportional Reporting Rate:", proportional_reporting_ratio(contingency_table))
    print("Reporting Odds Ratio:", reporting_odds_ratio(contingency_table))
    print("Chi-Square Yates:", chi_square_yates(contingency_table))
    print("Standard Deviation RRR:", sd_rrr(contingency_table))
    print("Standard Deviation PRR:", sd_prr(contingency_table))
    print("Standard Deviation ROR:", sd_ror(contingency_table))
    print("Confidence Interval RRR:", confidence_interval(relative_reporting_ratio(contingency_table), sd_rrr(contingency_table)))
    print("Confidence Interval ROR:", confidence_interval(reporting_odds_ratio(contingency_table), sd_ror(contingency_table)))
    print("Confidence Interval PRR:", confidence_interval(proportional_reporting_ratio(contingency_table), sd_prr(contingency_table)))
    print("Information Component:", information_component(contingency_table))
    print("Confidence Interval Information Component:", confidence_interval_information_component(contingency_table, information_component(contingency_table)))

if __name__ == "__main__":
    main()'''
