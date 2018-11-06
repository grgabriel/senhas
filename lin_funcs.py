import subprocess

def imprimir(n):
    #lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
    #lpr.stdin.write("10".encode('utf-8'))
    #lpr.terminate()
    subprocess.run(["lp", "-o", "fit-to-page", "-o", "orientation-requested=1", "-d", "TD-4100N", "static/{}.jpg".format(n)])
 
#from escpos.connections import getUSBPrinter
#
#def imprimir(n):
#    print("PRINTING {}".format(n))
#    printer = getUSBPrinter()(idVendor=0x04f9,
#			      idProduct=0x203a,
#                              inputEndPoint=0x81,
#                              outputEndPoint=0x02)
#    printer.text("Test")
#    printer.lf()

