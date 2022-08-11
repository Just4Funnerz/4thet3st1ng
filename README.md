# 4thet3st1ng
This was just an attempt at something I've never tried before.

###################\n
Please make sure to first install the requirements.
The script doesn't require much actions from the user aside of logging into the Gmail account to upload the file.

1. pip3 install -r requirements.txt
2. It should install PyDrive with the additional libraries, all of the other pre-exists within Python 3.7 and above.
3. Run main.py.
4. That's it.

The script will do all tasks from 3,a - 3,f.

- Create a password-read-protected archive (Varonica.zip) 
- ![image](https://user-images.githubusercontent.com/111051486/184109642-5828aee5-b57b-43d2-837a-b4873e48b632.png)
- Store 3 files inside (Var.txt, Oni.txt, S.txt), remove all of them and then extract from the zip only 1 (S.txt)
- ![image](https://user-images.githubusercontent.com/111051486/184109388-3f05ad2c-a4ac-490c-9377-f2dbb4e09e51.png)
- Calculate the sha-256 of it, store it inside the S.txt file. Afterwards, create an unprotected zip (Varonisa.zip)
- ![image](https://user-images.githubusercontent.com/111051486/184109599-21ef611e-c70b-44d8-821e-8d9e9ad0a560.png)
- Store inside the unprotected zip, the S.txt file and upload to Google Drive (not any specific folder):
- ![image](https://user-images.githubusercontent.com/111051486/184109773-d3d31595-ac96-4fb5-9686-f2b8cda6d13e.png)
- The zip is uploaded.

The rest of the task I ran out of time trying to figure out the exact requests, therefore I believe this is a DNF.
Thanks for the opportunity.

P.S.
This is a newly registered email.\n
####################
