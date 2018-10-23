@echo off
setlocal
.\curl.exe -L -O http://zlib.net/zlib128.zip
.\unzip.exe .\zlib128
cd zlib-1.2.8
nmake.exe -f .\win32\Makefile.msc
copy zlib1.dll ..\dll\
cd ..\dll\
ren zlib1.dll zlib128.dll