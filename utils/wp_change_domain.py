import os, sys, re
import optparse
try:
    import MySQLdb
except ImportError:
    print 'Except: sudo pip install MySQL-python\n'
    sys.exit()
try:
    from netifaces import interfaces, ifaddresses, AF_INET
except ImportError:
    print 'Except: sudo pip install netifaces\n'

def DBConnect(mdb_addr, mdb_id, mdb_pw, mdb_dbname, wp_addr):
    con = MySQLdb.connect(mdb_addr, mdb_id, mdb_pw, mdb_dbname)
    with con:
        cur = con.cursor()
        cur.execute("UPDATE wp_options set option_value = %s WHERE option_name = %s or option_name = %s",(wp_addr,"siteurl", "home"))
        print "\n\tUser:\t\t%s" %(mdb_id)
        print "\tPassword:\t%s" %(mdb_pw)
        print "\tDatabase:\t%s" %(mdb_dbname)
        print "\tAddress:\t%s" %(mdb_addr)
        print "\tChange Address:\t%s\n" %(wp_addr)
        print "%s database update complete" %(mdb_dbname)

def NETInterface(opt_target):
    if opt_target in interfaces():
        ip_addr = ifaddresses(opt_target).setdefault(AF_INET, [{'addr':'No IP addr'}])[0]['addr']
        full_path = 'http://%s' %(ip_addr)
    return full_path

def RewriteURL(opt_target):
    if bool(re.search('^((https)\:\/\/)([0-9a-zA-Z\-]+\.)+[a-zA-Z]{2,6}(\:[0-9]+)?(\/\S*)?$',opt_target)):
        opt_target = 'http://' + opt_target[8:]
        print 'do not use https, change to http'
    elif bool(re.search('^((http)\:\/\/)([0-9a-zA-Z\-]+\.)+[a-zA-Z]{2,6}(\:[0-9]+)?(\/\S*)?$',opt_target)):
        opt_target = opt_target
    else:
        opt_target = 'http://' + opt_target
    return opt_target

def run():
    parser =  optparse.OptionParser('\n Version: 0.1\n' +\
                                    '\n\twp_change_domain.py -u [MySQL User Name]' +\
                                    ' -p [MySQL Password] -n [MySQL Database Name]' + \
                                    ' -t [IP or Domain]\n' +\
                                    '\t(if -t option is null, default use eth0 IP)\n' + \
                                    '\t(if -s options is null, default use \'localhost\')\n')

    parser.add_option('-u', '--user', dest='USER', type='string', help='input MySQL user name')
    parser.add_option('-p', '--password', dest='PW', type='string', help='input MySQL user password')
    parser.add_option('-n', '--dbname', dest="DB", type='string', help='input database name')
    parser.add_option('-t', '--target', dest='PATH', type='string', help='input IP or Domain')
    parser.add_option('-s', '--server', dest='SERVER', type='string', help='input MySQL server address')
    (options, args) = parser.parse_args()

    try:
        opt_user = options.USER
        opt_pw = options.PW
        opt_dbname = options.DB
        opt_target = options.PATH
        opt_server = options.SERVER

        if opt_target is None:
            opt_target = NETInterface('eth0')
        else:
            opt_target = RewriteURL(opt_target)

        if opt_server is None:
            opt_server = 'localhost'

        DBConnect(opt_server, opt_user, opt_pw, opt_dbname, opt_target)

    except TypeError as e:
        parser.print_help()
#        print e


if __name__=='__main__':
    run()
