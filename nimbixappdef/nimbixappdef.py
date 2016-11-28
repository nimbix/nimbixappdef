#
# Copyright (c) 2016, Nimbix, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are
# those of the authors and should not be interpreted as representing official
# policies, either expressed or implied, of Nimbix, Inc.
#

from collections import OrderedDict
import simplejson as json


def new(name, desc, author, licensed=True, machines=['*'],
        classifications=['Uncategorized'],
        vaults=['FILE', 'BLOCK', 'OBJECT'], image=None):
    '''
    Creates a new AppDef initialized with meta data

    Required parameters:
        name(string): the short name of the application
        desc(string): the description of what the application does

    Optional parameters:
        licensed(bool):         True if the application contains license
                                (if applicable);
                                default: True
        machines(list):         list of machine types or machine type wildcards
                                the application can run on;
                                default: *
        classifications(list):  list of classifications/categories the
                                application belongs under;
                                default: Uncategorized
        vaults(list):           list of vault type the application supports;
                                default: FILE, BLOCK, and OBJECT
                                also valid: NONE (for no vault) and
                                BLOCK_ARRAY (for distributed FS)
        image(string):          graphic file with icon to embed (max 64kb)
                                default: no graphic
                                must be either png or jpg

    Returns:
        the AppDef object, which can be modified with other accessors before
        rendering; it may be treated as a dict
    '''
    appdef = OrderedDict()
    return appdef


def add(appdef, id, desc, path, interactive=True, name=None, args=[]):
    '''
    Adds a command with some optional constant positional arguments.
    A command maps an executable (and arguments) to an API endpoint with
    optional parameters.

    Required parameters:
        appdef(dict):       AppDef object to modify (from new_appdef())
        id(string):         command ID (should not have spaces)
        desc(string):       the description of what the command does

    Optional parameters:
        interactive(bool):  True if users should be able to reach the
                            runtime environment with a public IP while running;
                            default: True
        name(string):       user-facing short name of the command
                            default: same as id
        args(list):         positional arguments for command
                            default: none

    Notes:
        - for security, set interactive=False for any command which does
          not require user interaction while running; stdout and stderr
          will still be available to user via API and web interface
        - positional arguments should be separated as if using exec() - e.g.:
            ls -l /data
          should be added like this:
              add_command(<appdef>, <id>, <desc>, False, args=['-l', '/data'])

    Returns:
        no value, but modifies AppDef object in place
    '''
    return


def dump(appdef, f=None):
    '''
    Dumps an appdef object as JSON either to a stream or a string.

    Required parameters:
        appdef(dict):   AppDef object to dump (from new_appdef())

    Optional parameters:
        f(stream):      stream to dump AppDef to;
                        default: return as string instead

    Returns:
        string without pretty-printing if f=None, or AppDef dumped if f is set
    '''
    if f is None:
        return json.dumps(appdef)
    else:
        json.dump(appdef, f, indent=4)
