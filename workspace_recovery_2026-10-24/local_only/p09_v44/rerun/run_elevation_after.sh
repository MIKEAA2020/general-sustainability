#!/bin/bash
cd /home/user/p09_v44/rerun
while ! grep -q ALLDONE logs/driver.log; do sleep 20; done
cd wave_e_cod/src
echo "=== campaign_e2_elevation_v3.py (rerun) $(date -u +%H:%M:%S)" >> ../../logs/driver.log
( time timeout 7200 python3 -u campaign_e2_elevation_v3.py ) > ../../logs/campaign_e2_elevation_v3_rerun.log 2>&1
echo "exit $? $(date -u +%H:%M:%S)" >> ../../logs/driver.log
echo "ELEVDONE" >> ../../logs/driver.log
