# email-public-ip
Scheduler to trigger email if their is an ip change

Go To SystemCtl service file directory(/etc/systemd/system)
Copy the files emailip.service && emailip.timer

Reload the service files to include the new service.
```sudo systemctl daemon-reload```

Start your service
```
sudo systemctl start emailip.service
sudo systemctl start emailip.timer
```

To check the status of your service
```
sudo systemctl status emailip.service
sudo systemctl status emailip.timer
```

To enable your service on every reboot
```
sudo systemctl enable emailip.service
sudo systemctl enable emailip.timer
```

To disable your service on every reboot
```
sudo systemctl disable emailip.service
sudo systemctl disable emailip.timer
```

Reference https://www.shubhamdipt.com/blog/how-to-create-a-systemd-service-in-linux/
