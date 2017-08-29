# Shutdown daemon for Raspberry Pi

A daemon that triggers a graceful shutdown upon detecting a falling flank on GPIO 03, which is already used for LLWU.

## Usage

1. Copy the daemon `shutdown_d.py` to /usr/sbin/
2. Make the daemon exectutable: `sudo chmod +x /usr/sbin/shutdown_d.py`
3. Copy `pi_shutdown.rc`to /etc/init.d/
4. Add the service to rc.d: `sudo update-rc.d pi_shutdown defaults` 
5. Reboot
