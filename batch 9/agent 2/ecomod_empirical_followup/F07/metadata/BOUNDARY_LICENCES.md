# Boundary attribution and licences

The boundary data are full published country TopoJSON objects from **geoBoundaries gbOpen**, compressed losslessly for distribution. They are not the separately simplified geometry downloads. Full commit identifiers, upstream URLs, original byte counts and SHA256 digests are in `physical_source_registry.json`; detailed provider metadata are in `geography/`. Compression changes the container, not the decompressed source bytes.

Citation: Runfola, D., et al. (2020). *geoBoundaries: A global database of political administrative boundaries*. PLOS ONE 15, e0231866. https://doi.org/10.1371/journal.pone.0231866 . API documentation: https://www.geoboundaries.org/api.html . geoBoundaries' description of gbOpen as CC-BY-4.0-compliant does not replace the original source licences recorded in its country metadata.

| ISO | Source attribution recorded by provider | Original source licence |
|---|---|---|
| BRA | Instituto Brasileiro de Geografia e Estatística (IBGE) | CC BY 3.0 IGO |
| IDN | © OpenStreetMap contributors; Wambacher; geoBoundaries | Open Database License 1.0 |
| COD | © OpenStreetMap contributors; Wambacher; geoBoundaries | Open Database License 1.0 |
| CMR | geoBoundaries; Wikimedia | Creative Commons Attribution 3.0 |
| CAN | © OpenStreetMap contributors; Wambacher; geoBoundaries | Open Database License 1.0 |
| FIN | © OpenStreetMap contributors; Wambacher; geoBoundaries | Open Database License 1.0 |
| FRA | geoBoundaries; Wikipedia | CC0 1.0 |
| AUS | Australian Bureau of Statistics | Creative Commons Attribution 4.0 |

OpenStreetMap attribution and copyright: https://www.openstreetmap.org/copyright . ODbL 1.0: https://opendatacommons.org/licenses/odbl/1-0/ . CC BY 3.0 IGO: https://creativecommons.org/licenses/by/3.0/igo/ . CC BY 3.0: https://creativecommons.org/licenses/by/3.0/ . CC BY 4.0: https://creativecommons.org/licenses/by/4.0/ . CC0: https://creativecommons.org/publicdomain/zero/1.0/ . ABS source notice: https://www.abs.gov.au/website-privacy-copyright-and-disclaimer#copyright-and-creative-commons . No provider endorsement is implied.

The supplied source objects retain their respective original licences. The boundary-derived geographic support database (`country_domain_support.csv` and `geographic_planning_grid.csv`) is made available under ODbL 1.0 for database rights, with the above source-content attributions retained. The source objects, transformation code, methods and hashes needed to reconstruct this database are included. Country-level original contents retain their source terms rather than being unconditionally relicensed.

The separate account-identifier inventory and account-availability adaptations are distributed under **CC BY-SA 4.0**, as specified in `SOURCE_USE.md`. This is a collection of separately attributed sources and outputs, not a claim that every package file shares one licence. Territory notes and admission records identify the supporting sources and do not certify legal boundaries. The biomass data terms and guide reproduction restrictions remain separately applicable; raw native biomass responses are not redistributed.
