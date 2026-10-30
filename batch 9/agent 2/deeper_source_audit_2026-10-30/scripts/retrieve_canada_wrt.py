#!/usr/bin/env python3
"""Refresh the public Canada N3WRT class-35 snapshots used by the audit.

Requires: requests. This network step is separate from the offline diagnostics.
The service is live and versioned outputs can change; preserve prior snapshots.
"""
from __future__ import annotations

import json
import pathlib
import urllib.parse

import requests

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "canada_wrt"
OUT.mkdir(parents=True, exist_ok=True)
TEMPLATE = "https://nfi.nfis.org/resources/data_and_tools/templates/n3wrt_classifiers_list_tmp.txt"
ATTRIBUTES = "class_comb_id,forest2,forest2_desc,for_type,for_type_desc,ageclass,ageclass_desc,biom_total_mil,sep_biom,biomass_cll,biomass_clu,var_biom"
ECOZONE_ATTRIBUTES = "class_comb_id,ecozone_desc,forest2,forest2_desc,for_type,for_type_desc,ageclass,ageclass_desc,biom_total_mil,sep_biom,biomass_cll,biomass_clu,var_biom"


def retrieve(scope: str, measure: str, dataset: str, geolinks: str, attributes: str) -> dict:
    parameters = {
        "Service": "GDAS",
        "Request": "GetData",
        "Version": "0.9.1",
        "FrameworkDomain": "nfis.org",
        "FrameworkName": "nfi_web",
        "FrameworkVersion": "1",
        "DatasetDomain": "nfis.org",
        "DatasetName": dataset,
        "Attribute": attributes,
        "GeolinkIds": geolinks,
    }
    gdas_url = "https://nfi.nfis.org/gdas/gdas?" + urllib.parse.urlencode(parameters)
    query = {
        "gdasUrl": gdas_url,
        "templateUrl": TEMPLATE,
        "format": "text",
        "version": "1.0",
        "lang": "en",
        "cache": "false",
        "filterClause": 'class_comb_id EQUALS "35"',
    }
    response = requests.get("https://nfi.nfis.org/wrt/service", params=query, timeout=240)
    response.raise_for_status()
    payload = response.json()
    target = OUT / f"wrt_{scope}_{measure}_class35_variance.json"
    target.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(scope, measure, response.status_code, len(payload.get("data", [])), target)
    return payload


def main() -> None:
    retrieve("national", "point", "v_pp_summary_national_en_point", "canada", ATTRIBUTES)
    retrieve("national", "changes", "v_pp_summary_national_en_changes", "canada", ATTRIBUTES)
    retrieve("ecozone", "changes", "v_pp_summary_ecozone_en_changes", ",".join(str(x) for x in range(4, 16)), ECOZONE_ATTRIBUTES)


if __name__ == "__main__":
    main()
