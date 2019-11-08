# DataEngineering-FileToSQLServerChuncks
This code reads data from heavy CSV files, reading in chunks for the best approach of inserting data into an SQLServer.

### 1.- Installing the requirements
The code contains the requirements.txt, create a virtual env using this file before attempting to execute it. Once cloned, cd over the new directory.

```sh
$ git clone ~/DataEngineering-FileToSQLServerChuncks.git
$ conda create -n FileToSQLServerChuncks python=3.7
$ conda activate FileToSQLServerChuncks
$ pip install requirements.txt
```

## Authors
* **Enrique Plata** - *2019-10-05*