[![Board Status](https://dev.azure.com/PixHike/671eab8c-4049-428e-8382-68ac7878f53f/9629bdf9-58bf-498e-ad7e-db4025f1d043/_apis/work/boardbadge/99c9f1b7-1d06-48a8-b61a-422d6ab84574)](https://dev.azure.com/PixHike/671eab8c-4049-428e-8382-68ac7878f53f/_boards/board/t/9629bdf9-58bf-498e-ad7e-db4025f1d043/Microsoft.RequirementCategory)    [![CodeScene general](https://codescene.io/images/analyzed-by-codescene-badge.svg)](https://codescene.io/projects/69802)    [![Build](https://github.com/mookechee/tdm-macos/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/mookechee/tdm-macos/actions/workflows/ci.yml)

[![CodeScene Average Code Health](https://codescene.io/projects/69802/status-badges/average-code-health)](https://codescene.io/projects/69802)      [![CodeScene Hotspot Code Health](https://codescene.io/projects/69802/status-badges/hotspot-code-health)](https://codescene.io/projects/69802)  [![CodeScene Missed Goals](https://codescene.io/projects/69802/status-badges/missed-goals)](https://codescene.io/projects/69802)    [![CodeScene System Mastery](https://codescene.io/projects/69802/status-badges/system-mastery)](https://codescene.io/projects/69802)

# Twitch Drops Miner

This application allows you to AFK mine timed Twitch drops, without having to worry about switching channels when the one you were watching goes offline, claiming the drops, or even receiving the stream data itself. This helps you save on bandwidth and hassle.

### How It Works:

Every several seconds, the application pretends to watch a particular stream by fetching stream metadata - this is enough to advance the drops. Note that this completely bypasses the need to download any actual stream video and sound. To keep the status (ONLINE or OFFLINE) of the channels up-to-date, there's a websocket connection established that receives events about streams going up or down, or updates regarding the current amount of viewers.

[![Buy me a coffee](https://i.imgur.com/cL95gzE.png)](
    https://buymeacoffee.com/t4rjsfbmvbl
)