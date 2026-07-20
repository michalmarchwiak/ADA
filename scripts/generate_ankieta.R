#!/usr/bin/env Rscript
# Generate synthetic ankieta.csv (n = 200) matching the survey schema used in reports.

set.seed(2025)

n <- 200
n_pd <- 98

dzial <- c(rep("PD", n_pd), sample(c("HR", "IT", "MK"), n - n_pd, replace = TRUE))
dzial <- sample(dzial)  # shuffle

staz <- sample(1:3, n, replace = TRUE, prob = c(0.35, 0.4, 0.25))
plec <- sample(c("K", "M"), n, replace = TRUE, prob = c(0.48, 0.52))
czy_kier <- ifelse(staz == 3 & runif(n) < 0.32, "Tak", "Nie")
czy_kier[staz == 1] <- sample(c("Tak", "Nie"), sum(staz == 1), replace = TRUE, prob = c(0.06, 0.94))

pyt1 <- sample(c(-2, -1, 0, 1, 2), n, replace = TRUE, prob = c(0.05, 0.1, 0.15, 0.45, 0.25))
pyt1[dzial == "PD"] <- sample(c(-2, -1, 0, 1, 2), n_pd, replace = TRUE,
                               prob = c(0.02, 0.05, 0.08, 0.55, 0.30))

pyt2 <- sample(c(-2, -1, 1, 2), n, replace = TRUE, prob = c(0.12, 0.28, 0.4, 0.2))
pyt3 <- pyt2
na_idx <- sample(seq_len(n), 60)
pyt3[na_idx] <- NA
fill_idx <- sample(setdiff(seq_len(n), na_idx), 80)
pyt3[fill_idx] <- sample(c(-2, -1, 1, 2), 80, replace = TRUE, prob = c(0.08, 0.15, 0.45, 0.32))

wiek <- round(rnorm(n, mean = 38, sd = 9))
wiek <- pmax(22, pmin(62, wiek))

dane <- data.frame(
  DZIAL = dzial,
  STAZ = staz,
  CZY_KIER = czy_kier,
  PLEC = plec,
  PYT_1 = pyt1,
  PYT_2 = pyt2,
  PYT_3 = pyt3,
  WIEK = wiek,
  check.names = FALSE
)

write.table(dane, file = "ankieta.csv", sep = ";", row.names = FALSE,
            fileEncoding = "UTF-8", quote = FALSE)

cat("Wrote ankieta.csv with", nrow(dane), "rows (PD:", sum(dzial == "PD"), ")\n")
