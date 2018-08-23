# PNRstatusWatcher
On running the script, current PNR status will be sent to the user email.

## Configuring the project
- Edit the conf/config.ini file to provide email and other configurations.

## Run the project
- Provide the inputs in check_pnr_status/input.txt file
    * In the first line provide the PNR number.
    * In the second line provide the email address which we require the pnr status to be sent.
- Go to chek_pnr_status directory and run the below command
```
python pnr_status.py
```
