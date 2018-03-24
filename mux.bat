"C:/Program Files/MKVToolNix\mkvmerge.exe" --ui-language en --output ^"E:\an8\temp\temp.mkv^" --no-subtitles --language 0:und --default-track 0:yes --language 1:jpn --default-track 1:yes ^"^(^" ^"E:\an8\temp\%~1^" ^"^)^" --language 0:und --track-name 0:GarisMiring-an8 --default-track 0:yes ^"^(^" ^"E:\an8\temp\%~2^" ^"^)^" --chapters ^"E:\an8\temp\%~3^" --track-order 0:0,0:1,1:0
E:\an8\mux.py -i %1
push_sett.bat
twitter.py
@pause