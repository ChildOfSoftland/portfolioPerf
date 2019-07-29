import unittest
import pandas as pd
from portfolioPerf import PortfolioPerformance

class Test_test_portfolioPerf(unittest.TestCase):
    def test_asset_performance(self):
        P = pd.Series([1.000000, 1.007755, 1.015940, 1.019302], index = pd.date_range('20140113', '20140116'))
        self.assertTrue((PortfolioPerformance.calculate_asset_performance('20140113', '20140116') == P).bool)

    def test_currency_performance(self):
        CP = pd.Series([1.000000, 0.999568, 0.997234, 0.997369], index = pd.date_range('20140113', '20140116'))
        self.assertTrue((PortfolioPerformance.calculate_currency_performance('20140113', '20140116') == CP).bool)

    def test_total_performance(self):
        TP = pd.Series([1.000000, 0.999568, 0.997234, 0.997369], index = pd.date_range('20140113', '20140116'))
        self.assertTrue((PortfolioPerformance.calculate_total_performance('20140113', '20140116') == TP).bool)

if __name__ == '__main__':
    unittest.main()
