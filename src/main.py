from connect_db import fn_connect_to_db


## correct way to import function from another file
def fn_fetch_data():
    print('connecting to db')
    new_var = fn_connect_to_db()
    return new_var

## incorrect way to import function from another file
#var_1 = fn_connect_to_db()
#print(var_1)

def main():
    print('project start')
    new_var = fn_fetch_data()
    print(new_var)
    print('project end')


if __name__ == '__main__':
    main()