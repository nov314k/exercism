#!/usr/bin/env bash

if [ -z "$1" ]; then
	echo "ERROR: Please provide a directory to start searching in."
	exit 126
else
	files=$(find $1 -not -path '*/vendor/*' -name '*.c' -or -not -path '*/vendor/*' -name '*.h')
	dos2unix $files
	indent $files -linux -nut -i3
	dos2unix $files
fi
