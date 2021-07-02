from audioplayer import AudioPlayer
import time

def notificar():
    """Reproduz o audio de notificação estipulado"""
    player = AudioPlayer("audio/mixkit-retro-game-notification-212.wav")
    player.play()
    time.sleep(1)
    player.stop()

def finalizar():
    """Reproduz o audio de fim de jodo estipulado"""
    player = AudioPlayer("audio/mixkit-arcade-retro-game-over-213.wav")
    player.play()
    time.sleep(1)
    player.stop()