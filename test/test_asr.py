import time
from yapykaldi.asr import Asr, WaveFileStreamer
import signal

model_dir = "../data/kaldi-generic-en-tdnn_fl-latest"
model_type = "nnet3"
output_dir = "./output"

asr = Asr(model_dir, model_type, output_dir, WaveFileStreamer('file.wav'))


def interrupt_handle(sig, frame):
    """Interrupt handler that sets the flag to stop recognition and close audio stream"""
    print("Stopping ASR")
    asr.stop()
    time.sleep(3)

# Handle interrupt
signal.signal(signal.SIGINT, interrupt_handle)
asr.start()