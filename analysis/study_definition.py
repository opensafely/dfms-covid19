from cohortextractor import (
    StudyDefinition,
    Measure,
    codelist,
    codelist_from_csv,
    combine_codelists,
    filter_codes_by_category,
    patients,
)
from demographic_variables import demographic_variables
from indication_variables import indication_variables
from medication_variables import medication_variables
from codelists import *
from datetime import date


study = StudyDefinition(
    index_date = "2023-02-01",
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "index_date"},
        "rate": "uniform",
        "incidence": 0.2,
    },

    population=patients.all(),

    ** demographic_variables,

    research_population=patients.satisfying(
        """
        registered = 1
        AND NOT has_died
        AND age <= 120
        AND on_dfm
        AND NOT hematological_cancer
        AND NOT lung_cancer
        AND NOT other_cancer
        """,
        registered=patients.registered_as_of(
            "index_date",
        ),
        has_died=patients.died_from_any_cause(
            on_or_before="index_date",
            returning="binary_flag",
        ),
        on_dfm=patients.with_these_medications(
            dfm_codes,
            between=["index_date", "last_day_of_month(index_date)"],
        ),
        hematological_cancer=patients.with_these_clinical_events(
            haemcan_codes,
            between=["index_date", "last_day_of_month(index_date)"],
        ),
        lung_cancer=patients.with_these_clinical_events(
            lungcan_codes,
            between=["index_date", "last_day_of_month(index_date)"],
        ),
        other_cancer=patients.with_these_clinical_events(
            othercan_codes,
            between=["index_date", "last_day_of_month(index_date)"],
        ),
    ),
    with_indications=patients.with_these_clinical_events(
        ind_codes,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
        },
    ),
    with_consultation=patients.with_these_clinical_events(
        gp_consultations,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
            "incidence": 0.8,
        },
    ),
    has_social_prescribing=patients.with_these_clinical_events(
        socialrx_codes,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
            "incidence": 0.2,
        },
    ),
    ** indication_variables,
    ** medication_variables
)