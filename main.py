
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Conexão com o banco de dados "transactional"
try:
    transactional_db_string = "postgresql://postgres:password@transactional:5432/dvdrental"
    transactional_engine = create_engine(transactional_db_string)
    transactional_Session = sessionmaker(bind=transactional_engine)
    transactional_session = transactional_Session()
    print("Conexão estabelecida com sucesso com bd TRANSACTIONAL")
except:
    print("PROBLEMA NA CONEXAO AO BD TRANSACTIONAL!!!")

# Conexão com o banco de dados "analytics"
try:
    analytics_db_string = "postgresql://postgres:password@analytics:5432/analytics"
    analytics_engine = create_engine(analytics_db_string)
    analytics_Session = sessionmaker(bind=analytics_engine)
    analytics_session = analytics_Session()
    print("Conexão estabelecida com sucesso com bd ANALYTICS")
except:
    print("PROBLEMA NA CONEXAO AO BD ANALYTICS!!!")

#--
#As conexões foram realizadas com o nome dos serviços e ambas com a porta 5432 devido ao fato do container
#que contem o Python estar na mesma rede que os demais.
#--


# Query para selecionar todas as tabelas do banco de dados "transactional"
tables_query = """
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
"""

# Leitura de todas as tabelas do banco de dados "transactional"
tables = pd.read_sql_query(tables_query, transactional_session.bind)

# Loop para ler cada tabela do banco de dados "transactional" e carregá-la no banco de dados "analytics"
for table in tables["table_name"]:
    # Query para selecionar todos os dados da tabela
    data_query = f"SELECT * FROM {table}"
    
    # Leitura dos dados da tabela
    data = pd.read_sql_query(data_query, transactional_session.bind)
    
    # Carga dos dados na tabela correspondente no banco de dados "analytics"
    data.to_sql(table, analytics_session.bind, index=False, if_exists="replace")

# Encerrando conexão com o banco de dados "transactional"
transactional_session.close()
# Encerrando conexão com o banco de dados "analytics"
analytics_session.close()
