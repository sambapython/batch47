import logging
import sqlite3
'''
logging.basicConfig(level=logging.WARN,
    filename="log.txt",
    format="%(asctime)s=>%(levelname)s==>%(message)s")
'''
import f1
logging.basicConfig(level=logging.DEBUG,
    filename="log.txt",
    format="%(asctime)s=>%(levelname)s==>%(message)s")
logging.info("Starting the proces..")
try:
    con = sqlite3.connect("db1.db")
    logging.info("Connected well to DB")
    cur=con.cursor()
    logging.info("created a cursor")
    q=None
    logging.info("Showing menu to the user")
    print "Search by:\n\t1. id\n\t2.name"
    search_opt=raw_input("Enter am option:")
    logging.debug("selected option: %s"%search_opt)
    if search_opt=="1":
        logging.info("providing search by id")
        p_id=raw_input("Enter id of the per:")
        q="select * from customer where id=%s"%p_id
    elif search_opt=="2":
        p_name=raw_input("Enter name of the per:")
        q="select * from customer where name='%s'"%p_name
        logging.info("providing search by name")
    else:
        print "select proper option.."
    if q:
        logging.debug("query: %s"%q)
        cur.execute(q)
        logging.info("query executed successfully!!")
        data=cur.fetchall()
        logging.debug("data: %s"%data)
        print data
except Exception as err:
    print err
    logging.error(err.message)
finally:
    con.close()
    logging.info("closing the connection")
logging.info("Done with the searching process..")