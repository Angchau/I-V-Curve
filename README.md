# I-V-Curve
## I-V Curve Caracterisation of Solar cells

**10 March 2023 **

This repository allow user to plot I-V curve from solar cells with a Keithley 2400 Source meter
The communication protocole used in order to communicate between the computer and the Instrument is USB-Rs232 (Cable mandatory) - 

The script I-V_Curve_Rs232.py allows you to communicate with the sourcemeter Keithley 2400. 
To do that you'll have to specify the name of the Serial port on which the instrument is connected. 

The source meter will source and measure Voltage or Current from a solar panel or solar cell and the script will help you to plot its I-V curve.  

After that you need to set the Communication settings on the Keithley 2400 : Rs 232 and then choose your parameters (Baudrate, Bits, Parity).
Then you add the parameters in the python script to make them correspond. 

Before running the scripts select the range and limitation on Voltage and currents for your measurements.

When You run the script, it'll source the voltages you define and measure output currents form the solar panels and then plot them. 
This is your I-V curve. 
