import unittest
import sys
import pandas as pd
sys.path.insert(0,'../scripts/')

from data_fetch import get_data


class TestCases(unittest.TestCase):
   
    
    def test_input_value(self):
        """
        Provide an assertion level for arg input
        """
        
        
        assert type(get_data('data/train_processed.csv','C:/Users/User/Desktop/Pharmaceutical-Sales-Prediction','train_processed_v1')) is pd.DataFrame



if __name__ == '__main__':
    unittest.main()
