@echo off
setlocal
.\curl.exe -L -O http://zlib.net/fossils/zlib-1.2.4.tar.gz
.\unzip.exe .\zlib124
cd zlib-1.2.4
nmake.exe -f .\win32\Makefile.msc
copy zlib1.dll ..\dll\
cd ..\dll\
ren zlib1.dll zlib124.dll