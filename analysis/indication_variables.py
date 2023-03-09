from cohortextractor import (
    StudyDefinition,
    codelist,
    codelist_from_csv,
    combine_codelists,
    patients,
)
from codelists import *

indication_variables = dict(
    indication=patients.categorised_as(
        {
            "other": "DEFAULT",
            "acute_pain": """
                indication_code = '274663001'
            """,
            "alcohol_withdrawal": """
                indication_code = '386449006'
            """,
            "body_dysmorphic_disorder": """
                indication_code = '83482000'
            """,
            "chronic_depression": """
                indication_code = '192080009' OR
                indication_code = '161891005' OR
                indication_code = '134407002' OR
                indication_code = '736464002' OR
                indication_code = '274665008' OR
                indication_code = '278860009' OR
                indication_code = '144951000000106' OR
                indication_code = '735644008' OR
                indication_code = '3061000119102' OR
                indication_code = '23584100782423001' OR
                indication_code = '431481001' OR
                indication_code = '1362941000000102' OR
                indication_code = '860381000000107' OR
                indication_code = '237067000' OR
                indication_code = '279032003' OR
                indication_code = '128200000' OR
                indication_code = '36630001' OR
                indication_code = '49218002' OR
                indication_code = '279039007' OR
                indication_code = '68962001' OR
                indication_code = '22253000' OR
                indication_code = '10601006' OR
                indication_code = '76948002' OR
                indication_code = '30077003'
            """,
            "generalised_anxiety": """
                indication_code = '21897009' OR
                indication_code = '836551000000102' OR
                indication_code = '445455005'
            """,
            "insomnia": """
                indication_code = '272025006' OR
                indication_code = '44186003' OR
                indication_code = '440313002' OR
                indication_code = '83157008' OR
                indication_code = '59050008' OR
                indication_code = '326781000000101' OR
                indication_code = '41975002' OR
                indication_code = '162204000' OR
                indication_code = '67233009' OR
                indication_code = '192454004' OR
                indication_code = '191997003' OR
                indication_code = '39898005' OR
                indication_code = '193462001' OR
                indication_code = '268652009'
            """,
            "mild_depression": """
                indication_code = '310495003' OR
                indication_code = '87512008' OR
                indication_code = '79298009' OR
                indication_code = '237349002' OR
                indication_code = '231504006' OR
                indication_code = '191610000'
            """,
            "moderate_depression": """
                indication_code = '310496002' OR
                indication_code = '832007' OR
                indication_code = '15639000'
            """,
            "nerve_pain": """
                indication_code = '103014001' OR
                indication_code = '11679003' OR
                indication_code = '16269008' OR
                indication_code = '103015000'
            """,
            "neuropathic_pain": """
                indication_code = '762602002' OR
                indication_code = '944141000000108' OR
                indication_code = '247398009' OR
                indication_code = '279981003' OR
                indication_code = '810601000000106'
            """,
            "panic_disorder": """
                indication_code = '191722009' OR
                indication_code = '61569007' OR
                indication_code = '225624000' OR
                indication_code = '371631005' OR
                indication_code = '450356003'
            """,
            "ocd": """
                indication_code = '191736004'
            """,
            "personality_disorder": """
                indication_code = '76105009' OR
                indication_code = '26665006' OR
                indication_code = '231528008' OR
                indication_code = '37746008' OR
                indication_code = '20010003' OR
                indication_code = '442057004' OR
                indication_code = '473456000' OR
                indication_code = '84466009' OR
                indication_code = '1084061000000106' OR
                indication_code = '943161000000107' OR
                indication_code = '44376007' OR
                indication_code = '191496002' OR
                indication_code = '191772006' OR
                indication_code = '191765005' OR
                indication_code = '231527003' OR
                indication_code = '55341008' OR
                indication_code = '191753006' OR
                indication_code = '191773001' OR
                indication_code = '268633003' OR
                indication_code = '231525006' OR
                indication_code = '191774007' OR
                indication_code = '31611000' OR
                indication_code = '80711002' OR
                indication_code = '473457009' OR
                indication_code = '1376001' OR
                indication_code = '36217008' OR
                indication_code = '3601005' OR
                indication_code = '44966003' OR
                indication_code = '33449004' OR
                indication_code = '231530005' OR
                indication_code = '268634009' OR
                indication_code = '52954000' OR
                indication_code = '31027006' OR
                indication_code = '273844008'
            """,
            "psychotic_depression": """
                indication_code = '191676002'
            """,
            "restlessness_and_agitation": """
                indication_code = '274647009'
            """,
            "sciatica": """
                indication_code = '247366003' OR
                indication_code = '307176005' OR
                indication_code = '273206005' OR
                indication_code = '307177001' OR
                indication_code = '202794004' OR
                indication_code = '311804006' OR
                indication_code = '23056005'
            """,
        },
        indication_code=patients.with_these_clinical_events(
            ind_codes,
            between=["index_date", "last_day_of_month(index_date)"],
            returning="code",
        ),
        return_expectations={
            "category": {
                "ratios": {
                    "other": 0.06,
                    "acute_pain": 0.06,
                    "alcohol_withdrawal": 0.06,
                    "body_dysmorphic_disorder": 0.06,
                    "chronic_depression": 0.06,
                    "generalised_anxiety": 0.06,
                    "insomnia": 0.06,
                    "mild_depression": 0.06,
                    "moderate_depression": 0.06,
                    "nerve_pain": 0.06,
                    "neuropathic_pain": 0.06,
                    "panic_disorder": 0.06,
                    "ocd": 0.06,
                    "personality_disorder": 0.06,
                    "psychotic_depression": 0.06,
                    "restlessness_and_agitation": 0.05,
                    "sciatica": 0.05,
                }
            },
        },  
    ),
)
# print(indications)
