# ER036 Point Inventory and Disposition

## Accepted finding

The theorem-completion dossier was not fully raw-data-self-contained: it omitted portable Fourier coefficient vectors. Referencing NPZ paths was insufficient for an external solver without workspace access.

## Implemented correction

K80, K120, and K240 Newton coefficient vectors are now exported as CSV with:

- signed modes;
- state labels;
- real/imaginary coefficients;
- one-ULP outward storage hulls;
- periods;
- SHA-256 manifest.

The self-contained dossier now lists the files, hashes, convention, and limitation.

## Remaining qualification

The one-ULP hull covers floating storage rounding only. It is not the orbit interval ball, analytic tail, or radii-polynomial enclosure. CAP-ORB/FLOQ/SLACK/BUNCH and coupling/theorem gates remain open.

## Disposition

Valid data-delivery defect corrected. No theorem promotion.