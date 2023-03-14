from cohortextractor import (
    codelist_from_csv,
    codelist,
)

# Dependence forming medications all and grouped
dfm_codes = codelist_from_csv(
    "codelists/user-RachelS99-dependence-forming-medications-dmd.csv",
    system="snomed",
    column='dmd_id',
    category_column="bnf_code",
)

# Indications for prescribing dependence forming medications
ind_codes = codelist_from_csv(
    "codelists/user-RachelS99-indications-for-dependency-medications.csv",
    system="snomed",
)

# Referral to social prescribing codes
socialrx_codes = codelist_from_csv(
    "codelists/user-RachelS99-social-prescribing-in-dependency.csv",
    system="snomed",
)

# GP Consultations
gp_consultations = codelist_from_csv(
    "codelists/user-RachelS99-gp-consults.csv",
    system="snomed",
)

# Exclude patients with cancer and/or epilepsy
haemcan_codes = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-c19haemcan_cod.csv",
    system="snomed",
)

othercan_codes = codelist_from_csv(
    "codelists/opensafely-cancer-excluding-lung-and-haematological-snomed.csv",
    system="snomed",
    column='id',
)

lungcan_codes = codelist_from_csv(
    "codelists/opensafely-lung-cancer-snomed.csv",
    system="snomed",
    column='id',
)

epilepsy_codes = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-epil_cod.csv",
    system="snomed",
)