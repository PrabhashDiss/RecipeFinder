# Create a virtual environment (optional) and activate it
$ python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
$ pip install -r src/requirements.txt
$ npm install
$ npm run build

# Run the codebase
$ python3 src/backend/server.py &
$ node src/frontend/index.html

# Optional: Start a development server for frontend (if not using "npm run start")
$ cd src/frontend && webpack serve --open .
