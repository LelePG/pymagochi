from audioplayer import AudioPlayer
import time

def notificar():
    player = AudioPlayer("audio/mixkit-retro-game-notification-212.wav")
    player.play()
    time.sleep(1.3)
    player.stop()

def finalizar():
    player = AudioPlayer("audio/mixkit-arcade-retro-game-over-213.wav")
    player.play()
    time.sleep(1.3)
    player.stop()