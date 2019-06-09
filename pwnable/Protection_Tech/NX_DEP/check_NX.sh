# check Binary

echo 'check Binary'

if readelf -W -l $1 2>/dev/null | grep 'GNU_STACK' | grep -q 'RWE'; then
	echo 'NX Disabled'
else
	echo 'NX Enabled'
fi

echo ''
# check Process

echo 'check Process'

if readelf -W -l $1/exe 2>/dev/null | grep 'GNU_STACK' | grep -q 'RWE'; then
	echo 'NX Disabled'
else
	echo 'NX Enabled'
fi

echo ''
# check CPU

echo 'check CPU'

if grep -q nx /proc/cpuinfo; then
	echo 'NX Yes'
else
	echo 'NX No'
fi
