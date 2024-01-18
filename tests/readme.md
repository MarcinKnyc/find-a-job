```
pip install -e ../job_search_postgres
pip install -e ../job_search_qdrant
pip install -r requirements.txt
source ../job_search_postgres/set_connection_variables_debug.sh
source ../job_search_qdrant/set_env_vars_local.sh
python exact_matches_test.py
```

