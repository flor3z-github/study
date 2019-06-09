# check Binary

echo 'check Binary'

if readelf -l $1 2>/dev/null | grep -q 'GNU_RELRO'; then
	if readelf -d $1 2>/dev/null | grep -q 'BIND_NOW'; then
		echo 'Full RELRO'
	else
		echo 'Partial RELRO'
	fi
else
	echo 'No RELRO'
fi

echo ''
# check Process

echo 'check Process'

if readelf -l $1/exe 2>/dev/null | grep -q 'Program Headers'; then
	if readelf -l $1/exe 2>/dev/null | grep -q 'GNU_RELRO'; then
		if readelf -d $1/exe 2>/dev/null | grep -q 'BIND_NOW'; then
			echo 'Full RELRO'
		else
			echo 'Partial RELRO'
		fi
	else
		echo 'No RELRO'
	fi
else
	echo 'Permission Denied'
fi
