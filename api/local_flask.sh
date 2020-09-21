#!/bin/bash
#Run the toolbox flask entrypoint
export ENVIRONMENT=development
export FLASK_APP=/api/run.py
pushd /tmp
flask "$@"
popd /tmp
