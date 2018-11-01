from escpos.connections import getUSBPrinter

def imprimir(n):
    print("PRINTING {}".format(n))
    printer = getUSBPrinter()(idVendor=0x04f9,
			      idProduct=0x203a,
                              inputEndPoint=0x81,
                              outputEndPoint=0x02)
    printer.text("Test")
    printer.lf()

