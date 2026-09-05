#!/bin/bash
# Daily Content Engine — runs at 11:55 PM to generate that day's content.
# Add to crontab: 55 23 * * * /root/StallShark/tool/cron_daily.sh

set -e

DATE=$(date +%Y-%m-%d)
LOG_DIR="/root/StallShark/logs"

# Get day number from CompanyDay records (not a separate counter)
DAY_NUM=$(ls /root/StallShark/mythicbee-ops/days/ 2>/dev/null | wc -l)
if [ "$DAY_NUM" -eq 0 ]; then
    DAY_NUM=1
fi

# Generate content
cd /root/StallShark
python3 tool/daily_content.py \
    --date "$DATE" \
    --day "$DAY_NUM" \
    2>&1 | tee -a "$LOG_DIR/cron.log"

echo "$(date): Generated Day $DAY_NUM content" >> "$LOG_DIR/cron.log"
