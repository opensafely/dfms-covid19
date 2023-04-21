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
        registered
        AND NOT has_died
        AND age <= 120
        """,
    ),

    research_population=patients.satisfying(
        """
        registered
        AND NOT has_died
        AND age <= 120
        AND on_dfm
        AND NOT hematological_cancer
        AND NOT lung_cancer
        AND NOT other_cancer
        AND NOT has_epilepsy
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
            return_expectations={
                "incidence": 1,
                },
        ),
        hematological_cancer=patients.with_these_clinical_events(
            haemcan_codes,
            on_or_before="index_date",
        ),
        lung_cancer=patients.with_these_clinical_events(
            lungcan_codes,
            on_or_before="index_date",
        ),
        other_cancer=patients.with_these_clinical_events(
            othercan_codes,
            on_or_before="index_date",
        ),
        has_epilepsy=patients.with_these_clinical_events(
            epilepsy_codes,
            on_or_before="index_date",
        ),
    ),
    with_medication=patients.with_these_medications(
        dfm_codes,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
            "incidence": 0.95,
        },
    ),
    dfm_6_months = patients.with_these_medications(
        dfm_codes,
        between = ["index_date - 6 months", "index_date"],
        returning = "number_of_matches_in_period",
        return_expectations = {
            "int": {"distribution": "normal", "mean": 2, "stddev": 1},
            "incidence": 0.2,
        },
    ),
    repeat_dfm = patients.satisfying(
        """
        (dfm_6_months >= 3)
        """,
    ),
    non_repeat_dfm = patients.satisfying(
        """
        (dfm_6_months < 3 AND dfm_6_months > 0)
        """,
    ),
    antidepressants=patients.with_these_medications(
        antidepressants,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
            "incidence": 0.95,
        },
    ),
    benzodiazepines=patients.with_these_medications(
        benzodiazepines,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
            "incidence": 0.95,
        },
    ),
    chloral_and_derivatives=patients.with_these_medications(
        chloral_and_derivatives,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
            "incidence": 0.95,
        },
    ),
    clomethiazole=patients.with_these_medications(
        clomethiazole,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
            "incidence": 0.95,
        },
    ),
    gabapentinoids=patients.with_these_medications(
        gabapentinoids,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
            "incidence": 0.95,
        },
    ),
    opioid_pain_medicine=patients.with_these_medications(
        opioid_pain_medicine,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
            "incidence": 0.95,
        },
    ),
    z_drugs=patients.with_these_medications(
        z_drugs,
        find_last_match_in_period=True,
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={
            "incidence": 0.95,
        },
    ),
    with_indication=patients.with_these_clinical_events(
        ind_codes,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={
            "incidence": 0.8,
        },
    ),
    alcohol_dependence=patients.with_these_clinical_events(
        alcohol_dependence,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={
            "incidence": 0.05,
        },
    ),
    anxiety_disorder=patients.with_these_clinical_events(
        anxiety_disorder,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={
            "incidence": 0.05,
        },
    ),
    chronic_pain=patients.with_these_clinical_events(
        chronic_pain,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={
            "incidence": 0.05,
        },
    ),
    insomnia=patients.with_these_clinical_events(
        insomnia,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={
            "incidence": 0.05,
        },
    ),
    mental_disorder=patients.with_these_clinical_events(
        mental_disorder,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={
            "incidence": 0.05,
            },
    ),
    muscle_spasm=patients.with_these_clinical_events(
        muscle_spasm,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={
            "incidence": 0.05,
            },
    ),
    neurological_pain=patients.with_these_clinical_events(
        neurological_pain,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={
            "incidence": 0.05,
        },
    ),
    sciatica=patients.with_these_clinical_events(
        sciatica,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={
            "incidence": 0.05,
        },
    ),
    post_covid=patients.with_these_clinical_events(
        post_covid,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={
            "incidence": 0.05,
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
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={
        },
    ),
    count_social_prescribing=patients.with_these_clinical_events(
        socialrx_codes,
        find_last_match_in_period=True,
        on_or_before="index_date",
        returning="number_of_matches_in_period",
        return_expectations={
            "int": {"distribution": "poisson", "mean": 3},
            "incidence": 0.25,
        },
    ),
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
        numerator="research_population",
        denominator="population",
        group_by=["with_indication"],
    ),
    Measure(
        id="medication_rate",
        numerator="research_population",
        denominator="population",
        group_by=["with_medication"],
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
    Measure(
        id="repeat_prescribing_rate",
        numerator="repeat_dfm",
        denominator="population",
        group_by="research_population"
    ),
    Measure(
        id="non_repeat_prescribing_rate",
        numerator="non_repeat_dfm",
        denominator="population",
        group_by="research_population"
    ),
]