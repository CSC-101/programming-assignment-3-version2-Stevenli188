import county_demographics
import data
import build_data
from data import CountyDemographics

#part1, this function finds the total 2014 population from the selected counties
def population_total(counties:list[CountyDemographics])->int:
    total=0
    for county in counties:
        total += county.population["2014 Population"]
    return total

#part2, this function returns a list of county demographics objects if the provided state
# matches the state in the data.
def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    state_abbrv = state.upper()
    return [county for county in counties if county.state == state_abbrv]

#part3
#population by education,this function find the population in the selected counties that has the given education
# object and returns that population
def population_by_education(counties: list[CountyDemographics], education: str) -> float:
    total = 0.0
    for county in counties:
        peredu = county.education.get(education)
        if peredu == None:
            return None
        else:
            totalpop = county.population.get("2014 Population")
            total += totalpop * (peredu / 100)
    return total

#population by Ethnicity, this function finds the population in the selected counties that
#has the given ethnicity and returns that population
def population_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
    total = 0.0
    for county in counties:
        pereth = county.ethnicities.get(ethnicity)
        if pereth == None:
            return None
        else:
            totalpop = county.population.get("2014 Population")
            total += totalpop *(pereth / 100)
    return total

#population below poverty, this function find the population in the selected counties that
# is below poverty level and returns that population
def population_below_poverty_level(counties:list[CountyDemographics]) -> float:
    total = 0.0
    for county in counties:
        below = county.income.get("Persons Below Poverty Level")
        if below == None:
            return None
        else:
            totalpop = county.population.get("2014 Population")
            total += totalpop * (below / 100)
    return total

#part 4
#percent by education, this function find the population in the selected counties that
# has the selected education and returns the population that has the education in percentage.
def percent_by_education(counties: list[CountyDemographics], education: str) -> float:
    total = 0.0
    total_population = 0
    for county in counties:
        total_population += county.population.get("2014 Population")
        peredu = county.education.get(education)
        if peredu == None:
            return None
        else:
            totalpop = county.population.get("2014 Population")
            total += totalpop * (peredu / 100)
    return (float(total)/total_population)*100

#percent by ethnicity, this function find the population in the selected counties that
# has the selected ethnicity and returns the population that has the ethnicity in percentage.
def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
    total = 0.0
    total_population = 0
    for county in counties:
        total_population += county.population.get("2014 Population")
        pereth = county.ethnicities.get(ethnicity)
        if pereth == None:
            return None
        else:
            totalpop = county.population.get("2014 Population")
            total += totalpop *(pereth / 100)
    return (float(total)/total_population)*100

#percent_below_poverty_level, this function find the population in the selected counties that
# is below poverty level and returns that population in percentage.
def percent_below_poverty_level(counties:list[CountyDemographics]) -> float:
    total = 0.0
    total_population = 0
    for county in counties:
        total_population += county.population.get("2014 Population")
        below = county.income.get("Persons Below Poverty Level")
        if below == None:
            return None
        else:
            totalpop = county.population.get("2014 Population")
            total += totalpop * (below / 100)
    return (float(total)/total_population)*100

#part 5
#education_greater_than, this function finds the counties that have a percentage of
#population at the selected education level above the threshold and return the counties
def education_greater_than(counties:list[CountyDemographics], education: str, threshold:int) -> list[CountyDemographics]:

    counties_met=[]
    for county in counties:
        peredu = county.education.get(education)
        if peredu >=threshold:
            counties_met.append(county.county)
    return counties_met
#education_less_than, this function finds the counties that have a percentage of
#population at the selected education level below the threshold and return the counties
def education_less_than(counties:list[CountyDemographics], education: str, threshold:int) -> list[CountyDemographics]:
    counties_met=[]
    for county in counties:
        peredu = county.education.get(education)
        if peredu <= threshold:
            counties_met.append(county.county)
    return counties_met

#ethnicity greater than, this function finds the counties that have a percentage of
#population at the ethnicity above the threshold and return the counties
def ethnicity_greater_than(counties: list[CountyDemographics], ethnicity: str, threshold:int) -> list[CountyDemographics]:
    counties_met=[]
    for county in counties:
        pereth = county.ethnicities.get(ethnicity)
        if pereth >= threshold:
            counties_met.append(county.county)
    return counties_met

#ethniticy less than, this function finds the counties that have a percentage of
#population at the ethnicity below the threshold and return the counties
def ethnicity_less_than(counties: list[CountyDemographics], ethnicity: str, threshold:int) -> list[CountyDemographics]:
    counties_met=[]
    for county in counties:
        pereth = county.ethnicities.get(ethnicity)
        if pereth <= threshold:
            counties_met.append(county.county)
    return counties_met

#below poverty level greater than, this function finds the counties that have a percentage of
#population below poverty level above the threshold and return the counties
def below_poverty_level_greater_than(counties:list[CountyDemographics],threshold:int) -> list[CountyDemographics]:
    counties_met=[]
    for county in counties:
        below = county.income.get("Persons Below Poverty Level")
        if below >= threshold:
            counties_met.append(county.county)
    return counties_met

#below poverty level less than, this function finds the counties that have a percentage of
#population below poverty level below the threshold and return the counties
def below_poverty_level_less_than(counties:list[CountyDemographics], threshold:int) -> list[CountyDemographics]:
    counties_met = []
    for county in counties:
        below = county.income.get("Persons Below Poverty Level")
        if below <= threshold:
            counties_met.append(county.county)
    return counties_met