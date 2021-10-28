loglevel = "error"
keepalive = 120
timeout = 90
grateful_timeout = 120

# https://textkool.com/en/ascii-art-generator?hl=default&vl=default&font=Doom&text=PostHog%20%2B%20Toolchain
def on_starting(server):
    print(
        """
\x1b[1;34m"""
        + r"""
______         _   _   _                       _____           _      _           _       
| ___ \       | | | | | |                _    |_   _|         | |    | |         (_)      
| |_/ /__  ___| |_| |_| | ___   __ _   _| |_    | | ___   ___ | | ___| |__   __ _ _ _ __  
|  __/ _ \/ __| __|  _  |/ _ \ / _` | |_   _|   | |/ _ \ / _ \| |/ __| '_ \ / _` | | '_ \ 
| | | (_) \__ \ |_| | | | (_) | (_| |   |_|     | | (_) | (_) | | (__| | | | (_| | | | | |
\_|  \___/|___/\__\_| |_/\___/ \__, |           \_/\___/ \___/|_|\___|_| |_|\__,_|_|_| |_|
                                __/ |                                                     
                               |___/                                                      
"""
        + """
\x1b[0m
"""
    )
    print("Server running on \x1b[4mhttp://{}:{}\x1b[0m".format(*server.address[0]))
