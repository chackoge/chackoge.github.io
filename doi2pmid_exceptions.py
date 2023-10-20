# Wrapper written by Vikram Ramavarapu with a couple of clean up lines I added at the end. 
# The script handles exceptions better than vanilla doi2pmid
from metapub.convert import doi2pmid
from pandas import DataFrame

def doi2pmid_wrapper(doi):
	try:
		return doi2pmid(doi)
	except:
		return 'NA'

dois = ['10.7150/thno.21945','10.3390/cells8070727', '10.7150/tino.21945']
pmids = [doi2pmid_wrapper(doi) for doi in dois]

data = {'dois': dois, 'Column2': pmids}
df = DataFrame(data)

print(df)
# coerce returned values to integers and add an extra column
s = pd.to_numeric(df['Column2'], errors='coerce').convert_dtypes()
df = df.assign(pmids=s)
