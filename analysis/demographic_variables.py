from cohortextractor import patients, codelist_from_csv

# Age
demographic_variables = dict(
    age_band=patients.categorised_as(
        {
            "missing": "DEFAULT",
            "0-19": """ age >= 0 AND age < 20""",
            "20-29": """ age >=  20 AND age < 30""",
            "30-39": """ age >=  30 AND age < 40""",
            "40-49": """ age >=  40 AND age < 50""",
            "50-59": """ age >=  50 AND age < 60""",
            "60-69": """ age >=  60 AND age < 70""",
            "70-79": """ age >=  70 AND age < 80""",
            "80+": """ age >=  80 AND age <= 120""",
        },
        age=patients.age_as_of("index_date"),
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "missing": 0.005,
                    "0-19": 0.125,
                    "20-29": 0.125,
                    "30-39": 0.125,
                    "40-49": 0.125,
                    "50-59": 0.125,
                    "60-69": 0.125,
                    "70-79": 0.125,
                    "80+": 0.12,
                }
            },
        },
    ),
    # Sex
    sex=patients.sex(
        return_expectations={
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
            "incidence": 1,
        }
    ),
    # Index of Multiple Deprivation (IMD)
    imd_q5=patients.categorised_as(
        {
            "Unknown": "DEFAULT",
            "1": "imd >= 0 AND imd < 32800*1/5",
            "2": "imd >= 32800*1/5 AND imd < 32800*2/5",
            "3": "imd >= 32800*2/5 AND imd < 32800*3/5",
            "4": "imd >= 32800*3/5 AND imd < 32800*4/5",
            "5": "imd >= 32800*4/5 AND imd <= 32800",
        },
        imd=patients.address_as_of(
            "index_date",
            returning="index_of_multiple_deprivation",
            round_to_nearest=100,
        ),
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "Unknown": 0.05,
                    "1": 0.20,
                    "2": 0.20,
                    "3": 0.20,
                    "4": 0.20,
                    "5": 0.15,
                }
            },
        },
    ),
    # Region
    region=patients.registered_practice_as_of(
        "last_day_of_month(index_date)",
        returning="nuts1_region_name",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "North East": 0.1,
                    "North West": 0.1,
                    "Yorkshire and The Humber": 0.1,
                    "East Midlands": 0.1,
                    "West Midlands": 0.1,
                    "East": 0.1,
                    "London": 0.2,
                    "South East": 0.1,
                    "South West": 0.1,
                },
            },
        },
    ),
)