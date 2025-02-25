from unittest import result

import data
import build_data
import unittest
import hw3

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    # test population_total
    def test_population_total1 (self):
        counties = build_data.get_data()
        result = hw3.population_total(counties)
        self.assertEqual(result,318857056)

    def test_population_total2(self):
        county1 = reduced_data[0]
        county2 = reduced_data[1]
        county3 = reduced_data[2]
        counties = [county1,county2,county3]
        result = hw3.population_total(counties)
        self.assertEqual(result,396175)

    # Part 2
    # test filter_by_state
    def test_filter_by_state1(self):
        counties = reduced_data
        state = "ca"
        result = hw3.filter_by_state(counties,state)
        expected = [reduced_data[2],reduced_data[3]]
        self.assertEqual(result,expected)

    def test_filter_by_state2(self):
        counties = reduced_data
        state = "al"
        result = hw3.filter_by_state(counties,state)
        expected = [reduced_data[0]]
        self.assertEqual(result,expected)


    # Part 3
    # test population_by_education
    def test_population_by_education1(self):
        counties1 = reduced_data[0]
        counties2 = reduced_data[1]
        counties = [counties1,counties2]
        education = "Bachelor's Degree or Higher"
        result = hw3.population_by_education(counties,education)
        expected = 20400.226000000002
        self.assertEqual(result,expected)

    def test_population_by_education2(self):
        counties = reduced_data
        education = "Doctrate"
        result = hw3.population_by_education(counties,education)
        expected = None
        self.assertEqual(result,expected)


    # test population_by_ethnicity
    def test_population_by_ethnicity1(self):
        county1 = reduced_data[0]
        county2 = reduced_data[1]
        counties = [county1,county2]
        ethnicity = "White Alone"
        result = hw3.population_by_ethnicity(counties,ethnicity)
        expected = 99605.46
        self.assertEqual(result,expected)

    def test_population_by_ethnicity2(self):
        counties = reduced_data
        ethnicity = "martians"
        result = hw3.population_by_ethnicity(counties,ethnicity)
        expected = None
        self.assertEqual(result,expected)


    # test population_below_poverty_level
    def test_population_below_poverty_level1(self):
        county1 = reduced_data[2]
        county2 = reduced_data[3]
        counties = [county1,county2]
        result = hw3.population_below_poverty_level(counties)
        expected = 79558.55900000001
        self.assertEqual(result,expected)

    def test_population_below_poverty_level2(self):
        counties = reduced_data
        result = hw3.population_below_poverty_level(counties)
        expected = 107711.714
        self.assertEqual(result, expected)


    # Part 4
    # test percent_by_education
    def test_percent_by_education1(self):
        county1 = reduced_data[2]
        county2 = reduced_data[3]
        counties = [county1,county2]
        education = "Bachelor's Degree or Higher"
        result = hw3.percent_by_education(counties,education)
        expected = 34.22991515863835
        self.assertEqual(result,expected)

    def test_percent_by_education2(self):
        counties = reduced_data
        education = "Doctrate"
        result = hw3.percent_by_education(counties,education)
        expected = None
        self.assertEqual(result,expected)


    # test percent_by_ethnicity
    def test_percent_by_ethnicity1(self):
        county1 = reduced_data[0]
        county2 = reduced_data[1]
        counties = [county1,county2]
        ethnicity =  "Asian Alone"
        result = hw3.percent_by_ethnicity(counties,ethnicity)
        expected = 1.3634552317835549
        self.assertEqual(result,expected)

    def test_percent_by_ethnicity2(self):
        counties = reduced_data
        ethnicity = "Martians"
        result = hw3.percent_by_ethnicity(counties,ethnicity)
        expected = None
        self.assertEqual(result,expected)


    # test percent_below_poverty_level
    def test_percent_below_poverty_level1(self):
        county1 = reduced_data[2]
        county2 = reduced_data[3]
        counties = [county1,county2]
        result = hw3.percent_below_poverty_level(counties)
        expected = 16.347436368978762
        self.assertEqual(result,expected)

    def test_percent_below_poverty_level2(self):
        counties = reduced_data
        result = hw3.percent_below_poverty_level(counties)
        expected = 16.424150481920915
        self.assertEqual(result,expected)


    # Part 5
    # test education_greater_than
    def test_education_greater_than1(self):
        counties = reduced_data
        education = "Bachelor's Degree or Higher"
        threshold = 30
        result = hw3.education_greater_than(counties,education,threshold)
        expected = ["San Luis Obispo County", "Yolo County"]
        self.assertEqual(result,expected)

    def test_education_greater_than2(self):
        counties = reduced_data
        education = "High School or Higher"
        threshold = 90
        result = hw3.education_greater_than(counties,education,threshold)
        expected = ["Weston County"]
        self.assertEqual(result,expected)


    # test education_less_than
    def test_education_less_than1(self):
        counties = reduced_data
        education = "Bachelor's Degree or Higher"
        threshold = 10
        result = hw3.education_less_than(counties,education,threshold)
        expected = []
        self.assertEqual(result,expected)

    def test_education_less_than2(self):
        counties = reduced_data
        education = "High School or Higher"
        threshold = 85
        result = hw3.education_less_than(counties,education,threshold)
        expectd = ["Crawford County", "Yolo County", "Pettis County"]
        self.assertEqual(result,expectd)


    # test ethnicity_greater_than
    def test_ethnicity_greater_than1(self):
        counties = reduced_data
        ethnicity = "Two or More Races"
        threshold = 5
        result = hw3.ethnicity_greater_than(counties,ethnicity,threshold)
        expected = ["Yolo County"]
        self.assertEqual(result,expected)

    def test_ethnicity_greater_than2(self):
        counties = reduced_data
        ethnicity = "Native Hawaiian and Other Pacific Islander Alone"
        threshold = 0.3
        result = hw3.ethnicity_greater_than(counties,ethnicity,threshold)
        expected = ["Yolo County","Pettis County"]
        self.assertEqual(result,expected)


    # test ethnicity_less_than
    def test_ethnicity_less_than1(self):
        counties = reduced_data
        ethnicity = "Two or More Races"
        threshold = 2
        result = hw3.ethnicity_less_than(counties,ethnicity,threshold)
        expected = ["Autauga County","Pettis County"]
        self.assertEqual(result,expected)

    def test_ethnicity_less_than2(self):
        counties = reduced_data
        ethnicity = "American Indian and Alaska Native Alone"
        threshold = 0.5
        result = hw3.ethnicity_less_than(counties,ethnicity,threshold)
        expected = ["Autauga County"]
        self.assertEqual(result,expected)


    # test below_poverty_level_greater_than
    def test_below_poverty_level_greater_than1(self):
        counties = reduced_data
        threshold = 15
        result = hw3.below_poverty_level_greater_than(counties,threshold)
        expected = ["Crawford County","Yolo County","Butte County","Pettis County"]
        self.assertEqual(result,expected)

    def test_below_poverty_level_greater_than2(self):
        counties = reduced_data
        threshold = 30
        result = hw3.below_poverty_level_greater_than(counties,threshold)
        expected = []
        self.assertEqual(result,expected)


    # test below_poverty_level_less_than
    def test_below_poverty_level_less_than1(self):
        counties = reduced_data
        threshold = 10
        result = hw3.below_poverty_level_less_than(counties,threshold)
        expected = []
        self.assertEqual(result,expected)

    def test_below_poverty_level_less_than2(self):
        counties = reduced_data
        threshold = 20
        result = hw3.below_poverty_level_less_than(counties,threshold)
        expected = ["Autauga County","San Luis Obispo County","Yolo County","Butte County","Pettis County","Weston County"]
        self.assertEqual(result,expected)


if __name__ == '__main__':
    unittest.main()
