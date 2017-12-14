OpenBTS sending sms with **list IMSI**

commands are:
```
noz@noz:~/sms$:./imsiquery.py database sendernumber "text message"

noz@noz:~/sms$./imsiquery.py imsi.db 080989999 "Papa minta pulsa, kalau ga papa selingkuh"
noz@noz:~/sms$ ls -lah
total 28K
drwxrwxr-x  3 noz noz 4,0K Des 14 14:03 .
drwxr-xr-x 36 noz noz 4,0K Des 14 13:54 ..
-rwxr-xr-x  1 noz noz 1,6K Des 14 14:14 080989999.sh
drwxrwxr-x  8 noz noz 4,0K Des 14 12:46 .git
-rw-r--r--  1 noz noz 5,0K Des 14 14:02 imsi.db
-rwxrwxr-x  1 noz noz  584 Des 14 12:49 imsiquery.py
noz@noz:~/sms$ cat 080989999.sh 
./OpenBTSCLI sendsms 51011203792XXXX 080989999 "Papa minta pulsa, kalau ga papa selingkuh"
./OpenBTSCLI sendsms 51011000805XXXX 080989999 "Papa minta pulsa, kalau ga papa selingkuh"
./OpenBTSCLI sendsms 51011302505XXXX 080989999 "Papa minta pulsa, kalau ga papa selingkuh"
./OpenBTSCLI sendsms 51011312490XXXX 080989999 "Papa minta pulsa, kalau ga papa selingkuh"
./OpenBTSCLI sendsms 51011050286XXXX 080989999 "Papa minta pulsa, kalau ga papa selingkuh"
./OpenBTSCLI sendsms 51011312508XXXX 080989999 "Papa minta pulsa, kalau ga papa selingkuh"
./OpenBTSCLI sendsms 51011416473XXXX 080989999 "Papa minta pulsa, kalau ga papa selingkuh"
./OpenBTSCLI sendsms 51011011811XXXX 080989999 "Papa minta pulsa, kalau ga papa selingkuh"
./OpenBTSCLI sendsms 51011318304XXXX 080989999 "Papa minta pulsa, kalau ga papa selingkuh"
noz@noz:~/sms$

```
![smsloop](https://user-images.githubusercontent.com/3616842/33979753-62a59574-e0d8-11e7-9a91-f772a2a6abb9.png)



