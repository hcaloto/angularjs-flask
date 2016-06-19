# -*- coding:utf-8 -*-
# AngularJS and Flask
#
#    run.py
#

import os
from app import create_app

try:
    app = create_app(os.getenv('NSL_CONFIG') or 'development')
except Exception as exc:
    raise RuntimeError(exc)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
