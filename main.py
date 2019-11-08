# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 CompuCom, All Rights Reserved
# Created by Enrique Plata

import pandas as pd
import sys
import sqlalchemy
from pathlib import Path
from ETL.db import dbconn

"""
    This module contains the main code
"""

REGISTRY = {
    'file_path': Path('C:/Users/lf188653/Desktop/JobRequisitionsbyCreatedDate.csv_decrypted.csv'),
    'truncate_table': 'TRUNCATE TABLE [dbo].[JOB_REQUISITIONS_BY_CREATED_DATE];',
    'table_name': 'JOB_REQUISITIONS_BY_CREATED_DATE',
    'db_schema': 'dbo'
}

if __name__ == '__main__':

    try:
        # Setup icommit variable
        icommit = 150
        
        # Creating the dbconnection object and its engine
        dbObject = dbconn()
        engine = dbObject.getEngine()

        # Truncating table
        with engine.begin() as connection:
            connection.execute(REGISTRY['truncate_table'])

        # 3.- Load CSV file into a pandas dataframe in the size of the icommit variable
        with engine.begin() as connection:
            chunks = pd.read_csv(REGISTRY['file_path'], chunksize=icommit)
            for chunk in chunks:
                chunk.to_sql(REGISTRY['table_name'], schema=REGISTRY['db_schema'], con=engine, index=False, if_exists='append')
                print("Insert {icommit}".format(icommit = icommit))
                icommit += 150
                # if icommit >= 300: This line was added for debugging
                #      break
        
    except Exception as e:
        print("Exeption {}".format(e))

