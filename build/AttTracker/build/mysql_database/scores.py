import MySQLdb as mdb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import collections

db = mdb.connect(host="127.0.0.1", user="root", passwd="root", db="test2")
cur = db.cursor()

cur.execute("SELECT * FROM scores")
data = cur.fetchall()
db.close()

for row in data:
    print row