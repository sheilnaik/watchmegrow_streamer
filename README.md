
### What this tool does:
- Use this tool to stream watchmegrow video streams (need valid credentials) & store to disk locally.

### Dependencies
- Tested only on windows
- Python (tested using version 3.4.2)
- rtmpdump executable (can be downloaded from https://rtmpdump.mplayerhq.hu/)
- valid watchmegrow credentials

### Installation steps
- clone this project locally - `git clone https://github.com/brijs/watchmegrow_streamer.git`
- copy rtmpdump.exe to the project directory
- copy load_credentials.sample.bat & save as `load_credentials.bat` with your watchmegrow credentials
- To run: `stream_watchmegrow.bat <cam_num>`
