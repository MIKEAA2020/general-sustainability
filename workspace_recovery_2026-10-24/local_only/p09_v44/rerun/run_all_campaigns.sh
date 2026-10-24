#!/bin/bash
cd /home/user/p09_v44/rerun/wave_e_cod/src
for s in run_families_v3.py campaign_e2_structure_v3.py campaign_e2_cadence_v3.py campaign_e2_elevation_v3.py campaign_e2_identification_v3.py campaign_e2_depensation_v3.py campaign_e2_allee_declared_v3.py campaign_e2_fox_form_v3.py; do
  echo "=== $s $(date +%T)"; ( time timeout 3000 python3 -u $s ) > ../../logs/$s.log 2>&1; echo "exit $? $(date +%T)"
done
cd /home/user/p09_v44/rerun/wave_e_edwards/src
for s in run_intervention_v2.py e4_audit_layer.py; do
  echo "=== $s $(date +%T)"; ( time timeout 3000 python3 -u $s ) > ../../logs/$s.log 2>&1; echo "exit $? $(date +%T)"
done
cd /home/user/p09_v44/rerun && mkdir -p rerun_campaigns && cp ../src/rerun_campaigns/campaign_e4_elevation.py rerun_campaigns/ && cd rerun_campaigns && echo "=== campaign_e4_elevation.py $(date +%T)" && ( time timeout 3000 python3 -u campaign_e4_elevation.py ) > ../logs/campaign_e4_elevation.py.log 2>&1; echo "exit $? $(date +%T)"
echo ALLDONE
