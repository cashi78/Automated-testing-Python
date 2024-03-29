from sqlalchemy import create_engine


dbcs = 'postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet'
db = create_engine(dbcs).connect()
s = session.query(company).all()
print(s)
