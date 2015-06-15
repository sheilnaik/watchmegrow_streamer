import os, json, requests
from time import localtime, strftime,sleep
import subprocess
import sys
import argparse
import logging

wmg_url = "https://8938.mywatchmegrowvideo.com/index.php"
wmg_playlist_url = "https://8938.mywatchmegrowvideo.com/ipcameras/playlist.php"
post_data = {"username": os.environ['WMG_USERNAME'], 
			 "password": os.environ['WMG_PASSWORD'], 
			 "login": "Login"}


def stream_cam(dir_name, cam_id, cam_num):
	if not dir_name or not cam_id:
		logging.error("dir(" + dir_name + ") or cam_id(" + cam_id + ") is empty.")
		return

	rtmpdump_cmd = ['rtmpdump', '-r' , 'rtmp://8938.mywatchmegrowvideo.com/live/',
		'-a',  'live/', '-f', 'WIN 13,0,0,214', '-W',
		'https://8938.mywatchmegrowvideo.com/jwplayer6/jwplayer.flash.swf',
		'-p', 'https://8938.mywatchmegrowvideo.com/index.php', '-y', 
		cam_id, '-v', '-o', dir_name + "/" + str(cam_num) + strftime("_%H-%M-%S_", localtime()) + cam_id + ".flv"]

	logging.info("streaming " + cam_id + " to " + dir_name + " ....")
	subprocess.call(rtmpdump_cmd)
	pass


if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
	parser = argparse.ArgumentParser(description='parse camera id')
	parser.add_argument('cam_id', type=int, default=1, help='camera_id (1 or 2)')
	args = parser.parse_args()
	if args.cam_id != 1 and args.cam_id != 2:
		logging.error ("camera_id must be 1 or 2")
		sys.exit(1)


	s = requests.Session()

	MAX_RETRIES = 5
	retriedCount = 0
	while retriedCount < MAX_RETRIES:
		try:
			dir_name = (os.environ['WMG_MEDIA_DIR'] if 'WMG_MEDIA_DIR' in os.environ else 'watchmegrow/') \
				+ strftime("%Y-%m-%d", localtime())
			if not os.path.isdir(dir_name):
				logging.info("Creating dir " + dir_name)
				os.makedirs(dir_name)
			retriedCount = retriedCount + 1
			s.post(wmg_url, post_data)
			r= s.get(wmg_playlist_url)

			playlists = json.loads(r.text)
			logging.info ("Got Playlist: [0] => " + playlists[0]['stream'] +"  [1] => " + playlists[1]['stream'])

			stream_cam(dir_name, playlists[args.cam_id-1]['stream'], args.cam_id)

		except requests.ConnectionError as e:
			logging.warn("Failed to connect to " + wmg_playlist_url)
			logging.warn("retrying "  + str(retriedCount) + "/" + str(MAX_RETRIES))
			logging.warn(e)
			logging.info("sleeping for 1 min")
			sleep(60)
			continue
		except:
			logging.warn("Caught exception during streaming of " + playlists[args.cam_id-1]['stream'])
			logging.warn("retrying "  + str(retriedCount) + "/" + str(MAX_RETRIES))
			logging.info("sleeping for 1 min")
			sleep(60)
			continue

	logging.info("Streaming terminated..")