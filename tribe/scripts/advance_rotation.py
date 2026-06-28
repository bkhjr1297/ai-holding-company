#!/usr/bin/env python3
from tribe.calc.rotation import advance_rotation, load_state
import json

if __name__ == '__main__':
    result = advance_rotation(load_state(), steps=1)
    print(json.dumps(result, indent=2))
