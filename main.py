import pandas as pd
import time
from Patient import Patient
from SimulationClock import SimulationClock
from multiprocessing import Process
import keyboard

import dearpygui.dearpygui as dpg
from math import sin



simulationRunning = True

patientType = int(input('Enter Patient Type \n1)child \n2)adolescent \n3)Adult\n'))

patient = Patient(patientType)
simStartime = patient.getSimStartTime()

simClock = SimulationClock(simStartime)

print(simStartime)

print(f"[WAWA] Glucose at sim start time (should be 145 ish) {patient.getGlucoseLevelAtTimestamp(simStartime)}") #Bug: First timestamp is +2hrs from start!

df = patient._paientSimulationDataFrame.head(380).copy()
df['Time'] = pd.to_datetime(df['Time'])
start_time = df['Time'].iloc[0]
df['TimeSeconds'] = (df['Time'] - start_time).dt.total_seconds()

dpg.create_context()

with dpg.window(label="Sim-Glucose Simulator "):
     with dpg.plot(label="Glucose vs Time", height=400, width=600):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="Time (s)", tag="x_axis")
        dpg.add_plot_axis(dpg.mvYAxis, label="Glucose (mg/dL)", tag="y_axis")

        dpg.add_line_series(
            df['TimeSeconds'].tolist(),
            df['BG'].tolist(),
            label="Patient Glucose",
            parent="y_axis",
            tag='bg_tag'
        )


dpg.create_viewport(title='Glucose Simulation', width=900, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

while simulationRunning and dpg.is_dearpygui_running:
    simClock.updateClock()
    dpg.render_dearpygui_frame()
    if keyboard.is_pressed('q'):
        simulationRunning = False

    bg = patient.getGlucoseLevelAtTimestamp(simClock.getSimulationTime())
    dpg.set_value('bg_tag', [simClock.getSimulationTime(), bg]) #updates not working Check docs for proper updatess!!

dpg.destroy_context()
    


#problem then scope then related work then summarize the then brief overview then ident Gaps