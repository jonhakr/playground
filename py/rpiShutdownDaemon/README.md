# Shutdown daemon for Raspberry Pi

A daemon that triggers a graceful shutdown upon detecting a falling flank on GPIO 03, which is already used for LLWU.

## Usage

1. Copy the daemon to sudo bin: `sudo cp shutdown_d.py /usr/sbin/shutdown_d.py`
2. Make the daemon exectutable: `sudo chmod +x /usr/sbin/shutdown_d.py`
3. Copy the service initscript: `sudo cp pi_shutdown.rc /etc/init.d/pi_shutdown.rc`
4. Make the script executable: `sudo chmod +x /etc/init.d/pi_shutdown.rc`
5. Add the service to rc.d: `sudo update-rc.d pi_shutdown.rc defaults` 
6. Reboot
