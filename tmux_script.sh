#!/bin/bash
MY_PATH=$(dirname $(realpath -s $0))
# Create a new tmux session named pmk
SESSION_NAME="pmk"
/usr/bin/tmux new-session -d -s $SESSION_NAME}
/usr/bin/tmux set-option -t ${SESSION_NAME} remain-on-exit on
/usr/bin/tmux send-keys -t ${SESSION_NAME} "source /root/.bashrc" C-m
/usr/bin/tmux send-keys -t ${SESSION_NAME} "source /root/.profile" C-m
/usr/bin/tmux send-keys -t ${SESSION_NAME} "date" C-m
/usr/bin/tmux send-keys -t ${SESSION_NAME} "source virtenv/bin/active" C-m
/usr/bin/tmux send-keys -t ${SESSION_NAME} "./Lab1/MQTT/led.py" C-m
/usr/bin/tmux split-window -t ${SESSION_NAME}
/usr/bin/tmux send-keys -t ${SESSION_NAME} "./Lab1/MQTT/switch_led.py" C-m
/usr/bin/tmux split-window -t ${SESSION_NAME}
/usr/bin/tmux send-keys -t ${SESSION_NAME} "./Lab1/MQTT/button.py" C-m
