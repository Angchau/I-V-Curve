import serial
from plot_utiles import plot_iv

# Serial communication configuration
ser = serial.Serial()
ser.port = '/dev/ttyUSB0'            # Secify serial port for com
ser.baudrate = 9600                  # Specify Baudrate
ser.bytesize = serial.EIGHTBITS      # Specify Bites number
ser.parity = serial.PARITY_NONE      # Specify Parity
ser.stopbits = serial.STOPBITS_ONE   # Specify Stop bites
ser.timeout = 1                      # Specify delay for answer

# Open Serial Com
ser.open()

# Keithley 2400 Configuration
ser.write(b'*RST\n')                  # reinitialisation of the instrument
ser.write(b':SOUR:FUNC:MODE VOLT\n')  # Sourcing tension
ser.write(b':SOUR:VOLT:RANG 20\n')     # Tension Range set to 2V
ser.write(b':SENS:FUNC "CURR"\n')     # Measuring current
ser.write(b':SENS:CURR:PROT 1\n')  # Current protection set at 1.05A : Maximum for keithely 2400
ser.write(b':SENS:CURR:RANG 0.01\n')     # Current range to 0.01 Amp

# Number of measurement points
voltages = [0, 1, 2, 3, 4, 5, 6, 9, 12, 15]   # voltages values
currents = []                                                   # measured currents

for voltage in voltages:
    ser.write(b':SOUR:VOLT %f\n' % voltage)           # Source Tension (V)
    ser.write(b':OUTP ON\n')                          # Instrument output open
    ser.write(b':INIT\n')                             # Start measuring
    ser.write(b':FETC?\n')                            # Retrieve the measured values
    current = ser.readline().decode('ascii').strip()  # Save answers in a string
    values = current.split(',')                       # Split the string into measured values (Voltage, Current, Etc)
    print("voltage [V]")
    print(values[0])                                  # Print sourced Voltage
    currents.append(values[1])
    print("Current [A]")
    print(values[1])                                  # Print measured currents
    ser.write(b':OUTP OFF\n')                         # Close output from Instrument

# Close Serial Communication
ser.close()

# Plot the measured currents in function of the sourced voltage (I-V curve)
plot_iv(voltages,currents)
#plt.plot(voltages, currents)
#plt.xlabel("Tension [V]")
#plt.ylabel("Courant [A]")
#plt.show()

#Possibility to add Isc and Voc on the plot when it's working.