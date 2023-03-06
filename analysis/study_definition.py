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

    ** demographic_variables,

    population=patients.satisfying(
        """
        registered = 1
        AND NOT has_died
        AND age <= 120
        """,
        registered=patients.registered_as_of(
            "index_date",
        ),
        has_died=patients.died_from_any_cause(
            on_or_before="index_date",
            returning="binary_flag",
        ),
    ),

    research_population=patients.satisfying(
        """
        research_registered = 1
        AND NOT research_has_died
        AND age <= 120
        AND on_dfm
        AND NOT hematological_cancer
        AND NOT lung_cancer
        AND NOT other_cancer
        """,
        research_registered=patients.registered_as_of(
            "index_date",
        ),
        research_has_died=patients.died_from_any_cause(
            on_or_before="index_date",
            returning="binary_flag",
        ),
        on_dfm=patients.with_these_medications(
            dfm_codes,
            between=["index_date", "last_day_of_month(index_date)"],
            return_expectations={
                "incidence": 1,
                },
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
    with_medication=patients.with_these_clinical_events(
        dfm_codes,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
            "incidence": 0.95,
        },
    ),
    with_indication=patients.with_these_clinical_events(
        ind_codes,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
            "incidence": 0.8,
        },
    ),
    with_consultation=patients.with_these_clinical_events(
        gp_consultations,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
            "incidence": 0.75,
        },
    ),
    count_consultation=patients.with_these_clinical_events(
        gp_consultations,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="number_of_matches_in_period",
        return_expectations={
            "int": {"distribution": "poisson", "mean": 3},
            "incidence": 0.75,
        },
    ),
    with_social_prescribing=patients.with_these_clinical_events(
        socialrx_codes,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
        },
    ),
    count_social_prescribing=patients.with_these_clinical_events(
        socialrx_codes,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="number_of_matches_in_period",
        return_expectations={
            "int": {"distribution": "poisson", "mean": 3},
            "incidence": 0.25,
        },
    ),
    ** indication_variables,
    ** medication_variables
)

measures = [
        Measure(
        id=f"dfm_medications_by_{d}_rate",
        numerator="research_population",
        denominator="population",
        group_by=[d],
    )
    for d in demographic_variables.keys()
] + [
        Measure(
        id=f"compare_medications_by_{d}_socialrx_v_consultation_rate",
        numerator="research_population",
        denominator="population",
        group_by=[d,"with_social_prescribing", "with_consultation", "with_medication"],
    )
    for d in demographic_variables.keys()  
] + [
    Measure(
        id="dfm_medications_grouped_rate",
        numerator="research_population",
        denominator="population",
        group_by=["medication"],
    ),
    Measure(
        id="dfm_indications_grouped_rate",
        numerator="research_population",
        denominator="population",
        group_by=["indication"],
    ),
    Measure(
        id="social_prescribing_rate",
        numerator="with_social_prescribing",
        denominator="population",
        group_by=["research_population"],
    ),
    Measure(
        id="gp_consultation_rate",
        numerator="with_consultation",
        denominator="population",
        group_by=["research_population"],
    ),
    Measure(
        id="indication_rate",
        numerator="with_indication",
        denominator="population",
        group_by=["research_population"],
    ),
    Measure(
        id="medication_rate",
        numerator="with_medication",
        denominator="population",
        group_by=["research_population"],
    ),
    Measure(
        id="gp_consultation_with_medication_rate",
        numerator="research_population",
        denominator="population",
        group_by=["medication", "with_consultation"],
    ),
    Measure(
        id="social_prescribing_with_medication_rate",
        numerator="research_population",
        denominator="population",
        group_by=["medication", "with_social_prescribing"],
    ),
    Measure(
        id="compare_socialrx_v_consultation_rate",
        numerator="research_population",
        denominator="population",
        group_by=["with_social_prescribing", "with_consultation", "with_medication"],
    ),
]