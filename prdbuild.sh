#!/bin/sh
RUNNER="/bin/bash"
CMD="cd /project && make clean && make publish_prd"
source dockerbase.sh
