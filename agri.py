import serial
import requests
import re  # Import the re module for regular expressions

# Replace with your specific values
thingspeak_api_key = "HAJVOVMWWVME7JSB"
thingspeak_channel_id = "2488303"
arduino_port = "COM5"  # Replace with the actual port
baudrate = 9600

# Initialize serial communication with Arduino
ser = serial.Serial(arduino_port, baudrate)

def send_data_to_thingspeak(temperature, humidity, soil_moisture, light_intensity):
  """
  Sends sensor data to a ThingSpeak channel.
  """
  url = f"https://api.thingspeak.com/update?api_key={thingspeak_api_key}"
  url += f"&field1={temperature}&field2={humidity}&field3={soil_moisture}&field4={light_intensity}"
  try:
    response = requests.get(url)
    if response.status_code == 200:
      print("Data sent to ThingSpeak successfully!")
    else:
      print(f"Failed to send data. Status code: {response.status_code}")
  except Exception as e:
    print(f"Error sending data: {e}")

while True:
  # Read data from Arduino
  data = ser.readline().decode('utf-8').strip()

  # Extract sensor values using regular expressions
  match = re.search(r"Temperature: (\d+\.\d+) °C, Humidity: (\d+\.\d+)%, Soil Moisture: (\d+), Light Intensity: (\d+)", data)

  if match:
    temperature, humidity, soil_moisture, light_intensity = match.groups()
    # Send data to ThingSpeak
    send_data_to_thingspeak(temperature, humidity, soil_moisture, light_intensity)
  else:
    print("Failed to parse sensor data. Check Arduino output format.")

  # Optional delay
  # time.sleep(5)
