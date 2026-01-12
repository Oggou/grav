from astroquery.sdss import SDSS
query = "SELECT objID, ra, dec, z FROM SpecObj WHERE z BETWEEN 0.01 AND 0.05"
data = SDSS.query_sql(query)