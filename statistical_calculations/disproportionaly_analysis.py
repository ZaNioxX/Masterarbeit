import math


def reporting_ratio(contingency_table):
    DE = contingency_table[0][0]
    De = contingency_table[1][0]
    D = DE + De

    if D == 0:
        return 0
    reporting_rate = DE / D
    return reporting_rate


def relative_reporting_ratio(contingency_table):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    D = De + DE
    E = dE + DE
    if D == 0 or E == 0:
        return 0
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
    if dE == 0:
        return 0
    prr = (DE / D) / (dE / d)
    return prr


def reporting_odds_ratio(contingency_table):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    if dE == 0 or De == 0:
        return 0
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
    if D == 0 or d == 0 or E == 0 or e == 0:
        return 0
    chi_square_y = (N * (abs(DE * de - dE * De) - N / 2) ** 2) / (D * d * E * e)
    return chi_square_y


def sd_rrr(contingency_table):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    D = De + DE
    E = dE + DE
    N = de + DE + De + dE
    e = De + de
    if DE == 0 or D == 0 or E == 0 or N == 0 or e == 0:
        return 0
    sd_rrr = math.sqrt(De / (DE * D) + e / (E * N))
    return sd_rrr


def sd_prr(contingency_table):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    D = De + DE
    d = dE + de
    if DE == 0 or D == 0 or dE == 0 or d == 0:
        return 0
    sd_prr = math.sqrt(De / (DE * D) + de / (dE * d))
    return sd_prr


def sd_ror(contingency_table):
    DE = contingency_table[0][0]
    dE = contingency_table[0][1]
    De = contingency_table[1][0]
    de = contingency_table[1][1]
    if DE == 0 or dE == 0 or De == 0 or de == 0:
        return 0
    sd_ror = math.sqrt(1/DE + 1/De + 1/dE + 1/de)
    return sd_ror


def confidence_interval(FM, sd_FM):
    if FM == 0 or sd_FM == 0:
        return 0, 0
    ln_FM = math.log(FM)
    ci_lower = math.exp(ln_FM - 1.96 * sd_FM)
    ci_upper = math.exp(ln_FM + 1.96 * sd_FM)
    return ci_lower, ci_upper


def information_component(contingency_table):
    rrr = relative_reporting_ratio(contingency_table)
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
    var = ((1 / math.log(2)) ** 2) * (((N - DE + gamma - 1) / ((DE + 1) * (1 + N + gamma))) +
                                      ((N - E + 1)/((E + 1)*(N + 3))) + ((N - D + 1) / ((D + 1) * (N + 3))))
    ci_lower = IC - var
    ci_upper = IC + var
    return ci_lower, ci_upper


def get_signal(contingency_table, method, confidence='chi2'):
    if method == 'rrr' and confidence == 'chi2':
        rrr = relative_reporting_ratio(contingency_table)
        chi_square = chi_square_yates(contingency_table)
        return rrr > 2 and chi_square > 3.841

    if method == 'prr' and confidence == 'chi2':
        prr = proportional_reporting_ratio(contingency_table)
        chi_square = chi_square_yates(contingency_table)
        return prr > 2 and chi_square > 3.841

    if method == 'ror' and confidence == 'chi2':
        ror = reporting_odds_ratio(contingency_table)
        chi_square = chi_square_yates(contingency_table)
        return ror > 2 and chi_square > 3.841


    if method == 'ic' and confidence == 'chi2':
        ic = information_component(contingency_table)
        chi_square = chi_square_yates(contingency_table)
        return ic > 0 and chi_square > 3.841


    if method == 'rrr' and confidence == 'ci':
        rrr = relative_reporting_ratio(contingency_table)
        sdrrr = sd_rrr(contingency_table)
        rrr_ci_lower, rrr_ci_upper = confidence_interval(rrr, sdrrr)
        return rrr_ci_lower > 1


    if method == 'prr' and confidence == 'ci':
        prr = proportional_reporting_ratio(contingency_table)
        sdprr = sd_prr(contingency_table)
        prr_ci_lower, prr_ci_upper = confidence_interval(prr, sdprr)
        return prr_ci_lower > 1


    if method == 'ror' and confidence == 'ci':
        ror = reporting_odds_ratio(contingency_table)
        sdror = sd_ror(contingency_table)
        ror_ci_lower, ror_ci_upper = confidence_interval(ror, sdror)
        return ror_ci_lower > 1


    if method == 'ic' and confidence == 'ci':
        ic = information_component(contingency_table)
        ic_ci_lower, ic_ci_upper = confidence_interval_information_component(
            contingency_table, ic)
        return ic_ci_lower > 0



#Uncomment for test runs with specific values
def main():
    # Given contingency table
    contingency_table = [
        [12559, 3757],
        [931630, 1617069] # De, de
    ]


    print("Reporting Rate:", reporting_ratio(contingency_table))
    print("Relative Reporting Rate:", relative_reporting_ratio(contingency_table))
    print("Proportional Reporting Rate:", proportional_reporting_ratio(contingency_table))
    print("Reporting Odds Ratio:", reporting_odds_ratio(contingency_table))
    print("Chi-Square Yates:", chi_square_yates(contingency_table))
    print("Standard Deviation RRR:", sd_rrr(contingency_table))
    print("Standard Deviation PRR:", sd_prr(contingency_table))
    print("Standard Deviation ROR:", sd_ror(contingency_table))
    print("Confidence Interval RRR:", confidence_interval(relative_reporting_ratio(contingency_table),
                                                          sd_rrr(contingency_table)))
    print("Confidence Interval ROR:", confidence_interval(reporting_odds_ratio(contingency_table),
                                                          sd_ror(contingency_table)))
    print("Confidence Interval PRR:", confidence_interval(proportional_reporting_ratio(contingency_table),
                                                          sd_prr(contingency_table)))
    print("Information Component:", information_component(contingency_table))
    print("Confidence Interval Information Component:", confidence_interval_information_component(contingency_table,
                                                                              information_component(contingency_table)))


if __name__ == "__main__":
    main()
