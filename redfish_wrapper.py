#
#  RedFish Wrapper
#
#
# _author_ = Dave Williams <David.A.Williams@Dell.com>
# _version_ = 1.0
#
#
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#

import requests, json, sys, re, time, warnings, os

warnings.filterwarnings("ignore")

try:
    script = sys.argv[1]
    filepath = sys.argv[2]
    idrac_username = sys.argv[3]
    idrac_password = sys.argv[4]

except:
    print("- FAIL: You need SCRIPT NAME / IP ADDRESS TXT FILE / Usernname / Password. Example: \"script_name.py IPLIST.txt root calvin\"")
    sys.exit()




filepath = sys.argv[2]
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
	cmd = "{0} {1} {2} {3}".format(script, line.rstrip(), idrac_username, idrac_password)
	print (script, line.rstrip(), idrac_username, idrac_password)
	os.system(cmd)
