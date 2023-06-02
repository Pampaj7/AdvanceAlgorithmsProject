import sys
from colorama import init, Fore, Back

# Inizializza il modulo colorama
init()


def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', color=Fore.RED):
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write('\r%s |%s| %s%% %s' %
                     (prefix, color + bar + Fore.RESET, percent, suffix))
    sys.stdout.flush()
