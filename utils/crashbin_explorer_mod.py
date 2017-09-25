#!c:\\python\\python.exe

import getopt
import sys
sys.path.append(r"../../../paimei")

from boofuzz import utils

USAGE = "\nUSAGE: crashbin_explorer.py <xxx.crashbin>"                                      \
        "\n    [-t|--test #]     dump the crash synopsis for a specific test case number"   \
        "\n    [-g|--graph name] generate a graph of all crash paths, save to 'name'.udg\n"

#
# parse command line options.
#

try:
    if len(sys.argv) < 2:
        raise Exception

    opts, args = getopt.getopt(sys.argv[2:], "t:g:", ["test=", "graph="])
except Exception:
    print USAGE
    sys.exit(1)

test_number = graph_name = graph = None

for opt, arg in opts:
    if opt in ("-t", "--test"):
        test_number = int(arg)
    if opt in ("-g", "--graph"):
        graph_name  = arg

try:
    crashbin = utils.crash_binning.CrashBinning()
    crashbin.import_file(sys.argv[1])
except Exception:
    print "unable to open crashbin: '%s'." % sys.argv[1]
    sys.exit(1)

#
# display the full crash dump of a specific test case
#

for _, crashes in crashbin.bins.iteritems():
    for crash in crashes:
        print '-------------------------------------------------------------'
        print 'TEST CASE: %s' %crash.extra
        print ''
        print crashbin.crash_synopsis(crash)
        print '\r\n-------------------------------------------------------------'

