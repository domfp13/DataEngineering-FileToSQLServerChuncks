# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 CompuCom, All Rights Reserved
# Created by Enrique Plata

import pyodbc
import urllib
from sqlalchemy import create_engine

class dbconn():
    """
    This class creates a engine/connection object 
    """

    def __init__(self):
        """
        This function is call when and object of this class is created
        """
        self.engine = None
        self.server = 'SPW099SQL12VA\\NODE_A' 
        self.database = 'Clerk' 
        self.username = 'omsuser' 
        self.password = 'LHI7cYBH' 

    def getEngine(self):
        quoted = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+self.server+";DATABASE="+self.database+";UID="+self.username+";PWD="+self.password)
        self.engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
        return self.engine
        
        
    
