import subprocess

# Print the requested number
# Uses subprocess to run a linux command sending the
# image to the receipt printer

def imprimir(n):
    subprocess.run(["lp", "-o", "fit-to-page", "-o", "orientation-requested=1", "-d", "TD-4100N", "/home/sonigate/Projects/senhas/static/{}.jpg".format(n)])

