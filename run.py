#!/usr/bin/env python
from app import app

app.secret_key = 'dev' # change this before making app public
app.config['SESSION_TYPE'] = 'filesystem'

app.run(debug=True)
