
import pyodide
from pyodide.http import pyfetch

# create function

async def download(url, file='auto.save'):
    res = await pyfetch(url)
    if res.status == 200:
        with open(file, 'wb') as f:
            f.write(await res.bytes())

uri = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

download(url=filename)
filename="auto.csv"