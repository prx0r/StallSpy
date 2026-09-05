#!/bin/bash
# Daily Content Engine — runs at 11:55 PM to generate that day's content.
# Add to crontab: 55 23 * * * /root/StallSpy/tool/cron_daily.sh

set -e

DATE=$(date +%Y-%m-%d)
DAY_FILE="/root/StallSpy/.experiment_day"
LOG_DIR="/root/StallSpy/logs"

# Increment day counter
if [ ! -f "$DAY_FILE" ]; then
    echo "1" > "$DAY_FILE"
fi
DAY_NUM=$(cat "$DAY_FILE")
DAY_NUM=$((DAY_NUM + 1))
echo "$DAY_NUM" > "$DAY_FILE"

# Generate content
cd /root/StallSpy
python3 tool/daily_content.py \
    --date "$DATE" \
    --day "$DAY_NUM" \
    2>&1 | tee -a "$LOG_DIR/cron.log"

echo "$(date): Generated Day $DAY_NUM content" >> "$LOG_DIR/cron.log"
