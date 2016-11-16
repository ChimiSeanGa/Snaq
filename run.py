#!/usr/bin/env python
from app import app

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

app.run(debug=True)
