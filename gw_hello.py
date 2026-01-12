from gwpy.timeseries import TimeSeries
from gwpy.io.ligoinfo import fetch_open_data

strain = fetch_open_data('H1', 'GW150914', '2015-09-14', '2015-09-14', cache=True)
strain.plot(title='GW150914 Strain Data')