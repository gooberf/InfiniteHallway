import random
possibleLogs = [
'[2025-11-11 20:28:58.123] [PID:1542] [TID:0x7f4e2c6d] [INFO] CacheAccess: Request ID: RND-8A9F-B3C0-D7E1 | Key: user_session:0xABC12345 | Action: **MISS** | Duration: 4.5ms',
'[2025-11-11 20:28:58.210] [PID:1543] [TID:0x7f4e2c6e] [DEBUG] CacheStore: Key: asset_data:IMG-7234X | Size: 12096 bytes | Policy: LFU | Status: **STORED** | TTL: 300s',
'[2025-11-11 20:28:58.355] [PID:1542] [TID:0x7f4e2c6d] [INFO] CacheAccess: Request ID: RND-5B6C-CDE2-EFE3 | Key: user_config:john.doe | Action: **HIT** | Duration: 0.1ms',
'[2025-11-11 20:28:58.490] [PID:1544] [TID:0x7f4e2c6f] [WARN] CacheEviction: Policy triggered: LRU | Keys evicted: 15 | Total freed: 40960 bytes | Reason: Memory threshold',
'[2025-11-11 20:28:58.501] [PID:1545] [TID:0x7f4e2c70] [INFO] CacheAccess: Request ID: RND-7D8E-F012-3456 | Key: product_info:P-9901 | Action: **HIT** | Duration: 0.08ms',
'[2025-11-11 20:28:58.622] [PID:1543] [TID:0x7f4e2c6e] [DEBUG] CacheStore: Key: geo_data:NY-001 | Size: 450 bytes | Policy: FIFO | Status: **STORED** | TTL: 60s',
'[2025-11-11 20:28:58.789] [PID:1542] [TID:0x7f4e2c6d] [ERROR] CacheAccess: Request ID: RND-1G2H-3I4J-5K6L | Key: invalid_key:NULL | Action: **FAIL** | Message: Invalid key format',
'[2025-11-11 20:28:58.814] [PID:1545] [TID:0x7f4e2c70] [INFO] CacheAccess: Request ID: RND-6M7N-8O9P-0Q1R | Key: financial_rpt:Q3-2025 | Action: **MISS** | Duration: 12.1ms',
'[2025-11-11 20:28:58.930] [PID:1544] [TID:0x7f4e2c6f] [DEBUG] CacheManagement: Flush operation initiated | Scope: partial | Keys affected: 500',
"[2025-11-11 20:29:00.005] [PID:1542] [TID:0x7f4e2c6d] [INFO] CacheAccess: Request ID: RND-2S3T-4U5V-6W7X | Key: api_response:user/100 | Action: **HIT** | Duration: 0.15ms",
"[2025-11-11 20:29:00.111] [PID:1543] [TID:0x7f4e2c6e] [WARN] CacheEviction: Key: temporary_file:0x1B2C3D | Size: 81920 bytes | Reason: Explicit **EVICT** call",
"[2025-11-11 20:29:00.250] [PID:1545] [TID:0x7f4e2c70] [INFO] CacheAccess: Request ID: RND-8Y9Z-A0B1-C2D3 | Key: template_html:home | Action: **MISS** | Duration: 2.9ms"
]

def invHelper():
    while True:
        with open('functions/invHelper/latest.log', 'a') as log_file:
            choice = random.choice(possibleLogs)
            log_file.write(choice + '\n')