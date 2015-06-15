
### What this tool does:
- Use this tool to stream watchmegrow video streams (need valid credentials) & store to disk locally.

### Dependencies
- Tested only on windows
- Python (tested using version 3.4.2)
- rtmpdump executable (can be downloaded from https://rtmpdump.mplayerhq.hu/)
- valid watchmegrow credentials

### Installation steps
- Clone this project locally 
`git clone https://github.com/brijs/watchmegrow_streamer.git`
- Download & copy rtmpdump.exe to the project directory.
- Copy and edit `load_credentials.sample.bat` & save as `load_credentials.bat` with your watchmegrow credentials.
- To run: `stream_watchmegrow.bat <cam_num>`, where cam_num is 1 or 2.
- To schedule to run this scripts daily:
  - Launch Task Scheduler & set up 2 Tasks (for camid 1 and camid 2).
  - Set up a Weekly Trigger to run M-F.
  - Set 'Start in' directory to the project directory.
  - Set up "Action" to 'Start a program':
    - `run_stream_watchmegrow.bat 1`
    - `run_stream_watchmegrow.bat 2`
