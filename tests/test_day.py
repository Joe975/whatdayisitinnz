'''
Created on Jul 12, 2015

@author: hashtonmartyn
'''
import unittest
from nose.tools import raises
from whatdayisitinnz.day import Day, MOTHERS_DAY, CHRISTMAS, TODAY, WAITANGI_DAY, FATHERS_DAY, LABOUR_DAY, QUEENS_BIRTHDAY, NEW_YEARS_DAY
from pytz import timezone
from datetime import datetime


class TestDay(unittest.TestCase):

    def setUp(self):
        self.day = Day("someURL", "somename")
    
    @raises(AttributeError)
    def test_URL_can_not_change(self):
        self.day.URL = "someotherURL"
        
    @raises(AttributeError)
    def test_name_can_not_change(self):
        self.day.name = "someothername"

        
class TestSpecificDayBase(unittest.TestCase):
    
    def setUp(self):
        self.NZ_time = timezone("Pacific/Auckland") 
        self.sample_positive_days = []
        self.sample_negative_days = []
        self.offset_days = []
        
    def test_sample_negative_days_return_false(self):
        for sample_day in self.sample_negative_days:
            self.assertFalse(self.day.is_today(sample_day), sample_day)
            
    def test_sample_positive_days_return_true(self):
        for  sample_day in self.sample_positive_days:
            self.assertTrue(self.day.is_today(sample_day), sample_day)

    def test_offset_calculation(self):
        for sample_day in self.offset_days:
            day_date = self.day.is_date(sample_day["day"])
            self.assertEqual(self.day.calculate_offset(day_date, sample_day["day"]),
                             sample_day["offset"])

        
class TestMothersDay(TestSpecificDayBase):
    
    def setUp(self):
        super(TestMothersDay, self).setUp()
        self.day = MOTHERS_DAY
        self.sample_positive_days = (datetime(1990, 5, 13, tzinfo=self.NZ_time),
                                     datetime(1991, 5, 12, tzinfo=self.NZ_time),
                                     datetime(2000, 5, 14, tzinfo=self.NZ_time),
                                     datetime(2008, 5, 11, tzinfo=self.NZ_time),
                                     datetime(2010, 5, 9, tzinfo=self.NZ_time),
                                     datetime(2015, 5, 10, tzinfo=self.NZ_time),
                                     datetime(2016, 5, 8, tzinfo=self.NZ_time))
        
        self.sample_negative_days = (datetime(1990, 4, 13, tzinfo=self.NZ_time),
                                     datetime(1990, 6, 13, tzinfo=self.NZ_time),
                                     datetime(1990, 5, 12, tzinfo=self.NZ_time),
                                     datetime(1990, 5, 14, tzinfo=self.NZ_time),
                                     datetime(1990, 5, 6, tzinfo=self.NZ_time),
                                     datetime(2015, 5, 2, tzinfo=self.NZ_time))

        self.offset_days = ({"day":datetime(2015, 5, 2, tzinfo=self.NZ_time), "offset":8},
                            {"day":datetime(2015, 5, 15, tzinfo=self.NZ_time), "offset":359},
                            {"day":datetime(2015, 5, 10, tzinfo=self.NZ_time), "offset":0})

            
class TestChristmas(TestSpecificDayBase):
    
    def setUp(self):
        super(TestChristmas, self).setUp()
        self.day = CHRISTMAS
        self.sample_positive_days = (datetime(1990, 12, 25, tzinfo=self.NZ_time),
                                     datetime(1999, 12, 25, tzinfo=self.NZ_time),
                                     datetime(2000, 12, 25, tzinfo=self.NZ_time),
                                     datetime(2014, 12, 25, tzinfo=self.NZ_time),
                                     datetime(2015, 12, 25, tzinfo=self.NZ_time),
                                     datetime(3000, 12, 25, tzinfo=self.NZ_time))
        
        self.sample_negative_days = (datetime(1990, 12, 26, tzinfo=self.NZ_time),
                                     datetime(1990, 12, 24, tzinfo=self.NZ_time),
                                     datetime(1990, 11, 25, tzinfo=self.NZ_time))

        self.offset_days = ({"day":datetime(2000, 12, 15, tzinfo=self.NZ_time), "offset":10},
                            {"day":datetime(2014, 12, 28, tzinfo=self.NZ_time), "offset":362},
                            {"day":datetime(1995, 12, 25, tzinfo=self.NZ_time), "offset":0})

        
class TestToday(TestSpecificDayBase):
    
    def setUp(self):
        super(TestToday, self).setUp()
        self.day = TODAY
        self.sample_positive_days = (datetime.now(tz=self.NZ_time),)
        
class TestWaitangiDay(TestSpecificDayBase):
    
    def setUp(self):
        super(TestWaitangiDay, self).setUp()
        self.day = WAITANGI_DAY
        self.sample_positive_days = (datetime(1999, 2, 6, tzinfo=self.NZ_time),
                                     datetime(2000, 2, 6, tzinfo=self.NZ_time),
                                     datetime(2015, 2, 6, tzinfo=self.NZ_time),
                                     datetime(2016, 2, 6, tzinfo=self.NZ_time))
        
        self.sample_negative_days = (datetime(2016, 2, 7, tzinfo=self.NZ_time),
                                     datetime(2016, 2, 5, tzinfo=self.NZ_time),
                                     datetime(2016, 1, 6, tzinfo=self.NZ_time))

        self.offset_days = ({"day":datetime(1999, 2, 1, tzinfo=self.NZ_time), "offset":5},
                            {"day":datetime(2000, 3, 10, tzinfo=self.NZ_time), "offset":333},
                            {"day":datetime(2015, 2, 6, tzinfo=self.NZ_time), "offset":0})


class TestFathersDay(TestSpecificDayBase):
    
    def setUp(self):
        super(TestFathersDay, self).setUp()
        self.day = FATHERS_DAY
        self.sample_positive_days = (datetime(1990, 9, 2, tzinfo=self.NZ_time),
                                     datetime(1991, 9, 1, tzinfo=self.NZ_time),
                                     datetime(2000, 9, 3, tzinfo=self.NZ_time),
                                     datetime(2008, 9, 7, tzinfo=self.NZ_time),
                                     datetime(2010, 9, 5, tzinfo=self.NZ_time),
                                     datetime(2015, 9, 6, tzinfo=self.NZ_time),
                                     datetime(2016, 9, 4, tzinfo=self.NZ_time))
        
        self.sample_negative_days = (datetime(1990, 10, 2, tzinfo=self.NZ_time),
                                     datetime(1990, 8, 2, tzinfo=self.NZ_time),
                                     datetime(1990, 9, 1, tzinfo=self.NZ_time),
                                     datetime(1990, 9, 3, tzinfo=self.NZ_time),
                                     datetime(1990, 9, 6, tzinfo=self.NZ_time),
                                     datetime(2015, 9, 2, tzinfo=self.NZ_time))

        self.offset_days = ({"day":datetime(1999, 2, 1, tzinfo=self.NZ_time), "offset":216},
                            {"day":datetime(2000, 3, 10, tzinfo=self.NZ_time), "offset":177},
                            {"day":datetime(2015, 9, 6, tzinfo=self.NZ_time), "offset":0})


class TestLabourDay(TestSpecificDayBase):
    
    def setUp(self):
        super(TestLabourDay, self).setUp()
        self.day = LABOUR_DAY
        self.sample_positive_days = (datetime(1990, 10, 22, tzinfo=self.NZ_time),
                                     datetime(1991, 10, 28, tzinfo=self.NZ_time),
                                     datetime(1999, 10, 25, tzinfo=self.NZ_time),
                                     datetime(2000, 10, 23, tzinfo=self.NZ_time),
                                     datetime(2015, 10, 26, tzinfo=self.NZ_time),
                                     datetime(2016, 10, 24, tzinfo=self.NZ_time),)
        
        self.sample_negative_days = (datetime(1990, 10, 21, tzinfo=self.NZ_time),
                                     datetime(1990, 10, 23, tzinfo=self.NZ_time),
                                     datetime(1990, 9, 22, tzinfo=self.NZ_time),
                                     datetime(1990, 9, 3, tzinfo=self.NZ_time),
                                     datetime(1990, 9, 6, tzinfo=self.NZ_time),
                                     datetime(2015, 9, 2, tzinfo=self.NZ_time))

        self.offset_days = ({"day":datetime(1999, 2, 1, tzinfo=self.NZ_time), "offset":266},
                            {"day":datetime(2000, 11, 10, tzinfo=self.NZ_time), "offset":346},
                            {"day":datetime(2015, 10, 26, tzinfo=self.NZ_time), "offset":0})


class TestQueensBirthday(TestSpecificDayBase):
    
    def setUp(self):
        super(TestQueensBirthday, self).setUp()
        self.day = QUEENS_BIRTHDAY
        self.sample_positive_days = (datetime(1990, 6, 4, tzinfo=self.NZ_time),
                                     datetime(1991, 6, 3, tzinfo=self.NZ_time),
                                     datetime(1999, 6, 7, tzinfo=self.NZ_time),
                                     datetime(2015, 6, 1, tzinfo=self.NZ_time),
                                     datetime(2016, 6, 6, tzinfo=self.NZ_time))
        
        self.sample_negative_days = (datetime(1990, 6, 3, tzinfo=self.NZ_time),
                                     datetime(1990, 6, 5, tzinfo=self.NZ_time),
                                     datetime(1990, 5, 4, tzinfo=self.NZ_time),)

        self.offset_days = ({"day":datetime(1991, 2, 1, tzinfo=self.NZ_time), "offset":122},
                            {"day":datetime(1999, 11, 10, tzinfo=self.NZ_time), "offset":208},
                            {"day":datetime(2015, 6, 1, tzinfo=self.NZ_time), "offset":0})


class TestNewYearsDay(TestSpecificDayBase):
    
    def setUp(self):
        super(TestNewYearsDay, self).setUp()
        self.day = NEW_YEARS_DAY
        self.sample_positive_days = (datetime(1999, 1, 1, tzinfo=self.NZ_time),
                                     datetime(2000, 1, 1, tzinfo=self.NZ_time),
                                     datetime(2015, 1, 1, tzinfo=self.NZ_time),
                                     datetime(2016, 1, 1, tzinfo=self.NZ_time))
        
        self.sample_negative_days = (datetime(2016, 1, 2, tzinfo=self.NZ_time),
                                     datetime(2016, 2, 1, tzinfo=self.NZ_time),
                                     datetime(2015, 12, 31, tzinfo=self.NZ_time))
        
        self.offset_days = ({"day":datetime(1999, 12, 25, tzinfo=self.NZ_time), "offset":7},
                            {"day":datetime(2000, 2, 10, tzinfo=self.NZ_time), "offset":326},
                            {"day":datetime(2015, 1, 1, tzinfo=self.NZ_time), "offset":0})


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()