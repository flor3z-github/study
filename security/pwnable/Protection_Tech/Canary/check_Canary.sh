# check Binary

echo 'check Binary'

if readelf -s $1 2>/dev/null | grep -q '__stack_chk_fail'; then
	echo 'Canary found'
else
	echo 'No Canary found'
fi

echo ''
# check Process

echo 'check Process'

if readelf -s $1/exe 2>/dev/null | grep -q 'Symbol table'; then
	if readelf -s $1/exe 2>/dev/null | grep -q '__stack_chk_fail'; then
		echo 'Canary found'
	else
		echo 'No Canary found'
	fi
else
	if [ "$1" != "1" ] ; then
		echo 'Permission Denied'
	else
		echo 'No Symbol Table found'
	fi
fi
