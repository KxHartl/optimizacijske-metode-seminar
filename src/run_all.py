"""
Master Runner Script for OMRiUS Seminar Simulations
Executes Tasks 1 through 4, validates analytical-numerical tolerances,
and generates all publication figures in docs/figures/.
"""

import os
import sys
import subprocess

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run_step(script_name):
    print(f"\n==========================================")
    print(f"Running {script_name}...")
    print(f"==========================================")
    cmd = [sys.executable, os.path.join(os.path.dirname(__file__), script_name)]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    print(res.stdout)
    if res.returncode != 0:
        print(f"ERROR in {script_name}:\n{res.stderr}")
        sys.exit(res.returncode)

if __name__ == '__main__':
    run_step('task1_qp_analysis.py')
    run_step('task2_robust_qp.py')
    run_step('task3_road_leveling.py')
    run_step('task4_lmi_switched_stabilization.py')
    print("\nAll OMRiUS simulation suites completed successfully!")
