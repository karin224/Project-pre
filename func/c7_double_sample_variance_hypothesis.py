from scipy.stats import f as F_TEST


# hypo for both sided
def Variance_both_side(VAR1 = 1, tot1=100, VAR2 = 0.5, tot2=100, alpha=0.05):
    # return [alpha, p_value, variance of sample1, Event number of sample1, variance of sample2, Event number of sample2]
    # H0 : sigma1 = sigma2
    # H1 : sigma1 != sigma2
    F = VAR1 / VAR2;   #print(F)
    df1 = tot1-1; df2 = tot2-1;
    p_value = F_TEST.cdf(F, df1, df2)
    if(p_value>0.500):
        p_value = 1-p_value

    p025 = F_TEST.ppf(0.025, df1, df2)
    p975 = F_TEST.ppf(0.975, df1, df2)
    #print(p025, p975)
    return [alpha,p_value, VAR1, tot1, VAR2, tot2]
    # p_value < alpha --> Reject the null hypothesis that Var(X) == Var(Y)

def main():
    F_test = Variance_both_side(VAR1 = 10, tot1=1000, VAR2=10.7, tot2=1000)
    print(F_test)

if __name__=="__main__":
    main()

