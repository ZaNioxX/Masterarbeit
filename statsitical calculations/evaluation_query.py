import numpy as np
from pymongo import MongoClient
import disproportionaly_analysis
from util import formatting
from util.timer import Timer

vaccine = "COVID19"
Manufacturer = "NOVAVAX"
symptom = "Pyrexia"

client = MongoClient('localhost', 27017)
db = client.vaers
col = client.reports

timer = Timer()
timer.start()

N_query_timer = Timer()
N_query_timer.start()
N = col.estimated_document_count()
N_query_timer.stop()
print("N query:", formatting.format_time(N_query_timer.time()))
print("N:", N)

D_query_timer = Timer()
D_query_timer.start()
D_query = {'vax_data.'}
D = col.count_documents(D_query)
D_query_timer.stop()
print("D query: ", formatting.format_time(D_query_timer.time()))

D_query_timer = Timer()
D_query_timer.start()
D_query = {'vax_data.'}
D = col.count_documents(D_query)
D_query_timer.stop()
print("D query: ", formatting.format_time(D_query_timer.time()))

E_query_timer = Timer()
E_query_timer.start()
E_query = {'vax_data.'}
E = col.count_documents(E_query)
E_query_timer.stop()
print("E query: ", formatting.format_time(D_query_timer.time()))

DE_query_timer = Timer()
DE_query_timer.start()
DE_query = {'$and': [D_query, E_query]}
DE = col.count_documents(DE_query)
DE_query_timer.stop()
print("DE query: ", formatting.format_time(D_query_timer.time()))

timer.stop()
print("Total: ", formatting.format_time(timer.time()))

De = D - DE
dE = E - DE
de = N - (DE + De + dE)
contingency_table = [[DE, dE], [De, de]]
print(contingency_table)

