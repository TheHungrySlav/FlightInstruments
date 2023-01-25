# FlightInstruments
A sim of Flight Instrumentation using Pygame

Libraries: math, Pygame

User Input:

Arrow Up - Flies up
Arrow Dowsn - Flies Down
W - Increase airspeed
S - Decrease airspeed

GUI:

Altimeter is on the left, Air speed indicator is on the right

Functions:

airspeed()
  Calculates the airspeed based on how long the user holds the "throttle"
  input: current_airspeed, throttle
  output: new_airspeed, acceleration
airspeed_indicator()
  updates GUI airspeed indicator based on airspeed()
  input: current_airspeed
altitude()
  calculated current altitude based on airspeed() and direction of flight
  input: current_altitude, direction, airspeed, acceleration
  output: new_altitude
altimeter()
  updates GUI altimeter based on altitude()
  input: current_altitude
