
# Common Signals
[![GitHub](https://img.shields.io/github/v/release/Stoupy51/CommonSignals?logo=github&label=GitHub)](https://github.com/Stoupy51/CommonSignals/releases/latest)
[![Smithed](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.smithed.dev%2Fv2%2Fpacks%2Fcommon_signals%2Fmeta&query=%24.stats.downloads.total&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDQgNCIgeG1sbnM6dj0iaHR0cHM6Ly92ZWN0YS5pby9uYW5vIj48cGF0aCBkPSJNLjczNy44NTlsLjg4Ny0uMjg1Yy4wOTktLjAzMi4yMDUtLjAzMi4zMDQgMGwxLjMzNS40MjktMS4wNC4zMzR6bS0uMTk1LjE4OXYuNDg3YzAgLjEwNS4wNjguMTk5LjE2OC4yMzFsMS41MTQuNDg3TDMuMjkgMS45MWMuMS0uMDMyLjE2OC0uMTI2LjE2OC0uMjMxdi0uNDg3bC0xLjIzNC4zOTF6bS44NTkgMS4xOWwuODIzLjI2LjQxMi0uMTI3di4zNzlsLS40MTIuMTMyLS44MjMtLjI2NHptLS40NDguNTA1di4yOTlsMS4yNzIuNDA4LjgyMy0uMjY0di0uM2wtLjgyMy4yNTl6IiBwYWludC1vcmRlcj0ic3Ryb2tlIGZpbGwgbWFya2VycyIgZmlsbD0iIzFiNDhjNCIvPjwvc3ZnPg%3D%3D&logoColor=224bbb&label=Smithed&labelColor=black&color=224bbb)](https://smithed.net/packs/common_signals)
[![Modrinth](https://img.shields.io/modrinth/dt/common_signals?logo=modrinth&label=Modrinth)](https://modrinth.com/datapack/common_signals)
[![Discord](https://img.shields.io/discord/1216400498488377467?label=Discord&logo=discord)](https://discord.gg/anxzu6rA9F)
[![Python Datapack](https://img.shields.io/github/v/release/Stoupy51/python_datapack?logo=github&label=Python%20Datapack)](https://github.com/Stoupy51/PythonDatapackTemplate)

📚 Common Signals is a library datapack that provides signals through function tags to help developers optimize their datapacks.<br>
The initial goal is to prevent multiple datapacks from ticking the same inefficient `@e` selectors.

## Available Signals 📡

🔔 Common Signals provides several function tags that developers can hook into:
- `#common_signals:signals/on_new_item` - 📦 Triggered when a new item entity is detected in the world (not having the `common_signals.checked` tag)

Feel free to suggest new signals!

## Usage for Developers 🔧
1. 📦 Create a datapack that depends on Common Signals
2. ➕ Add functions to the signal tags you want to listen to 
3. ⚡ Your functions will be called whenever those signals are triggered

