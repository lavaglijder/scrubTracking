# Roblox game information
GAME_UNIVERSE_ID = 300039023 # Universe id of game to track
GAME_REQUEST_URL = f'https://games.roblox.com/v1/games?universeIds={GAME_UNIVERSE_ID}'

# Roblox group information
GROUP_ID = 3620943 # Group id of group to track
MEMBERS_REQUEST_URL = f'https://groups.roblox.com/v1/groups/{GROUP_ID}'

# Webhook info
DISCORD_WEBHOOKS = { # Dictionary of webhooks to send requests to
    "visits": "", # Visits webhook
    "members": "", # Members webhook
    "playing": "" # Playing webhook
}
TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ" # Time format for tracker time on Discord
VISITS_COUNTDOWN = 1000000 # Milestone frequency (count down to every x number of visits)
MEMBERS_COUNTDOWN = 10000 # Milestone frequency (count down to every x number of members)

# Other
INTERVAL = 60 # Number of seconds between tracking requests
