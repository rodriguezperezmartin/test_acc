from connect_db import fn_connect_to_db, fn_connect_to_db2

## correct way to import function from another file
def fn_fetch_data():
    print('connecting to db 1')
    db_var = fn_connect_to_db()
    return db_var

def fn_fetch_data2():
    print('connecting to db 2')
    db_var = fn_connect_to_db2()
    return db_var

## incorrect way to import function from another file
#var_1 = fn_connect_to_db()
#print(var_1)

def main():
    print('project start')

    db_var = fn_fetch_data()
    print(db_var)

    db_var2 = fn_fetch_data2()
    print(db_var2)

    print('project end')


if __name__ == '__main__':
    main()