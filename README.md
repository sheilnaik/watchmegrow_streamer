
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
- Copy and edit `load_credentials.sample.bat` & save as `load_credentials.bat` with the following information:

1. Login and password to watchmegrow.com
2. Prefix for your center's website. The prefix is the string at the beginning of the camera URL. For example, after logging in if you are directed to https://8938.mywatchmegrowvideo.com/index.php, the prefix is 8938.
3. The path to store your records. Remember to end your path with a /.

### Running
- To run: `stream_watchmegrow.bat <cam_num>`, where cam_num is the number of the camera you'd like to access, starting with 1. For example, if you want to access the fourth camera from the watchmegrow.com drop-down list, the cam_num is 4.
- To schedule to run this scripts daily:
  - Launch Task Scheduler & set up a task for each camera you'd like to record.
  - Set up a Weekly Trigger to run M-F.
  - Set 'Start in' directory to the project directory.
  - Set up "Action" to 'Start a program':
    - `run_stream_watchmegrow.bat 4`
