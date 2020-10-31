"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>

    authors: 	            Psycho <https://github.com/Psychokiller1888>
                            philipp2310 <https://github.com/philipp2310>

	retired or
	inactive authors:       Jierka <https://github.com/jr-k>
							maxbachmann <https://github.com/maxbachmann>
"""

import subprocess

subprocess.run(['clear'])

try:
	from pathlib import Path
	import json

	conf = json.loads(Path('debug_server.json').read_text())
	if not conf['enable']:
		raise Exception

	import pydevd_pycharm

	pydevd_pycharm.settrace(conf['server'], port=conf['port'], stdoutToServer=conf['stdout'], stderrToServer=conf['stderr'])
except:
	# Do nothing, this is only for debug server, advanced stuff
	pass

import logging.handlers
from datetime import datetime
from core.util.model import FileFormatting, BashFormatting

_logger = logging.getLogger('ProjectAlice')
_logger.setLevel(logging.INFO)

date = int(datetime.now().strftime('%Y%m%d'))
logsMountpoint = Path(Path(__file__).resolve().parent, 'var', 'logs')

logFileHandler = logging.FileHandler(filename=f'{logsMountpoint}/logs.log', mode='w')
rotatingHandler = logging.handlers.RotatingFileHandler(filename=f'{logsMountpoint}/{date}-logs.log', mode='a', maxBytes=100000, backupCount=20)
streamHandler = logging.StreamHandler()

logFileFormatter = FileFormatting.Formatter()
bashFormatter = BashFormatting.Formatter()
logFileHandler.setFormatter(logFileFormatter)
rotatingHandler.setFormatter(logFileFormatter)
streamHandler.setFormatter(bashFormatter)

_logger.addHandler(logFileHandler)
_logger.addHandler(rotatingHandler)
_logger.addHandler(streamHandler)

from core.Initializer import Initializer

Initializer().initProjectAlice()
