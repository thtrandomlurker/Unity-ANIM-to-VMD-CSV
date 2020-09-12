import json
import sys

#don't ask how, but i ALWAYS end up with at least one of these
curr_curveset = int(0)

with open(sys.argv[1], 'r') as f:
    with open(f'{sys.argv[1][:-4]}csv', 'w') as out:
        data = json.load(f)
        while True:
            if curr_curveset == int(len(data["AnimationClip"]["m_FloatCurves"])):
                break
            for i in data["AnimationClip"]["m_FloatCurves"][curr_curveset]["curve"]["m_Curve"]:
                _serializedVersion = i["serializedVersion"]
                _time = i["time"]
                _value = i["value"]
                _inSlope = i["inSlope"]
                _outSlope = i["outSlope"]
                _tangentMode = i["tangentMode"]
                _weightedMode = i["weightedMode"]
                _inWeight = i["inWeight"]
                _outWeight = i["outWeight"]
                
                frames = int(float(_time * 30))
                
                
                #print(_value)
                
                #move the node name data here, so it can exist for all necessary writes
                
                blend_node_name = data["AnimationClip"]["m_FloatCurves"][curr_curveset]["attribute"]
                
                out.write(f'{blend_node_name},{frames},{float(_value / 100)}\n')
                
#surprisingly, this is the least janky code i've ever written i think
                
            
            
            
            curr_curveset += 1
