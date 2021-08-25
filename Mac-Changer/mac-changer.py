import subprocess
import optparse

def parser():
    parse = optparse.OptionParser()
        # optparse.OptionParser() is function which will look for command line argument
    parse.add_option("-m" , "--mac " , dest = "new_mac" , help="specify new mac  ")
    parse.add_option("-i" , "--interface " , dest = "interface" , help="Specify interface you want change it's mac address")
        # here we make options that OptionParser() should expect
    (options , argumets ) = parse.parse_args()
        # here we parse arguments and values that add_option had taked
    if not options.interface :
        parse.error("please specify Interface You wanna use ")
    elif not options.new_mac :
        parse.error(" please specify the New Mac address ")
    return options
        # here return will go to the option the is not specified


def MacChanger (interface , mac ) :
    print("[+] Chaninging The " + interface + " to the " + mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Your MAC Address has been changed to " + mac + " [+] ")
        # we used subprocess.call to execute those commands

options = parser()
    # at this point all values of arguments or vlaues of options will be in function and we move them to a variable so we can use them
MacChanger(options.interface , options.new_mac)
    # here we use our function and specified agruments inside options
