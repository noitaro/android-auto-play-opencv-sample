# This Python file uses the following encoding: utf-8

# pip install android-auto-play-opencv
import android_auto_play_opencv as am

adbpath = '..\\platform-tools\\'

def main():

    aapo = am.AapoManager(adbpath)
    
    while True:
    
        # 画面キャプチャ
        aapo.screencap()
        
        # 早送りボタンは常にタップ
        if aapo.touchImg('./umamusume/hayaokuri.png'):
            # タップ出来たら待機
            aapo.sleep(1)
    
        # Google Playダイアログが出たら、キャンセルの位置をタップ
        elif aapo.chkImg('./umamusume/google-play.png'):
            aapo.touchPos(135, 630)
            aapo.sleep(1)

if __name__ == '__main__':
    main()