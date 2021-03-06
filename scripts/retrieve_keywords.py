from pyo import *

t = "PyoObject|PyoTableObject|example|class_args|pa_count_devices|pa_get_default_input|pa_get_default_output|pa_list_devices|pa_get_output_devices|pa_get_input_devices|pm_count_devices|pm_list_devices|pm_get_input_devices|pm_get_default_input|pm_get_output_devices|pm_get_default_output|sndinfo|midiToHz|midiToTranspo|BandSplit|Biquad|Clip|Compress|Counter|DCBlock|Delay|Disto|Dummy|Fader|Follower|Freeverb|Granulator|Hilbert|Input|InputFader|Metro|Midictl|Mix|Noise|Notein|Osc|OscReceive|OscSend|Pan|Pattern|Phasor|Pointer|Port|PyPattern|SPan|TrigEnv|TrigRand|TrigChoice|TrigFunc|Select|SfMarkerShuffler|SfPlayer|Sig|Sine|TableRec|Tone|Waveguide|LinTable|NewTable|SndTable|HannTable|HarmTable|Server|Stream|TableStream|SigTo|Map|SLMap|SLMapFreq|SLMapMul|SLMapPhase|SLMapQ|SLMapDur|SLMapPan|Clean_objects|Pulsar|TableRead|Thresh|SawTable|SquareTable|ZCross|Degrade|Lookup|ChebyTable|Adsr|Convolve|TableMorph|sampsToSec|secToSamps|Randi|Randh|Choice|RandInt|FM|Cloud|Linseg|WGVerb|Trig|CosTable|CurveTable|Score|SineLoop|OscLoop|Print|Sin|Cos|Tan|Abs|Sqrt|Log|Log2|Log10|Pow|Xnoise|XnoiseMidi|TrigXnoise|TrigXnoiseMidi|Snap|Change|PyoMatrixObject|NewMatrix|MatrixRec|MatrixPointer|TrigLinseg|Interp|SampHold|EQ|CallAfter|Switch|Selector|savefile|Compare|ExpTable|Expseg|TrigExpseg|Allpass|Allpass2|Phaser|Harmonizer|Record|Biquadx|Chorus|SfMarkerLooper|Beat|Looper|Percent|MatrixMorph|TableIndex|DataTable|Seq|TrigRandInt|SDelay|Mixer|AllpassWG|Blit|PinkNoise|CrossFM|Between|Mirror|Wrap|BrownNoise|IRWinSinc|IRAverage|IRPulse|IRFM|Rossler|Lorenz|LFO|MidiAdsr|Denorm|FreqShift|OscBank|Follower2|Gate|ParaTable|FourBand|FFT|IFFT|Atan2|CarToPol|PolToCar|FrameDelta|FrameAccum|TrigTableRec|OscDataSend|OscDataReceive|Floor|Round|ControlRec|ControlRead|reducePoints|NoteinRec|NoteinRead|CtlScan|MidiDelAdsr|Ceil|Bendin|Touchin|Programin|DBToA|AToDB|WinTable|serverCreated|serverBooted|Timer|RandDur|Vectral|Scale|Iter|MToF|distanceToSegment|rescale|Biquada|upsamp|downsamp|VoiceManager|XnoiseDur|SincTable|MToT|linToCosCurve|CentsToTranspo|TranspoToCents|VarPort|getVersion|pa_count_host_apis|pa_get_default_host_api|pa_list_host_apis|OscListReceive|Count|Urn|NextTrig"
t2 = t.split("|")

tree = OBJECTS_TREE
l = []
for k1 in tree.keys():
    if type(tree[k1]) == type({}):
        for k2 in tree[k1].keys():
            for val in tree[k1][k2]:
                l.append(val)
    else:
        for val in tree[k1]:
            l.append(val)
l.append("PyoObject")
l.append("PyoTableObject")
l.append("PyoMatrixObject")
l.append("Server")

with open("pyo_keywords.txt", "w") as f:
    for i, word in enumerate(l):
        if word not in t2:
            print(word)
        if (i % 10) == 0:
            f.write("\n")
        f.write(word + " ")

