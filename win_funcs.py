import tempfile
import win32api
import win32print

def imprimir(n):
    filename = tempfile.mktemp (".txt")
    open (filename, "w").write ("Teste")
    win32api.ShellExecute (
        0,
        "printto",
        filename,
        '"%s"' % win32print.GetDefaultPrinter (),
        ".",
        0
    )