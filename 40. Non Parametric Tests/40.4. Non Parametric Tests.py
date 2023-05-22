import scipy.stats as stats

# Mann-Whitney U test
def mann_whitney_u_test(data1, data2):
  """
  Performs a Mann-Whitney U test on two independent samples.

  Args:
    data1: The first sample.
    data2: The second sample.

  Returns:
    A tuple of the test statistic and the p-value.
  """

  u = stats.mannwhitneyu(data1, data2)
  p = u.pvalue

  return u, p

# Wilcoxon signed-rank test
def wilcoxon_signed_rank_test(data):
  """
  Performs a Wilcoxon signed-rank test on a paired sample.

  Args:
    data: The paired sample.

  Returns:
    A tuple of the test statistic and the p-value.
  """

  w = stats.wilcoxon(data)
  p = w.pvalue

  return w, p

# Kruskal-Wallis test
def kruskal_wallis_test(data):
  """
  Performs a Kruskal-Wallis test on more than two independent samples.

  Args:
    data: The data.

  Returns:
    A tuple of the test statistic, the degrees of freedom, and the p-value.
  """

  h = stats.kruskal_wallis(data)
  df = h.dof
  p = h.pvalue

  return h, df, p

# Friedman test
def friedman_test(data):
  """
  Performs a Friedman test on more than two dependent samples.

  Args:
    data: The data.

  Returns:
    A tuple of the test statistic, the degrees of freedom, and the p-value.
  """

  f = stats.friedmanchisquare(data)
  df = f.dof
  p = f.pvalue

  return f, df, p

# These are just a few examples of the many nonparametric tests that can be implemented in Python. The best test to use in a particular situation will depend on the specific research question and the characteristics of the data.
