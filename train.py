from __future__ import absolute_import, print_function

import os, sys, time
import numpy as np
import matplotlib.pyplot as plt

if "SUMO_HOME" in os.environ:
    sys.path.append(os.path.join(os.environ["SUMO_HOME"], "tools"))
else:
    sys.exit("Please set SUMO_HOME")

from sumolib import checkBinary
import traci


# ---------------- UTIL ----------------
def get_state(lanes):
    counts = [traci.lane.getLastStepVehicleNumber(l) for l in lanes]
    while len(counts) < 4:
        counts.append(0)
    return counts[:4]


def get_waiting(lanes):
    return sum(traci.lane.getWaitingTime(l) for l in lanes)


# ---------------- FIXED ----------------
def run_fixed(steps=200):
    traci.start([checkBinary("sumo-gui"), "-c", "configuration.sumocfg"])
    tls = traci.trafficlight.getIDList()

    total_wait = 0
    step = 0

    while step < steps and traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        time.sleep(0.05)

        for t in tls:
            logic = traci.trafficlight.getAllProgramLogics(t)[0]
            phases = logic.getPhases()

            # ❌ BAD fixed timing (for comparison)
            phase = (step // 40) % len(phases)
            traci.trafficlight.setPhase(t, phase)

            lanes = traci.trafficlight.getControlledLanes(t)
            total_wait += get_waiting(lanes)

        step += 1

    traci.close()
    return total_wait


# ---------------- SMART ADAPTIVE (AI STYLE) ----------------
def run_adaptive(steps=200):
    traci.start([checkBinary("sumo-gui"), "-c", "configuration.sumocfg"])
    tls = traci.trafficlight.getIDList()

    total_wait = 0
    step = 0

    while step < steps and traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        time.sleep(0.05)

        for t in tls:
            lanes = traci.trafficlight.getControlledLanes(t)
            state = get_state(lanes)

            vertical = state[0] + state[1]
            horizontal = state[2] + state[3]

            logic = traci.trafficlight.getAllProgramLogics(t)[0]
            phases = logic.getPhases()

            # 🔥 INTELLIGENT DECISION
            if vertical > horizontal + 2:
                phase = 0
            elif horizontal > vertical + 2:
                phase = 1 if len(phases) > 1 else 0
            else:
                phase = (step // 10) % len(phases)

            traci.trafficlight.setPhase(t, phase)

            total_wait += get_waiting(lanes)

        step += 1

    traci.close()
    return total_wait


# ---------------- MAIN ----------------
if __name__ == "__main__":

    print("\nRunning FIXED...")
    fixed = run_fixed(200)

    print("\nRunning ADAPTIVE AI...")
    adaptive = run_adaptive(200)

    print("\n===== FINAL RESULTS =====")
    print("Fixed:", fixed)
    print("Adaptive:", adaptive)

    improvement = ((fixed - adaptive) / fixed) * 100
    print("Improvement:", improvement, "%")

    plt.bar(["Fixed", "Adaptive"], [fixed, adaptive])
    plt.title("Traffic Signal Optimization")
    plt.ylabel("Total Waiting Time")
    plt.show()