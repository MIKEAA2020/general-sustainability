# External crop-proxy inputs (supplementary sensitivity only)

These two packaged files are used only for the explicitly labeled, exploratory crop-proxy decomposition in `work/nfa_2026_proxy_divisia.py`. They do not populate a physical ecological-capital inventory and do not establish a measured physical-stock decline.

| File | Variable used | Definition and source |
|---|---|---|
| `cropland_area_owid.csv` | World, `Cropland - Area (hectares)` | FAOSTAT land-use cropland area: arable land plus permanent crops; hectares. Our World in Data (OWID) Grapher series `cropland-area`, source FAO, last updated 2026-02-25; downloaded 2026-10-24. |
| `cereal_yield_owid.csv` | World, `Cereals - Yield (tonnes per hectare)` | FAOSTAT cereal (primary) yield; tonnes per hectare. OWID Grapher series `cereal-yield`, source FAO, last updated 2026-02-25; downloaded 2026-10-24. Cereals are a sentinel, not all-crop output or an NFA yield factor. |

Source pages:

- https://ourworldindata.org/grapher/cropland-area
- https://ourworldindata.org/grapher/cereal-yield
- Underlying FAOSTAT Land Use data: http://www.fao.org/faostat/en/#data/RL
- Underlying FAOSTAT crop-yield data: https://www.fao.org/faostat/en/#data/QCL

The OWID/FAOSTAT time series are physical area and yield inputs. Their growth indices are combined with a base-year level calibrated to 1961 NFA cropland biocapacity. That calibration gives the proxy account an NFA-unit scale but does not establish a one-to-one boundary or valuation match. The proxy `X = b_hat_f A_f` therefore remains an assumed observation operator. Its residual `C = B_NFA - X` is an accounting residual only; it is not automatically non-cropland biocapacity, the model's `Upsilon(q) A_c`, or physical ecological capital.

The separate all-crops World Bank crop-production-index series is not used in this package; it was excluded from the proxy after discontinuous base-period changes were identified in the source series.
