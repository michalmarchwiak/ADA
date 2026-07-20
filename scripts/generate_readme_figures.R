#!/usr/bin/env Rscript
# Generate preview figures for README from survey data.

suppressPackageStartupMessages({
  library(tidyverse)
  library(scales)
  library(gridExtra)
})

root <- getwd()
if (!file.exists(file.path(root, "ankieta.csv"))) {
  gen <- file.path(root, "scripts", "generate_ankieta.R")
  if (file.exists(gen)) source(gen) else stop("ankieta.csv not found")
}

out_dir <- "docs/images"
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

dane <- read.csv("ankieta.csv", stringsAsFactors = FALSE, fileEncoding = "UTF-8",
                 check.names = FALSE, sep = ";")

dane <- dane %>%
  mutate(
    DZIAL = factor(DZIAL, levels = c("HR", "IT", "PD", "MK")),
    STAZ = factor(STAZ, levels = 1:3,
                  labels = c("Poniżej 1 roku", "1-3 lata", "Powyżej 3 lat")),
    PYT_1 = factor(PYT_1, levels = c(-2, -1, 0, 1, 2),
                   labels = c("Zdec. nie zgadzam", "Nie zgadzam", "Nie mam zdania",
                              "Zgadzam", "Zdec. zgadzam"))
  )

theme_set(theme_minimal(base_size = 12) +
            theme(plot.title = element_text(face = "bold", size = 13),
                  legend.position = "bottom"))

# Figure 1: PYT_1 distribution (bar)
p1 <- dane %>%
  count(PYT_1) %>%
  mutate(PYT_1 = forcats::fct_rev(PYT_1)) %>%
  ggplot(aes(PYT_1, n, fill = PYT_1)) +
  geom_col(show.legend = FALSE, width = 0.7) +
  scale_fill_brewer(palette = "RdYlBu") +
  labs(title = "Rozkład odpowiedzi PYT_1 (dostępność materiałów szkoleniowych)",
       x = NULL, y = "Liczba odpowiedzi") +
  coord_flip()

ggsave(file.path(out_dir, "pyt1_distribution.png"), p1, width = 8, height = 5, dpi = 150)

# Figure 2: Department composition
p2 <- dane %>%
  count(DZIAL) %>%
  ggplot(aes(DZIAL, n, fill = DZIAL)) +
  geom_col(show.legend = FALSE, width = 0.65) +
  scale_fill_manual(values = c(HR = "#4daf4a", IT = "#377eb8", PD = "#ff7f00", MK = "#984ea3")) +
  labs(title = "Struktura próby według działu (n = 200)",
       x = "Dział", y = "Liczba pracowników")

ggsave(file.path(out_dir, "department_counts.png"), p2, width = 6, height = 4.5, dpi = 150)

# Figure 3: PYT_1 by department (column profile)
p3 <- dane %>%
  count(DZIAL, PYT_1) %>%
  group_by(DZIAL) %>%
  mutate(pct = n / sum(n)) %>%
  ggplot(aes(DZIAL, pct, fill = PYT_1)) +
  geom_col(position = "stack", width = 0.7) +
  scale_y_continuous(labels = percent_format()) +
  scale_fill_brewer(palette = "RdYlBu", name = "PYT_1") +
  labs(title = "Profil odpowiedzi PYT_1 w podziale na działy",
       x = "Dział", y = "Odsetek")

ggsave(file.path(out_dir, "pyt1_by_department.png"), p3, width = 8, height = 5, dpi = 150)

# Figure 4: PYT_2 pie (report 1 style)
dane2 <- dane %>%
  mutate(PYT_2 = factor(PYT_2, levels = c(-2, -1, 1, 2),
                        labels = c("Zdec. nie zgadzam", "Nie zgadzam", "Zgadzam", "Zdec. zgadzam")))

p4 <- dane2 %>%
  count(PYT_2) %>%
  ggplot(aes("", n, fill = PYT_2)) +
  geom_col(width = 1) +
  coord_polar("y") +
  scale_fill_brewer(palette = "Spectral", name = "PYT_2") +
  theme_void() +
  labs(title = "PYT_2 — szkolenia a możliwości awansu")

ggsave(file.path(out_dir, "pyt2_pie.png"), p4, width = 6, height = 5, dpi = 150)

cat("Wrote figures to", out_dir, "\n")
