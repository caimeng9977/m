import sqlite3
def get_conn_cur(db:str):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    return conn, cur
def update_sql(db, table:str, up: dict, f:list=None):
    """..."""
    con, cur = get_conn_cur(db=db)
    if up:
        ft = lambda x: str(x) if isinstance(x, (int,float)) else "'" + x + "'"

        t = [f"{k}={ft(v)}" for k, v in up.items()]
        c = ",".join(t)
    if f:
        t = lambda : str(f[-1]) if isinstance(f[-1],(int,float))else "'" + "'"
        f[-1] = t()
        w = " ".join(f)
        sql =f"""update {table} set {c} where {w};"""
    else:
        sql = f"""update {table} set {c};"""
    print(sql)
    cur.execute(sql)
    con.commit()
    con.close()
    con.close()
if __name__=='__main__':
    update_sql(db="students.db", table="stu1210",up={"teacher": "zgs", "class": "人工智能2班"}, f=["class","=", "人工智能2班"])