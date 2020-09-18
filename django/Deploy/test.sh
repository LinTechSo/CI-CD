#!/bin/bash
echo ''
echo '.......make sure you have installed simple testing dependencies................'
pkg=curl
which $pkg > /dev/null 2>&1
if [ $? == 0 ];then
	echo "$pkg is already installed."
else
	echo "installed dependencies"
	yum install $pkg -y
fi
ip=$(ip addr | grep inet | head -3 | tail -1 | cut -c10-24 | cut -d '/' -f1)
echo '.....................Test Level One Begin ......................................'
echo ''
res=$(curl --write-out "%{http_code}\n" --silent --output /dev/null "$ip")
if [ $res == "200" ];then
	echo "[+] we got 200 response"
	echo ''
	echo "[+] Test level one passed...."
	echo ''
else
	echo "[-] Error: we received $res response"
	exit 1
fi
echo '.....................Test Level Two Begin ......................................'
echo ''
test=$(curl $ip --silent)
t1=$(echo $test | grep script)
t2=$(echo $test | grep "<a href=" | grep "/static")
if [ ! -z "$t1"  ] && [ ! -z "$t2"  ] ; then
	echo ''
	echo "[+] Test level two passed...."
	echo ''
	curl -Ik $ip --silent
	echo ''
	echo '---------------------------------------------------------------------------------'
else
	echo "Test Level two Failed"
	exit 1
fi

