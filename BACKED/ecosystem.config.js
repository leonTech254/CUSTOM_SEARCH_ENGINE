module.exports = {
  apps: [
    {
      "name": "leonteqsecurityapi3",
      "script": "app.py",
      "args": [],
      "instances": "1",
      "wait_ready": true,
      "autorestart": false,
      "max_restarts": 5,
      //"interpreter": "../.venv/bin/python",
      "interpreter": "/root/PYTHONBACKEDS/.venv/bin/python",
    }
  ],
};










