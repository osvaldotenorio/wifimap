import math
from scipy.optimize import least_squares

wifi_points = [
{
'SSID':'MYWIFI',
'time':1685220612.3635876,
'POWER':71,
'coord':[-20.442192, -54.648853]
},
{
'SSID':'MYWIFI',
'time':1685220616.8830545,
'POWER':88,
'coord':[-20.442124, -54.648991]
},
{
'SSID':'MYWIFI',
'time':1685220621.1812577,
'POWER':68,
'coord':[-20.442111, -54.649286]
},
{
'SSID':'MYWIFI',
'time':1685220634.1812577,
'POWER':30,
'coord':[-20.442367, -54.649423]
},
{
'SSID':'MYWIFI',
'time':1685220645.1812577,
'POWER':90,
'coord':[-20.442282803439593, -54.64905017325472]
},
{
'SSID':'MYWIFI',
'time':1685220666.1812577,
'POWER':85,
'coord':[-20.442268980313706, -54.6489375204833]
},
{
'SSID':'MYWIFI',
'time':1685220680.1812577,
'POWER':95,
'coord':[-20.44218981147781, -54.64906224319452]
}]



def convert_power_to_dbm(power_percentage):
    return (power_percentage / 2) - 100

def calculate_distance(frequency, PL):
    return 10 ** ((27.55 - (20 * math.log10(frequency)) + abs(PL)) / 20)

def residuals(point, coords, distances):
    return [math.sqrt((point[0]-c[0])**2 + (point[1]-c[1])**2) - d for c,d in zip(coords, distances)]

# Convert power to dbm and calculate distances
for point in wifi_points:
    point['POWER_DBM'] = convert_power_to_dbm(point['POWER'])
    point['DISTANCE'] = calculate_distance(2.4e9, point['POWER_DBM'])

# Initial guess for the wifi location is the average of the coordinates
initial_guess = [sum(point['coord'][i] for point in wifi_points) / len(wifi_points) for i in range(2)]

# Perform least squares optimization
result = least_squares(residuals, initial_guess, args=([point['coord'] for point in wifi_points], [point['DISTANCE'] for point in wifi_points]))

print(f"A localização estimada do ponto de acesso Wi-Fi é {result.x}")
