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

dfm_antidepressants = codelist_from_csv(
    "codelists/user-RachelS99-dependence-forming-medications-antidepressants-dmd.csv",
    system="snomed",
    column='dmd_id',
    category_column="bnf_code",
)

dfm_benzodiazepines = codelist_from_csv(
    "codelists/user-RachelS99-dependence-forming-medications-benzodiazepines-dmd.csv",
    system="snomed",
    column='dmd_id',
    category_column="bnf_code",
)

dfm_chloral = codelist_from_csv(
    "codelists/user-RachelS99-dependence-forming-medications-chloral-and-derivatives-dmd.csv",
    system="snomed",
    column='dmd_id',
    category_column="bnf_code",
)

dfm_clomethiazole = codelist_from_csv(
    "codelists/user-RachelS99-dependence-forming-medications-clomethiazole-dmd.csv",
    system="snomed",
    column='dmd_id',
    category_column="bnf_code",
)

dfm_gabapentinoids = codelist_from_csv(
    "codelists/user-RachelS99-dependence-forming-medications-gabapentinoids-dmd.csv",
    system="snomed",
    column='dmd_id',
    category_column="bnf_code",
)

dfm_opioids = codelist_from_csv(
    "codelists/user-RachelS99-dependence-forming-medications-opioid-pain-medicine-dmd.csv",
    system="snomed",
    column='dmd_id',
    category_column="bnf_code",
)

dfm_zdrugs = codelist_from_csv(
    "codelists/user-RachelS99-dependence-forming-medications-z-drugs-dmd.csv",
    system="snomed",
    column='dmd_id',
    category_column="bnf_code",
)

# Indications for prescribing dependence forming medications
ind_codes = codelist_from_csv(
    "codelists/user-RachelS99-indications-for-dependency-forming-medications.csv",
    system="snomed",
)

ind_agitation = codelist_from_csv(
    "codelists/user-RachelS99-dfm-indications-agitation.csv",
    system="snomed",
)

ind_alcohol_withdrawal = codelist_from_csv(
    "codelists/user-RachelS99-dfm-indications-alcohol-withdrawal.csv",
    system="snomed",
)

ind_anxiety = codelist_from_csv(
    "codelists/user-RachelS99-dfm-indications-anxiety.csv",
    system="snomed",
)

ind_body_dysmorphia = codelist_from_csv(
    "codelists/user-RachelS99-dfm-indications-body-dysmorphic-disorder.csv",
    system="snomed",
)

ind_depression = codelist_from_csv(
    "codelists/user-RachelS99-dfm-indications-depression.csv",
    system="snomed",
)

ind_dissociative_disorder = codelist_from_csv(
    "codelists/user-RachelS99-dfm-indications-dissociative-disorder.csv",
    system="snomed",
)

ind_insomnia = codelist_from_csv(
    "codelists/user-RachelS99-dfm-indications-insomnia.csv",
    system="snomed",
)

ind_pain = codelist_from_csv(
    "codelists/user-RachelS99-dfm-indications-pain.csv",
    system="snomed",
)

ind_personality_disorder = codelist_from_csv(
    "codelists/user-RachelS99-dfm-indications-personality-disorder.csv",
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