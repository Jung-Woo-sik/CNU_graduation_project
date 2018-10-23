@echo off
setlocal
.\curl.exe -L -O http://zlib.net/zlib128.zip
::: 다른 버전의 경우 http://zlib.net/fossils/에 들어가시면 나와있습니다.
::: 단 해당 경우 tar.gz 확장자를 지원하여 아직 수정중에 있습니다.
.\unzip.exe .\zlib128
cd zlib-1.2.8
nmake.exe -f .\win32\Makefile.msc
copy zlib1.dll ..\dll\
cd ..\dll\
ren zlib1.dll zlib128.dll