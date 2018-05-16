<html><head>
<meta charset="UTF-8" />
<title>Ki?m tra tên mi?n</title>
</head>
<body>
<input id="domain" maxlength="512" name="domain" type="text" />&nbsp&nbsp<a href="#" onclick="window.location.href='check.php?domain='+document.getElementById('domain').value;"><font face="tahoma" size="2" color="green"><b>Ki?m tra</b></font></a><br>
<?php 
$domain = $_GET['domain'];
function check_domain($domain)
{
$dot = explode(".",$domain);a
$dot = $dot[1];
if  (!$domain)
{
echo '<font color="blue" face="tahoma" size="2"><b>Nh?p d?y d? tên mi?n và ph?n m? r?ng.</b></font><br><font face="tahoma" size="2">VD: shopthoitrang.com</font>';
}elseif(strpos($domain, ".")===false){
echo '<font color="red" face="tahoma" size="2"><b>B?n chua nh?p ph?n m? r?ng.</b></font><br><font face="tahoma" size="2">VD: shopthoitrang.com</font>';
}elseif($dot == "vn" || $dot== "com.vn"  ||  $dot == "net.vn"  ||  $dot == "org.vn"  ||  $dot == "info.vn"  ||  $dot == "gov.vn"  ||  $dot == "edu.vn"  ||  $dot == "biz.vn"  ||  $dot == "name.vn"  ||  $dot == "pro.vn"  ||  $dot == "health.vn"  ||  $dot == "ac.vn" ||  $dot == "com" ||  $dot == "net"  ||  $dot == "org"  ||  $dot == "info"  ||  $dot == "us"  ||  $dot == "biz"  ||  $dot == "cc"  ||  $dot == "asia"  ||  $dot == "eu"  ||  $dot == "me"  ||  $dot == "tel"  ||  $dot == "ws"  || $dot == "name"  ||  $dot == "tv"  ||  $dot == "mobi"  ||  $dot == "bz"  ||  $dot == "mn"  ||  $dot == "in"  ||  $dot == "co.uk"  ||  $dot == "co"  ||  $dot == "ca"  ||  $dot == "es"  ||  $dot == "de"  ||  $dot == "xxx"  ||  $dot == "com.ru"  ||  $dot == "pro"  ||  $dot == "sx"  ||  $dot == "pw"  ||  
$dot == "nl"  ||  $dot == "la"  ||  $dot == "solar"  ||  $dot == "house"  ||  $dot == "florist"  ||  $dot == "coffee"  ||  $dot == "marketing"  ||  $dot == "farm"  ||  $dot == "cool"  ||  $dot == "watch"  ||  $dot == "bargains"  ||  $dot == "boutique"  ||  $dot == "cheap"  ||  $dot == "zone"){
$kq= file_get_contents("http://www.whois.net.vn/whois.php?domain=".$domain) ;
if  ($kq==0)
{
$check = '<font color="green" face="tahoma" size="2"><b>B?n có th? dang ký tên mi?n này.</b></font>';
}
elseif($kq==1)
{
$check = '<font color="red" face="tahoma" size="2"><b>Tên mi?n này dã du?c dang ký.</b></font>';
}
}else{
$check = '<font color="red" face="tahoma" size="2"><b>Ph?n m? r?ng b?n nh?p không dúng</b></font>';
}
return $check;
}


echo check_domain($domain);


?></div>
</body>
</html>