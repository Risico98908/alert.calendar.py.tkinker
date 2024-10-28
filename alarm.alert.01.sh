#ignore this file
# Copy each service file to the systemd directory
sudo cp /0.myfiles/notify.02.service /etc/systemd/system/
sudo cp /0.myfiles/notify.04.service /etc/systemd/system/
sudo cp /0.myfiles/notify.05.service /etc/systemd/system/


# Reload systemd to recognize new service files
sudo systemctl daemon-reload


# Enable each service to start on boot
sudo systemctl enable notify.02.service
sudo systemctl enable notify.04.service
sudo systemctl enable notify.05.service

# Start each service immediately
sudo systemctl start notify.02.service
sudo systemctl start notify.04.service
sudo systemctl start notify.05.service



sudo systemctl status notify.02.service
sudo systemctl status notify.04.service
sudo systemctl status notify.05.service
