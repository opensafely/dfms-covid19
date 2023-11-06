library(dplyr)
library(readr)
library(glue)
library(here)
library(tidyr)

target_dir = here("output")
target_pattern = "measure_.*.csv"

target_files = list.files(
  path = target_dir,
  pattern = target_pattern,
  full.names = TRUE,
  recursive = TRUE
) 

for (file in target_files) {
  file_out <- read_csv(file) %>%
    mutate(
      research_population = case_when(
                  research_population==0 ~ as.integer(0),
                  research_population>7  ~ as.integer(round(research_population/5,0)*5),
                  T~NA
        ),
      population = case_when(
        population==0 ~ as.integer(0),
        population>7  ~ as.integer(round(population/5,0)*5),
        T~NA
        ),
      value = research_population / population
    )
  file_out
write_csv(file_out,here("output",glue("redacted_{basename(file)}")))  
}

